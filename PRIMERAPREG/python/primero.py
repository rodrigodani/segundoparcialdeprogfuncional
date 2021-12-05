# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 21:58:11 2021

@author: USUARIO
"""
def calculadora(a,b,op):
    if (op == "suma"):
        return suma(a,b)
    elif (op == "resta"):
        return resta(a,b)
    elif (op == "multiplicacion"):
        return mutilplicacion(a,b)
    else:
        return division(a,b)
def suma (a,b):
    return a+b    
    
def resta (a,b):
    return a-b    
def multiplicacion (a,b):
    return a*b    
def division (a,b):
    return a/b        
    
    
def main():
    print ("calculadora")
    print ("Ingrese primer numero")
    a = input ()
    print ("Ingrese otro numero")
    b = input ()
    print ("Ingrese la operacion que desea realizar")
    op = input ()
    print(calculadora(int(a),int(b),op))
main()



    
    
