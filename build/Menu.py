from __future__ import print_function
import os
import grpc
import broker_pb2
import broker_pb2_grpc

# ========================= MENUS ============================
def Menu(stub: broker_pb2_grpc.BrokerStub):
    while True:
        try:
            os.system("cls")
            opt = int(inputOptionsGeneral())
            if opt == 1:
                os.system("cls")
                menuPublisher(stub)
            if opt == 2:
                os.system("cls")
                print("Menu de suscriptor aquí...")
                os.system("sleep 2")
            if opt == 3:
                os.system("cls")
                response = stub.Ping(broker_pb2.ping(msg="Ping a servidor"))
                print(f"[SERVIDOR]: {response.msg}")
                os.system("sleep 2")
            elif opt == 0:
                os.system("cls")
                break

        except:
            print("\n[ERROR] Tipo de dato no valido, solo enteros...")
            os.system("sleep 2")
        

def menuPublisher(stub: broker_pb2_grpc.BrokerStub):
    while True:
        os.system("cls")
        opt = int(inputOptionsPublisher())
        if opt == 1:
            os.system("cls")
            nombreTema = crearTema()

            response = stub.Crear_topic(broker_pb2.crear_topic_req(nombre=nombreTema))

            if response.creado == False:
                print(f"\n   [X][SERVER] {response.razon}")
            else:
                print("\n   [Y][SERVER] Topico creado correctamente")
                print(f"\n   Nombre: {response.nombre}  ID: {response.topicId}")
            
            os.system("pause")
                
        elif opt == 2:
            os.system("cls")
            print("Menu publicar en tema aquí...")
            os.system("sleep 2")
        elif opt == 3:
            os.system("cls")
            print("______Lista de temas existentes______")

            for topics in stub.Listar_topics(broker_pb2.listar_topics_req()):
                print(f"ID: {topics.topicId}    Nombre: {topics.nombreTopic}")

            os.system("pause")
        elif opt == 0:
            break
        else:
            print("[AVISO] Opción no valida, elegir las mostradas en la lista")
            os.system("sleep 2")
        




# ========== MOSTRAR GENERAL ==========

def showOptionsGeneral():
    listaMenu = """============ MESSAGE BROKER - Pub/Sub ============

        [1] Publicador
        [2] Suscriptor
        [3] Ping a servidor
        [0] Salir
            
            > """

    return listaMenu

def inputOptionsGeneral():
    return input(showOptionsGeneral())

# ========== MOSTRAR PUBLISHER ==========
def showOptionsPublisher():
    listaMenu = """============ MESSAGE BROKER - Menu Publicador ============
        [1] Crear tema
        [2] Publicar en tema
        [3] Listar temas creados
        [0] Volver
            
            > """
    return listaMenu

def inputOptionsPublisher():
    return input(showOptionsPublisher())

# ========== MOSTRAR CREADOR DE TOPICS ==========

def showCrearTema():
    listaMenu = """============ MESSAGE BROKER - Crear Tema ============
        [!] Inserta el nombre del tema
            
            > """
    return listaMenu

def crearTema():
    return input(showCrearTema())