import threading as th

class Topic():

    def __init__(self, topicId: str = "", nombre: str = ""):
        self.__topicId = topicId
        self.__nombre = nombre
        self.__buffer = []
        self.__mutex_publicar = th.Lock()
        self.__cond_var = th.Condition()
    
    # Getters
    def getTopicId(self) -> str:
        return self.__topicId
    def getNombre(self) -> str:
        return self.__nombre
    def getBuffer(self) -> list[str]:
        return self.__buffer
    
    # Setters
    def setTopicId(self, topicId: str):
        self.__topicId = topicId
    def setNombre(self, nombre: str):
        self.__nombre = nombre

    def publicarMsg(self, mensaje: str):
        self.__cond_var.acquire()

        self.__buffer.append(mensaje)

        self.__cond_var.notify_all()
        
        self.__cond_var.release()
    
    
    def leerMsg(self):
        self.__cond_var.acquire()
        self.__cond_var.wait()

        msg = self.__buffer[-1]

        self.__cond_var.release()

        return msg
    
    def toString(self) -> str:
        return f"ID: {self.__topicId}   Nombre: {self.__nombre}"
        


class ListaTopics():
    def __init__(self):
        self.topics : list[Topic] = []
        self.can = 0
    
    def buscarTopic(self, topicNombre : str) -> Topic:
        for t in self.topics:
            if t.getNombre() == topicNombre:
                return t
    
        return None
    
    def buscarTopicId(self, topicId : str) -> Topic:
        for t in self.topics:
            if t.getTopicId() == topicId:
                return t
    
        return None
        
    def existeTopic(self,topicNombre: str) -> bool:
        if self.buscarTopic(topicNombre) == None:
            return False
        return True
    
    def insertarTopic(self, topic : Topic) -> Topic:
        self.can += 1
        topicId = str(self.can)
        topic.setTopicId(topicId)
        self.topics.append(topic)

        return topic
    
    def toString(self) ->str:
        s = ""

        for t in self.topics:
            s += f"{t.toString()}\n"
        
        return s
    

