"""
Escribe una funcion que tome una caracter y devuelva True si 
es una vocal de lo contrario devuelva false
"""
def Palabra(caracter):
    """
    dada una pablabra 

    Args:
    palabra: string

    Returns:
    bool:  devuelva verdadeo o falso si tiene vocal

    """
    lista_vocales=['a','e','i','o','u']

    if caracter in lista_vocales:
        return True
    else:
        return False

print(Palabra('u'))
