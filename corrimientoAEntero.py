"""
Función: Pasar un número con decimal a entero
Entradas: Un número con decimal
Salidas: un número entero
Restricciónes: El número ingresado debe ser flotante y mayor a cero
"""

def CorrimientoAEntero(num):
    if (isinstance(num,float) and num > 0):
        Num = num * 1000000000000000
        Num = int(Num)

        return CorrimientoAEntero_aux(Num)
    else:
        return ("Digite un número con decimales que sea mayor a 0")


def CorrimientoAEntero_aux(num2):
    if(num2 == 0):
        return 0
    elif(num2%10)%2 == 0:
        return CorrimientoAEntero_aux(num2//10)
    else:
        return num2 + CorrimientoAEntero_aux(num2%10//10)
         
