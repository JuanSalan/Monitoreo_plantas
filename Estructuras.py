from math import *
import random
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
    def __str__(self):
        return str(self.dato)
class Pila:
    def __init__(self):
        self.superior = None
        self.size = 0
    def __len__(self):
        return self.size
    def apilar(self, dato):
        if self.superior == None:
            self.superior = Nodo(dato)
            self.size+=1
            return
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.superior
        self.superior = nuevo_nodo
        self.size+=1
    def __str__(self):
        st = "["
        cur = self.superior
        for i in range(self.size):
            st += str(cur)
            if i != len(self) - 1:
                st += str(", ")
            cur = cur.siguiente
        st += "]"
        return st
    def desapilar(self):
        a = 0
        if self.superior == None:
            return print("No hay ningún elemento en la pila para desapilar")
        a = self.superior.dato
        self.superior = self.superior.siguiente
        self.size-=1
        return a 
class nodeCola:
    def __init__(self,Value):
        self.Value = Value
        self.next = None
    def __str__(self):
        return str(self.Value)  
class cola:
    def __init__(self):
        self.First = None
        self.Last = None
        self.size = 0
    def __len__(self):
        return self.size
    def encolar(self,x):
        nuevoNodo = nodeCola(x)
        if self.Last:
            self.Last.next = nuevoNodo
            self.Last = nuevoNodo
        else:
            self.First  = nuevoNodo
            self.Last = nuevoNodo
        self.size += 1
    def __str__(self):
        st = "["
        cur = self.First
        for i in range(len(self)):
            st += str(cur)
            if i != len(self) - 1:
                st += str(", ")
            cur = cur.next
        st += "]"
        return st
    def desencolar(self):
        if self.First != None:
            valor = self.First.Value
            self.First = self.First.next
            self.size -=1
            if self.First == None:
                self.Last = None    
            return valor 
        else:     
            raise ValueError("La cola está vacía")
class node:
    def __init__(self,Value):
        self.Value = Value
        self.next = None
    def __str__(self):
        return str(self.Value)
class linkedList:
    def __init__(self):
        self.first = None
        self.size = 0
    def append(self, value):
        miNode = node(value)
        if self.size == 0:
            self.first =miNode
        else:
            cur = self.first
            while cur.next != None:
                cur = cur.next
            cur.next = miNode
        self.size += 1
        return miNode
    def __len__(self):
        return self.size
    def __str__(self):
        st = "["
        cur = self.first
        for i in range(len(self)):
            st += str(cur)
            if i != len(self) - 1:
                st += str(", ")
            cur = cur.next
        st += "]"
        return st
    def get(self,index):
        if index >= self.size:
            return None
        cur_id = 0
        curNode = self.first
        while True:
            if cur_id == index: return curNode.Value
            curNode = curNode.next
            cur_id += 1





