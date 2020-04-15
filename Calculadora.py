import sys

from pip._vendor.distlib.compat import raw_input
def pedirNumeros():
   global primer_numero
   global segundo_numero
   primer_numero = int(input("Ingrese un Numero: "))
   segundo_numero = int(input("Ingrese otro Numero: "))
def Suma():
   suma = primer_numero + segundo_numero
   print("SUMA: ", suma)
def Resta():
   resta = primer_numero - segundo_numero
   print("RESTA: ", resta)
def Multiplicacion():
   multiplicacion = primer_numero * segundo_numero
   print("MULTIPLICACIÓN: ", multiplicacion)
def Division():
   if segundo_numero == 0:
      print("ERROR")
   else:
      division = primer_numero / segundo_numero
      print("DIVISIÓN", division)
def Salir():
   print("HASTA LUEGO!")
   sys.exit()

respuesta="si"
while respuesta!="no":
   print (''' 
CALCULADORA BASICA ----->
1) SUMAR
2) RESTAR
3) MULTIPLICAR
4) DIVIDIR
5) SALIR''')
   opcion=int(input("Ingrese el numero de su opcion: "))
   if opcion>0 and opcion<6:
      pedirNumeros()
      if opcion == 1:
         Suma()
      elif opcion == 2:
         Resta()
      elif opcion == 3:
         Multiplicacion()
      elif opcion == 4:
         Division()
      elif opcion == 5:
         Salir()
   respuesta=raw_input("Desea hacer otra operacion? [si/no]: ")