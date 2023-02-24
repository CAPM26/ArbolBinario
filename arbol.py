
from nodo import Nodo
class Arbol:

    def __init__(self, dato):
        self.raiz = Nodo(dato)

    def existe(self, busqueda):
        return self.__existe(self.raiz, busqueda)

    # -----------funciones privadas llevan _ recomendado
    def __existe(self, n, busqueda): 
        if n is None:
            return False
        if n.dato == busqueda:
            return True
        elif busqueda < n.dato:
            return self.__existe(n.izdo, busqueda)
        else:
            return self.__existe(n.dcho, busqueda)
    
    def insertar(self, dato):
        if self.raiz is None:
            self.raiz = dato
        else:
            self.__insertar(self.raiz, dato)

    def __insertar(self, padre, dato):
        if dato > padre.dato:
            if padre.dcho is None:
                padre.dcho = Nodo(dato)
            else:
                self.__insertar(padre.dcho, dato)
        else:
            if padre.izdo is None:
                padre.izdo = Nodo(dato)
            else:
                self.__insertar(padre.izdo, dato)

    def __preorden(self, nodo):
        if nodo is not None:
            print(nodo.dato, end=", ")
            self.__preorden(nodo.izdo)
            self.__preorden(nodo.dcho)
    
    def preorden(self):
        print("imprimiendo árbol preorden: ")
        self.__preorden(self.raiz)
        print("")
