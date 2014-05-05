from pyswip import *
from code import *
p=Prolog()

def agregarRestaurante(nombre, tipo, ubicacion, telefono):
    p = open("base.pl","a")
    p.write("restaurantes("+nombre+","+tipo+","+ubicacion+","+telefono+").\n")
    p.close()

def agregarPlatillo(restaurante,platillo,tipo,pais,ingredientes):
    p = open("base.pl","a")
    p.write("platillos("+restaurante+","+platillo+","+pais+","+ingredientes+").\n")
    p.close()

def verRestaurantes():
    p.consult("base.pl")
    resultados=[]
    for i in p.query("restaurantes(A,_,_,_)"):
        resultados.append(str(i["A"]))
    return resultados

def consulta():
    verRestaurantes()
