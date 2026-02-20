"""
Docstring pour src.view

ce model contient la  vue de l'applicatiom(interface)

"""
def menu():
    print("====== MENU =======")
    print("1.  ADDITION ")
    print("2.  SOUSTRACTION ")
    print("3.  MULTIPLICATION ")
    print("4.  DIVISION")
    print("0.  Quiter ")


def saisir_op():
    return input("saisir operateur : ")


def saisir_val(label):
    float(input(f"Enter valeurs {label}: "))

if __name__ == "__main__":
    menu()
    op = saisir_op()
    print(op)

    a = saisir_val("a")
    print(a)

    b = saisir_val("b")
    print(b)


def affiche_resultats(res):
    print(f"Resultats : {res} ")