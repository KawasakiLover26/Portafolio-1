#Función: realizar una division sin usar un operador de division
#Entradas: un número que sera el divisor y otro que sera el dividendo
#Salidas: la division entre los numeros ingresados
#Restricciónes: deben ser numeros enteros positivos, el divisor no puede ser cero
def divisionRecursivo(divisor, dividendo):
    if(isinstance(divisor,int) and (isinstance(dividendo,int))):
        if(divisor==0):
            return print("ERROR: el divisor no puede ser cero")
        elif(divisor>0):
            return divisionRecursivo_aux(divisor, dividendo, 1)
        

def divisionRecursivo_aux(divisor, dividendo, Res):
    Multi = divisor * Res
    if(dividendo==Multi):
        return Res
    else:
        return divisionRecursivo_aux(divisor, dividendo, Res + 1)
        
   
        

    
    
