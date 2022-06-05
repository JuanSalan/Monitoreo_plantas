import Estructuras
from prueba import lectura
import time
from math import *
import random
start = time.time()
pilaContingencias=Estructuras.Pila()
lista = random.choices(range(1023), k=2000000)
lista2 =random.choices(range(1023), k=2000000)
lista3 = random.choices(range(1023), k=2000000)
lista4 =random.choices(range(1023), k=2000000)
lista5 = random.choices(range(1023), k=2000000)
dato1=[1,1,150,125,34,lista]
dato2=[2,1,152,122,35,lista2]
dato3=[3,1,158,119,37,lista3]
dato4=[4,1,159,119,37,lista4]
dato5=[5,1,160,117,36,lista5]
pilaContingencias=Estructuras.Pila()
Datos=[dato1,dato2,dato3,dato4,dato5]
lectura(Datos,pilaContingencias)
print("The time used to execute this is given below")
end = time.time()
print(end - start)