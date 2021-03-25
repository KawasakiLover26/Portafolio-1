def cantidadDedigitos(num):
    if(isinstance(num,int) and num>=0):
        if(10>num):
            return 1
        elif(num//10) >= 0:
            return 1+cantidadDedigitos(num//10)
        else:
            return num
        
    else:
        return ("digite un numero positivo")


#Función: devuelve el numero al revés
#Entradas: un numero
#Salidas: el numero al réves
#Restricciones: el numero debe ser entero
def inversaNum(num):
    if isinstance(num, int):
        if (num>=10):
            if (num <=10):
                return num
            else:
                return inversaNum_aux(num, cantidadDedigitos(num))
        else:
            print("El número debe ser positivo")
            
    else:
        print("Error: el numero no es entero")
        
def inversaNum_aux(num, largo):
    if largo == 0:
        return 0
    else:
        return (num % 10) * (10 ** (largo - 1)) + inversaNum_aux(num // 10, largo - 1)
