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
    def get(self,index):
        if index >= self.size:
            return None
        cur_id = 0
        curNode = self.superior
        while True:
            if cur_id == index: return curNode.dato
            curNode = curNode.siguiente
            cur_id += 1
    def actualizar(self,index,valor):
        if index >= self.size:
            return None
        cur_id = 0
        curNode = self.superior
        while True:
            if cur_id == index: 
                curNode.dato= valor 
                return
            curNode = curNode.siguiente
            cur_id += 1
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
    def get(self,index):
        if index >= self.size:
            return None
        cur_id = 0
        curNode = self.First
        while True:
            if cur_id == index: return curNode.Value
            curNode = curNode.next
            cur_id += 1
    def actualizar(self,index,valor):
        if index >= self.size:
            return None
        cur_id = 0
        curNode = self.First
        while True:
            if cur_id == index: 
                curNode.Value= valor 
                return
            curNode = curNode.next
            cur_id += 1
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
class HashTable:  
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX  
    
    def __getitem__(self, key):
        arr_index = self.get_hash(key)
        for kv in self.arr[arr_index]:
            if kv[0] == key:
                return kv[1]
            
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0] == key:
                self.arr[h][idx] = (key,val)
                found = True
        if not found:
            self.arr[h].append((key,val))
        
    def __delitem__(self, key):
        arr_index = self.get_hash(key)
        for index, kv in enumerate(self.arr[arr_index]):
            if kv[0] == key:
                print("del",index)
                del self.arr[arr_index][index]