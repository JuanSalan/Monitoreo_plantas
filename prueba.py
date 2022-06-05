import Estructuras
from Estructuras import cola,Pila
#los datos de entrada tienen el siguiente orden:
# 1-Numero de la medicion el cual actuaria como un tipo de hora de la medicion 
# 2-Numero de huerta
# 3-temperatura general promedio 
# 4-Humedad del aire general promedio
# 5-luz promedio
# 6-Humedad de la tierra
# Por cada medicion se tiene que recibir un unico dato de : hora o numero representativo , temperatura , humedad
# Por cada medicion se tiene que recibir los datos de cada cuadrilla
# Es decir que cada cuadrilla se debe recicibir su humedad

#Si se hacen lecturas cada 10 min serian 144 lecturas en un dia
pilaContingencias=Pila()
def lectura(Datos,pilaContingencias):
    contador=1
    while contador<=5:
        if Datos[contador-1][0]!=contador:
            print("La ultima medicion requerida no a sido entregada")
        else:
            humedadcuadrillas=Datos[contador-1][5]
            if(compruebahumedad(humedadcuadrillas)==1):
                colaRegar=cola()
                colaRegar=creaColaRegar(Datos[contador-1][5],len(Datos[contador-1][5]))
                pilaContingencias.apilar(colaRegar)
            elif(compruebahumedad(humedadcuadrillas)!=1):
                colaRegar=cola()
                colaRegar=creaColaRegar(Datos[contador-1][5],len(Datos[contador-1][5]))
                pilaContingencias.apilar(colaRegar)
            temperatura=Datos[contador-1][2]
            if(comprueba_temperatura(temperatura,contador)):
                pilaContingencias.apilar("Temperatura")
            if(pilaContingencias.size!=0):
                Contingencia(pilaContingencias)
        contador+=1
            

def comprueba_temperatura(temperatura,contador):
    """
        La temperatura esperada depende de la hora de medicion 
        Primeramente se tendra en cuenta que no supere valores extremos
        los valores extremos seran considerados como 0 grados y 30 grados celcius
        Luego verificara que los valores esten entre los valores esperadose por cada hora
    """
    if(temperatura<0 or temperatura>300):
        return True
    else:
        #Entre las 6 de la tarde y las 6 de la mañana se espera que temperatura no baje de 5 grados
        if((contador<36 or contador>108) and temperatura<50):
            return True
        #Entre las 6am-9am y 3pm-6pm se espera que la temperatura no sea menor a 5 grados y que no sea mayor a 15 grados
        elif(((contador>=36 and contador<=54) or (contador>=90 and contador<=18)) and (temperatura<50 or temperatura>150)):
            return True
        elif((contador>54 and contador<90) and temperatura<250):
            return True
        return False
    
def compruebahumedad(Datos):
    i=0
    numeroDatos=len(Datos)
    suma=0
    while(i<numeroDatos):
        """
            Sacaremos el promedio de humedad de todas las mediciones de humedad del suelo 
            la cual nos permitira decidir si es necesario el proximo rriego 
            
            teniendo en cuenta que en la escala del sensor utilizado 1023 es 0 porciento humedo 
            y 0 es 100 porciento humedo
        """
        suma+=Datos[i]
        i+=1
    suma=suma/numeroDatos
    i=0   
    if(suma>972):
        return 0
    
    while(i<numeroDatos):
        """
            Ademas se verificara que ninguno de los valores se encuentre en valores extremos
            asumiremos que la humedad del suelo no debe sobrepasar un 30 porciento de humedad ni
            debe estar por debajo de un 5 porciento de la humedad , ademas para poder definir si
            la medicion de una cuadrilla es realmente un valor critico teine que estar desviado un 
            10 porciento del promedio aritmetico de todas las mediociones
        """
        if((Datos[i]>972 or Datos[i]<716) and (abs(Datos[i]-suma)>51)):
            return suma
        i+=1
    else : 
        return -1
def crearColaRegarParcial(Datos,numeroDatos,suma): 
    miCola = cola()
    arregloaux1=sorted(Datos)
    i=0
    while(i<numeroDatos and (abs(Datos[i]-suma)>51)):
        j=0
        while(j<numeroDatos):
            if(Datos[j]==arregloaux1[i]):
                miCola.encolar(j)
            j+=1
        i+=1
        
def creaColaRegar(Datos,numeroDatos):
    miCola = cola()
    arregloaux1=(Datos.sort())
    i=0
    while(i<numeroDatos):
        j=0
        while(j<numeroDatos):
            if(Datos[j]==arregloaux1[i]):
                miCola.encolar(j)
            j+=1
        i+=1
def Contingencia(pila):
    print(pila.desapilar())
