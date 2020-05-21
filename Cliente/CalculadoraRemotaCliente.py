import sys
import glob
sys.path.append('gen-py')
from CalculadoraRemota import CalculadoraRemotaServicio

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

transporte = TSocket.TSocket('localhost', 8080)
transporte = TTransport.TBufferedTransport(transporte)
protocolo = TBinaryProtocol.TBinaryProtocol(transporte)

cliente = CalculadoraRemotaServicio.Client(protocolo)

transporte.open()

def Menu():
    print("------------")
print("Calculadora")
print("------------")
print("Menu")
print("1) Adición")
print("2) Substracción")
print("3) Multiplicacion")
print("4) Division")
print("5) Salir")

def Calculadora():
    Menu()
    opc = int(input("Seleccione una opcion\n"))

    if opc <= 0 or opc > 5: 
        print("------------")
        print("¡Seleccione una opción valida, compañero!")
        print("------------")
        Calculadora()

    while (opc > 0 and opc < 5):
        enteroA = int(input("Ingrese un numero entero\n"))
        enteroB = int(input("Ingrese un otro numero entero\n"))
        if (opc == 1):
            print ("[Cliente] Resultado:", cliente.RealizarAdicion(enteroA, enteroB).resultadoOperacion)
            print ("------------")
            opc = int(input("Seleccione una opcion\n"))
            print("------------")
        elif(opc == 2):
            print ("[Cliente] Resultado: ", cliente.RealizarSubstraccion(enteroA, enteroB).resultadoOperacion)
            print ("------------")
            opc = int(input("Seleccione una opcion\n"))
            print ("------------")
        elif(opc == 3):
            print ("[Cliente] Resultado: ", cliente.RealizarMultiplicacion(enteroA, enteroB).resultadoOperacion)
            print ("------------")
            opc = int(input("Seleccione una opcion\n"))
            print ("------------")
        elif(opc == 4):
            if (enteroB == 0):
                print ("[Cliente] Resultado: ", cliente.RealizarDivision(enteroA, enteroB).mensaje)
                print ("------------")
                opc = int(input("Seleccione una opcion\n"))
                print ("------------")
            elif(enteroB != 0):
                print ("[Cliente] Resultado: ", cliente.RealizarDivision(enteroA, enteroB).resultadoOperacion)
                print ("------------")
                opc = int(input("Seleccione una opcion\n"))
                print ("------------")
    if opc == 5:
        print ("------------")
        print("[Cliente] Ayoch")

Calculadora()