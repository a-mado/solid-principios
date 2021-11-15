import abc
class animal(abc.ABC):
    @abc.abstractmethod
    def animal_caminar(self):
        pass

class gato(animal):
    def animal_caminar(self):
        return True

class perro(animal):
    def animal_caminar(self):
        return True

class pez(animal):
    def animal_caminar(self):
        return False

def imprimir(animales:list[animal]):
    for animal in animales:
        print(animal.animal_caminar())
if __name__ == "__main__":
    array_animales = [gato(), perro(), pez()]
    imprimir(array_animales)