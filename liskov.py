import abc

class animal(abc.ABC):
    @abc.abstractmethod
    def numpatas(self):
        pass

class gato(animal):
    def numpatas(self):
        return 4

class grillo(animal):
    def numpatas(self):
        return 6

def imprimir(animales):
    for animal in animales:
        print(animal.numpatas())

if __name__ == '__main__':
    array_animales = [gato(), grillo()]
    imprimir(array_animales)
