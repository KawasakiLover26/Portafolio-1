#Función: Multiplicar dos numeros sin usar el signo de multiplicación
#Entradas: dos numeros que serviran como factores de la multiplicación
#Salidas: El valor resultante de la multiplicación
#Restriciones


def MultiplicarRecursivo(num, factor):
    if(isinstance(num,int) and (isinstance(factor,int))):
        if(factor==0):
            return 0
        elif(factor>0):
            return ((num+num)//2) + MultiplicarRecursivo(num, factor - 1)
