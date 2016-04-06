"""
Classe que implementa uma multiplicacao entre dois numeros

e.g.
Multiplica(2, 6)
12
"""


class Multiplica(object):

    """Multiplica dois numeros passados como argumento"""

    def __new__(self, num1, num2):
        """Faz a multiplicacao e retorna o resultado"""
        return num1 * num2
