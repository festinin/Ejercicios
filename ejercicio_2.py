"""
1. definir una funcion max de tres() que tome como 
argumento tres numeros y devuelva el mayor de ellos.
"""

def custon_max(n1: int, n2: int, n3:int) -> int:
    """
    Dado tres numeros de entrada retorna el maximo de ambos

    Args:
    n1 (int): Primer numero
    n2(int): segundo numero
    n3(int): tercero numero

    Returns:
    int: Mayor de ambos

    """

    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n3 and n2 > n1 : 
        return n2
    elif n3 > n2 and n3 > n1 : 
        return n3
    else:
        raise Exception("no cumple")

print(custon_max(1, 7, 3))