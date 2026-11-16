# imports internos
from cli_calculator.src.utils.user_input import solicitar_numero, solicitar_operador

# imports externos
from unittest import TestCase
from unittest.mock import patch

class TestInputs(TestCase):
    """Testes direcionados as entradas de dados do usuário"""

    @patch('builtins.input')
    def test_solicitar_numero_sucesso_direto(self, mock_input):
        mock_input.return_value = '5.5'

        resultado = solicitar_numero()
        self.assertEqual(resultado, 5.5)

    @patch('cli_calculator.src.utils.user_input.alertar')
    @patch('builtins.input')
    def test_solicitar_numero_com_erro_antes_do_sucesso(self, mock_input, mock_alertar):
        mock_input.side_effect = ['texto_invalido', '10.2']

        resultado = solicitar_numero()

        self.assertEqual(resultado, 10.2)
        mock_alertar.assert_called_once()

    @patch('builtins.input')
    def test_solicitar_operador_sucesso(self, mock_input):
        mock_input.return_value = '2'

        resultado = solicitar_operador(opcoes=[1, 2, 3])
        self.assertEqual(resultado, 2)

    @patch('cli_calculator.src.utils.user_input.alertar')
    @patch('builtins.input')
    def test_solicitar_operador_fora_da_lista_e_letra(self, mock_input, mock_alertar):
        mock_input.side_effect = ['5', 'abc', '3']

        resultado = solicitar_operador(opcoes=[1, 2, 3, 4])

        self.assertEqual(resultado, 3)
        self.assertEqual(mock_alertar.call_count, 2)
