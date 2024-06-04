from concurrent import futures

import datetime as dt

import logging

import grpc
import broker_pb2
import broker_pb2_grpc

from logic.Topic import Topic
from logic.Topic import ListaTopics

listaTopics = ListaTopics()

port = "50100"

class Broker(broker_pb2_grpc.BrokerServicer):
    def Ping(self, request, context):
        Broker.registrarBitacora(f"Nuevo cliente conectado al servidor en el puerto {port}")
        return broker_pb2.ping(msg="Servidor está levantado")
    
    def Crear_topic(self, request, context):
        if listaTopics.existeTopic(request.nombre) == False:
            topic_aux = Topic(nombre=request.nombre)
            topic_aux = listaTopics.insertarTopic(topic_aux)
            
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
                return broker_pb2.publicar_mensaje_res(publicado=True)
        return broker_pb2.publicar_mensaje_res(publicado=False, razon=f"El Tema con ID {request.topicId} no se pudo encontrar")

    @staticmethod 
    def registrarBitacora(msg : str):
        fechaActual = dt.datetime.now()
        bitacora = f"{fechaActual.day}/{fechaActual.month}/{fechaActual.year}:{fechaActual.hour}:{fechaActual.minute}:{fechaActual.second} {msg}\n"

        arch = open(f"../bitacoras/log{fechaActual.day}_{fechaActual.year}.txt", "a")

        arch.write(bitacora)

        arch.close()
        

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