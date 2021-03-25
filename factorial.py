"""
Nombre:
      Factorial

Entradas:
        n = un número entero

Salida:
      resultado = es la multiplicacion de los numeros desde n hasta 1

Restricciones:
             solo numeros enteros positivos
             Mayor a cero
             El factorial de 0 = a 1
"""

def factorial(n):
    if(isinstance(n,int)):
        if(0 > n):
            print ("el numero debe ser mayor a cero")
        elif(n==0):
            return 1
        else:
            return n*factorial(n-1)
       
        
              
       
       
