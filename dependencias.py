import abc

class conexion():
    @abc.abstractmethod
    def getdatos(self):
        pass

    @abc.abstractmethod
    def setdatos(self):
        pass

class accesodatos():
    def __init__(self, conexion):
        self.conexion = conexion

    def getdatos(self):
        self.conexion.getdatos()


class databaseservice(conexion):
    def getdatos(self):
        pass

    def setdatos(self):
        pass


class apiservice(conexion):
    def getdatos(self):
        pass

    def setdatos(self):
        pass
