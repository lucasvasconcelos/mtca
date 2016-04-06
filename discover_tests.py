"""Procura testes e executa todos"""
import unittest
import xmlrunner


def load_tests(loader=None, standard_tests=None, pattern=None):
    """Faz discovery dos testes no diretorio tests"""
    return unittest.TestLoader().discover('tests')

if __name__ == '__main__':
    xmlrunner.XMLTestRunner(output='reports').run(load_tests())
    # unittest.main()
