import sys
import os

sys.path.insert(0, "/Users/mortallaniang/Documents/l2dsdb/Flask/My_projet/projet_calculatrice")



from src.model import add , supp , div, mult

def test_add():
    assert add(1, 2) == 3
    

def test_supp():
    assert supp(10 ,4) == 6

def test_div():
    assert div(4 ,2) == 2

def test_mult():
    assert mult(2,2) == 4

    