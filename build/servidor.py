from concurrent import futures

import datetime as dt

import threading as th

import logging

import grpc
import broker_pb2
import broker_pb2_grpc

from logic.Topic import Topic
from logic.Topic import ListaTopics

BUFFER_MAX = 50
BUFFER_VACIO = 0

#Mutexes y semaforos disponibles
mutex_bitacora = th.Lock()
mutex_crear_tema = th.Lock()
semaforo_lleno = th.Semaphore(BUFFER_MAX)
semaforo_vacio = th.Semaphore(BUFFER_VACIO)

listaTopics = ListaTopics()

port = "50100"

class Broker(broker_pb2_grpc.BrokerServicer):
    def Ping(self, request, context):
        Broker.registrarBitacora(f"Nuevo cliente conectado al servidor en el puerto {port}")
        return broker_pb2.ping(msg="Servidor está levantado")
    
    def Crear_topic(self, request, context):
        if listaTopics.existeTopic(request.nombre) == False:
            topic_aux = Topic(nombre=request.nombre)

            # MUTEX debe estar cerca de cond. carrera. Talvez un mutex dentro de lista.

            mutex_crear_tema.acquire()
            topic_aux = listaTopics.insertarTopic(topic_aux)
            mutex_crear_tema.release()
            
            print(listaTopics.toString())

            Broker.registrarBitacora(f"""Tema creado "{topic_aux.getNombre()} ID({topic_aux.getTopicId()})" """)

            return broker_pb2.crear_topic_res(nombre=topic_aux.getNombre(), topicId=topic_aux.getTopicId(), creado=True)
        else:
            return broker_pb2.crear_topic_res(razon=f"El tema especificado {request.nombre} ya existe", creado=False)
        
    def Listar_topics(self, request, context):
        for t in listaTopics.topics:
            yield broker_pb2.listar_topics_res(topicId=t.getTopicId(), nombreTopic=t.getNombre())

    def Publicar_mensaje(self, request, context):
        topicAux = None
        for t in listaTopics.topics:
            if t.getTopicId() == request.topicId:
                t.publicarMsg(request.mensaje)
                print(f"Mensaje publicado en topic ({t.getTopicId()}): {request.mensaje}")
                Broker.registrarBitacora(f"Cliente {context.peer()} publico mensaje en {t.getNombre()}: {request.mensaje}")
                return broker_pb2.publicar_mensaje_res(publicado=True)
        return broker_pb2.publicar_mensaje_res(publicado=False, razon=f"El Tema con ID {request.topicId} no se pudo encontrar")

    def Suscribirse_topic(self, request, context):
        topicAux = listaTopics.buscarTopicId(request.topicId)

        if topicAux != None:
            Broker.registrarBitacora(f"Cliente {context.peer()} suscrito al tema {topicAux.getNombre()}")
            return broker_pb2.suscribirse_res(topicId=topicAux.getTopicId(), nombreTopic=topicAux.getNombre(), suscrito=True)
        
        return broker_pb2.suscribirse_res(suscrito=False)
    
    def Recibir_topic(self, request, context):
        topicAux = listaTopics.buscarTopicId(request.topicID)
        listaTops = []

        # CONDICION SEMAFORO

        if topicAux != None:
            #semaforo_lleno.acquire()

            for msg in topicAux.getBuffer():
                yield broker_pb2.mensaje_res(mensaje=msg)

            #semaforo_vacio.release()

        #listaTops.append(broker_pb2.mensaje_res(mensaje="semL", valorSem=semaforo_lleno._value))
        #listaTops.append(broker_pb2.mensaje_res(mensaje="semV", valorSem=semaforo_vacio._value))

        #yield listaTops
            
        



    @staticmethod
    def registrarBitacora(msg : str):
        fechaActual = dt.datetime.now()
        bitacora = f"{fechaActual.day}/{fechaActual.month}/{fechaActual.year}:{fechaActual.hour}:{fechaActual.minute}:{fechaActual.second} {msg}\n"

        mutex_bitacora.acquire()
        arch = open(f"../bitacoras/log{fechaActual.day}_{fechaActual.year}.txt", "a")

        arch.write(bitacora)

        arch.close()
        mutex_bitacora.release()
        

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    broker_pb2_grpc.add_BrokerServicer_to_server(Broker(), server)
    server.add_insecure_port("[::]:"+port)
    server.start()
    print(f"Server escuchando en {port}")
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()