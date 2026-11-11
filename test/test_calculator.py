# imports internos
from cli_calculator.src.objects.calculadora import Calculadora

# imports externos
from unittest import TestCase


class TestCalculadora(TestCase):
    """Testes direcionados a classe Calculadora"""

    def test_soma(self):
        self.assertEqual(Calculadora._somar(2, 3), 5)
        self.assertEqual(Calculadora._somar(-1, 1), 0)
        self.assertEqual(Calculadora._somar(0, 1), 1)

    def test_subtracao(self):
        self.assertEqual(Calculadora._subtrair(5, 3), 2)
        self.assertEqual(Calculadora._subtrair(0, 0), 0)
        self.assertEqual(Calculadora._subtrair(-1, -1), 0)

    def test_multiplicacao(self):
        self.assertEqual(Calculadora._multiplicar(4, 2), 8)
        self.assertEqual(Calculadora._multiplicar(-1, -1), 1)
        self.assertEqual(Calculadora._multiplicar(0, 10), 0)

    def test_divisao(self):
        self.assertEqual(Calculadora._dividir(6, 2), 3)
        self.assertEqual(Calculadora._dividir(0, 2), 0)
        self.assertEqual(Calculadora._dividir(10, -1), -10)

    def test_calcular_somar(self):
        self.assertEqual(Calculadora.calcular(1, 1, 1), 2)

    def test_calcular_operador_invalido(self):
        with self.assertRaises(ValueError) as erro:
            Calculadora.calcular(1, 0, 0)

        self.assertEqual(str(erro.exception), "Operador inválido, tente novamente...")

    def test_calcular_divisao_por_zero(self):
        with self.assertRaises(ZeroDivisionError) as erro:
            Calculadora.calcular(10, 0, 4)

        self.assertEqual(
            str(erro.exception), "Divisão por 0 não permitida, tente novamente..."
        )
