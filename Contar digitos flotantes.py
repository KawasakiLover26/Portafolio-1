"""
Función: Pasar un número con decimal a entero
Entradas: Un número con decimal
Salidas: un número entero
Restricciónes: El número ingresado debe ser flotante y mayor a cero
"""
def CorrimientoAEntero(num):
        Num = num * 10000
        Num = int(Num)

        return CorrimientoAEntero_aux(Num)


def CorrimientoAEntero_aux(num2):
    if(num2 == 0):
        return 0
    elif(num2%10)%2 == 0:
        return CorrimientoAEntero_aux(num2//10)
    else:
        return num2 + CorrimientoAEntero_aux(num2%10//10)


#Función: Contar todos los digitos de un numero sin importar si es flotante, negaivo o positivo
#Entradas: Un número
#Salidas: cantidad de digitos del numero 
#Restricciónes: num no puede ser str

def contarDigitosFlotantes(num):
    if(isinstance(num,str)):
         return ("Error: el numero no puede ser str")
    else:
         return canntidadDedigitos(CorrimientoAEntero(num))
      
def canntidadDedigitos(num):
       Num = num
       Num = int(Num)
       if(10 > num):
            return 1
       elif(num // 10) >= 0:
           return 1+canntidadDedigitos(num//10)
       else:
           return num
        
 
    
         
