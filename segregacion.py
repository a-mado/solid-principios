import abc

class iave(abc.ABC):
    @abc.abstractmethod
    def comer(self):
        pass

class iavevoladora(abc.ABC):
    @abc.abstractmethod
    def volar(self):
        pass

class iavenadadora(abc.ABC):
    @abc.abstractmethod
    def nadar(self):
        pass

class loro(iave, iavevoladora):
    def comer(self):
        pass

    def volar(self):
        pass

class pinguino(iave, iavenadadora):
    def comer(self):
        pass

    def nadar(self):
        pass