# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 23:20:22 2021

@author: USUARIO
"""

def calculadora(a, b, fun):
    return fun(a, b);
suma = lambda a, b:a+b        
resta = lambda a,b:a-b    
multiplicacion = lambda a,b:a*b    
division = lambda a,b:a/b        
 
def main():
    print ("calculadora")
    print ("Ingrese primer numero")
    a = input ()
    print ("Ingrese otro numero")
    b = input ()
    print ("Ingrese la operacion que desea realizar")
    op = input ()
    if (op == "suma"):
        print(calculadora(int(a),int(b),suma))
    elif (op == "resta"):
        print(calculadora(int(a),int(b),resta))
    elif (op == "multiplicacion"):
        print(calculadora(int(a),int(b),multiplicacion))
    else:
        print(calculadora(int(a),int(b),division))
main()



    
    
