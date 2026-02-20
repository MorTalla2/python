"""
Docstring pour src.cotroller
ce fichier consiste a mettre en place des interactions entre le model et vue

"""

import model
import view

def run():
    while True:
        # affichage du menu
        print(view.menu())
        
        # Saisir l'operateur
        op = view.saisir_op().strip()
        if op not in "+,-,*,/":
            print("Bye")
            break
        # recuperation desvaleurs
        a = view.saisir_val("a")
        b = view.saisir_val("b")

        if op == "+":
            res = model.add(a , b)

        elif op == "-":
            res = model.supp(a , b)

        elif op == "/":
            res = model.div(a , b)
    
        elif op == "*":
            res = model.mult(a , b)
        
        print()

        # Afficher le resultat
        view.affiche_resultats(res)
        print("-"*100)
        print()

if __name__ == "__main__":
    run()
