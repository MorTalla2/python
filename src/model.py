"""
Docstring pour src.model
Ce fichier contient la logique metier des operations de base

if __name__ === " __main__ " permet de debbugguer localement
"""

def add(a , b):
    return a + b

def supp(a, b):
    return a - b

def mult(a , b):
    return a * b

def div(a , b):
    return a / b

if __name__ == " __main__ ":
    print(add(2,5))
    print(supp(4 , 34))
    print(mult(4 ,6))
    print(div(234 ,7))