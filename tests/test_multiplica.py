"""Testa a classe multiplica"""
import unittest
from mtca.multiplica import Multiplica


class MultiplicaTestCase(unittest.TestCase):

    """Testes de unidade da classe Multiplica"""

    def test_multiplica_positivo(self):
        """Faz um teste com numeros positivos"""
        result = Multiplica(2, 50)
        self.assertEqual(100, result)

    def test_multiplica_negativo_positivo(self):
        """Faz um teste com numeros negativos e positivos"""
        result = Multiplica(10, -4)
        self.assertEqual(-40, result)

    def test_multiplica_negativo_negativo(self):
        """Faz um teste com numeros negativos"""
        result = Multiplica(-2, -8)
        self.assertEqual(16, result)

    def test_multiplica_string(self):
        """
        Testa multiplicacao de strings
        Deve-se receber um TypeError
        """
        with self.assertRaises(TypeError):
            Multiplica('a', 'b')

    def test_multiplica_string_numero(self):
        """Testa multiplicacao de str por um numero inteiro"""
        result = Multiplica('a', 5)
        self.assertEqual('aaaaa', result)

    def test_para_falhar(self):
        self.assertEqual(True, False)
