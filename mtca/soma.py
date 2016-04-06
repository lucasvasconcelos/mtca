"""
Classe que implementa uma soma entre dois numeros ou duas strings

e.g.
Soma(5, 6)
11
"""
import json


class Soma(object):

    """
    Soma dois numeros/strings passados como argumento
    Estou colocando essa linha aqui so para dar mais que 80 caracteres olha isso aqui pqp
    """

    def __new__(self, num1, num2):
        """Faz a soma retorna o resultado"""
        return num1 + num2
