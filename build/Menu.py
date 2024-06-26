from __future__ import print_function
import os
import grpc
import broker_pb2
import broker_pb2_grpc
import threading as th

import keyboard

from logic.Topic import *

global kill_thread

# ========================= MENUS ============================
class Menu():

    def __init__(self, stub : broker_pb2_grpc.BrokerStub):
        self.topicsCreados = ListaTopics()
        self.topicsSuscritos = ListaTopics()
        self.stub = stub
        self.listenersTopics : list[th.Thread] = []
        self.topicos_activos = set()

    def start(self):
        globals()["kill_thread"] = False

        self.stub.Ping(broker_pb2.ping(msg="Ping from client"))

        while True:
            try:
                os.system("cls")
                opt = int(self.inputOptionsGeneral())
                if opt == 1:
                    os.system("cls")
                    self.menuPublisher()
                if opt == 2:
                    os.system("cls")
                    self.menuSuscriptor()
                elif opt == 0:
                    os.system("cls")
                    break

            except grpc.RpcError:
                print("\n[X][SERVIDOR] Servidor caido, levante el servidor para continuar")
                os.system("pause")
            except:
                print("\n[ERROR] Tipo de dato no valido, solo enteros...\n")
                os.system("pause")
        

    def menuPublisher(self):
        while True:
            os.system("cls")
            opt = int(self.inputOptionsPublisher())

            if opt == 1:
                os.system("cls")
                nombreTema = self.crearTema()

                response = self.stub.Crear_topic(broker_pb2.crear_topic_req(nombre=nombreTema))

                if response.creado == False:
                    print(f"\n   [X][SERVER] {response.razon}")
                else:
                    print("\n   [Y][SERVER] Temas creado correctamente")
                    print(f"\n   Nombre: {response.nombre}  ID: {response.topicId}")
                    

                os.system("pause")

            elif opt == 2:
                os.system("cls")
                print("_____________________ ELEGIR TOPICS _____________________")
                for t in self.stub.Listar_topics(broker_pb2.listar_topics_req()):
                    print(f"Nombre: {t.nombreTopic}  ID: {t.topicId}")
                print("\n")

                topicId = input("Introducir ID del tema\n\n   > ")
                res = self.stub.Publicar_mensaje(broker_pb2.publicar_mensaje_req(mensaje="$2a$12$6MCe7W8YqBD0kFmAJJ18XOrAx58d4Rw.mwdwMkKDKS4FU3t6QxvKO", topicId=topicId))
                topicMensaje = input("\nMensaje: ")
                
                response = self.stub.Publicar_mensaje(broker_pb2.publicar_mensaje_req(mensaje=topicMensaje, topicId=topicId))

                if response.publicado == False:
                    print(f"[X][SERVIDOR] {response.razon}")
                else:
                    print("[Y][SERVIDOR] Mensaje enviado con exito")

                os.system("pause")
            elif opt == 3:
                os.system("cls")
                print("______Lista de temas existentes______")

                for topics in self.stub.Listar_topics(broker_pb2.listar_topics_req()):
                    print(f"ID: {topics.topicId}    Nombre: {topics.nombreTopic}")

                os.system("pause")
            elif opt == 0:
                break
            else:
                print("[AVISO] Opción no valida, elegir las mostradas en la lista")
                os.system("pause")
        

    def menuSuscriptor(self):
        while True:
            os.system("cls")
            opt = int(self.inputSuscriptorMenu())
            if opt == 1:
                for topics in self.stub.Listar_topics(broker_pb2.listar_topics_req()):
                    print(f"|   ID: {topics.topicId}    Nombre: {topics.nombreTopic}")

                topicId = input("\n   ID del tema a suscribirse:\n        > ")
            
                res = self.stub.Suscribirse_topic(broker_pb2.suscribirse_req(topicId=topicId))

                if res.suscrito == False:
                    print("\n[X] El tema no existe, selecciona otro tema\n")
                else:
                    self.topicsSuscritos.insertarTopic(Topic(res.topicId, res.nombreTopic))
                    self.topicsSuscritos.topics[-1].setTopicId(topicId=res.topicId)
                    print(f"\n[Y] Suscrito al tema {res.nombreTopic} exitosamente\n")

                os.system("pause")
                
            elif opt == 2:
                self.iniciarListeners()

                print("================= ESCUCHANDO MENSAJES =================")
                print("[NOTA] Apretar tecla 'esc' para salir del modo escucha\n")
                #for t in self.listenersTopics:
                 #   print(t.getName())
                  #  print(t.is_alive())
                while True:
                    if keyboard.is_pressed('esc'):
                        globals()["kill_thread"] = True
                        break;


            elif opt == 3:
                os.system("clear")

                print("________________ LISTA DE TEMAS SUSCRITOS __________________")
                for t in self.topicsSuscritos.topics:
                    print(f"|   ID: {t.getTopicId()}    Nombre: {t.getNombre()}")

                os.system("pause")
            elif opt == 0:
                os.system("cls")
                break

    
    def iniciarListeners(self):
        globals()["kill_thread"] = False
        idWorker : int = 0;

        for t in self.topicsSuscritos.topics:
            idWorker += 1
            topic_id = t.getTopicId()
            if topic_id not in self.topicos_activos:
                self.topicos_activos.add(topic_id)
                threadAux = th.Thread(target=worker, name=f"listener ({topic_id})", args=(self.stub, t.getTopicId(),))
                self.listenersTopics.append(threadAux)
                threadAux.start()

            

    # ========== MOSTRAR GENERAL ==========
    def showOptionsGeneral(self):
        listaMenu = """============ MESSAGE BROKER - Pub/Sub ============

            [1] Publicador
            [2] Suscriptor
            [0] Salir

                > """

        return listaMenu

    def inputOptionsGeneral(self):
        return input(self.showOptionsGeneral())

    # ========== MOSTRAR PUBLISHER ==========
    def showOptionsPublisher(self):
        listaMenu = """============ MESSAGE BROKER - Menu Publicador ============
            [1] Crear tema
            [2] Publicar en tema
            [3] Listar temas creados
            [0] Volver

                > """
        return listaMenu

    def inputOptionsPublisher(self):
        return input(self.showOptionsPublisher())

    # ========== MOSTRAR CREADOR DE TOPICS ==========

    def showCrearTema(self):
        listaMenu = """============ MESSAGE BROKER - Crear Tema ============
            [!] Inserta el nombre del tema

                > """
        return listaMenu

    def crearTema(self):
        return input(self.showCrearTema())
    
    def showSuscriptorMenu(self):
        listaMenu = """============ SUSCRIPTOR - Menu ============
            [1] Suscribirse a un tema
            [2] Ver mensajes de temas suscritos
            [3] Listar temas suscritos
            [0] Volver
            
                > """

        return listaMenu
    
    def inputSuscriptorMenu(self):
        return input(self.showSuscriptorMenu())
        


def worker(stub : broker_pb2_grpc.BrokerStub, topicId : str):

    try:
        res = stub.Recibir_topic(broker_pb2.mensaje_req(topicID=topicId))
        if res.status == False:
            print(f"[{res.nombre}]: {res.mensaje}")
    
        while True:
            #if globals()["kill_thread"] == True:
                #break;
            res = stub.Recibir_topic(broker_pb2.mensaje_req(topicID=topicId))
            if res.status and globals()["kill_thread"] == False:
                if res.mensaje != "$2a$12$6MCe7W8YqBD0kFmAJJ18XOrAx58d4Rw.mwdwMkKDKS4FU3t6QxvKO":
                    print(f"[{res.nombre}]: {res.mensaje}")
    except:
        print("Hilo finalizado")