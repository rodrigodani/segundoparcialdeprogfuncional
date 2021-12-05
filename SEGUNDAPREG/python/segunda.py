# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 23:57:09 2021

@author: USUARIO
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 23:20:22 2021

@author: USUARIO
"""

calculadora = lambda a, b, op: resta(a,b) if (op=="resta") else (suma(a,b) if (op=="suma") else (multiplicacion (a,b) if (op=="multi") else division (a,b)))
    
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
    print(calculadora(int(a),int(b),op))
main()



    
    
