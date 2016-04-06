"""Testando a classe Soma"""
import unittest
from mtca.soma import Soma


class SomaTestCase(unittest.TestCase):

    """Testes de unidade da classe soma"""

    def test_soma_positiva(self):
        """Testa uma soma positiva"""
        result = Soma(10, 10)
        self.assertEqual(20, result)

    def test_soma_negativa(self):
        """Testa uma soma negativa"""
        result = Soma(5, -15)
        self.assertEqual(-10, result)

    def test_soma_string(self):
        """Testa uma soma com strings"""
        result = Soma('ab', 'cd')
        self.assertEqual('abcd', result)

    def test_tipos_diferentes(self):
        """
        Testa uma soma com 2 tipos diferentes
        Deve-se receber uma excecao TypeError
        """
        with self.assertRaises(TypeError):
            Soma('a', 1)
