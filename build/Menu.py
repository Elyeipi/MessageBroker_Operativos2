from __future__ import print_function
import os
import grpc
import broker_pb2
import broker_pb2_grpc

from logic.Topic import *

# ========================= MENUS ============================
class Menu():

    def __init__(self, stub : broker_pb2_grpc.BrokerStub):
        self.topicsCreados = ListaTopics()
        self.topicsSuscritos = ListaTopics()
        self.stub = stub

    def start(self):
        self.stub.Ping(broker_pb2.ping(msg="Ping from client"))

        while True:
            #try:
            os.system("cls")
            opt = int(self.inputOptionsGeneral())
            if opt == 1:
                os.system("cls")
                self.menuPublisher()
            if opt == 2:
                os.system("cls")
                print("Menu de suscriptor aquí...")
                os.system("sleep 2")
            elif opt == 0:
                os.system("cls")
                break

            # except grpc.RpcError:
            #     print("\n[X][SERVIDOR] Servidor caido, levante el servidor para continuar")
            #     os.system("pause")
            # except:
            #     print("\n[ERROR] Tipo de dato no valido, solo enteros...\n")
            #     os.system("pause")
        

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
                    self.topicsCreados.insertarTopic(Topic(response.topicId, response.nombre))
                    print("____________________Topics Creados____________________\n")
                    print(self.topicsCreados.toString())
                    

                os.system("pause")

            elif opt == 2:
                os.system("cls")
                print("_____________________ ELEGIR TOPICS CREADOS _____________________")
                print(self.topicsCreados.toString())
                print("\n")

                topicNombre = input("Introducir nombre del tema\n\n   > ")

                topicAux = self.topicsCreados.buscarTopic(topicNombre)
                topicMensaje = input("\nMensaje: ")
                
                response = self.stub.Publicar_mensaje(broker_pb2.publicar_mensaje_req(mensaje=topicMensaje, topicId=topicAux.getTopicId()))

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
                os.system("sleep 2")
        

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
    
    # def imprimirTopicsCreados(self):
    #     print(f"\n\n________Lista de topics creados________\n")
    #     for t in self.topicsCreados:
    #         print(f"ID: {t.getTopicId()}  Nombre: {t.getNombre()}")
    #     print("\n")
        

    # def imprimirTopicsSuscritos(self):
    #     print(f"\n\n________Lista de topics suscritos________\n")
    #     for t in self.topicsSuscritos:
    #         print(f"ID: {t.getTopicId()}  Nombre: {t.getNombre()}")
    #     print("\n")