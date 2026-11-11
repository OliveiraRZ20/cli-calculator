# imports internos
from cli_calculator.src.objects.calculadora import Calculadora
from cli_calculator.src.utils.logger import alertar
from cli_calculator.src.utils.terminal import cls, pause, encerrar
from cli_calculator.src.utils.user_input import ler_float, ler_opcao

# imports externos

MENU_STR: str = """
+------------------------------------------------+
|      Bem-vindo à Calculadora no Terminal!      |
+------------------------------------------------+
| Operações disponíveis:                         |
| 01. Soma                                       |
| 02. Subtração                                  |
| 03. Multiplicação                              |
| 04. Divisão                                    |
+------------------------------------------------+
| 00. Sair                                       |
+------------------------------------------------+
"""


def main():
    cls()
    print(MENU_STR)
    operador: int = ler_opcao(
        "Digite o número da operação desejada (1-4):\n> ", opcoes=[0, 1, 2, 3, 4]
    )
    if operador == 0:
        encerrar()
    a: float = ler_float("Digite o primeiro número:\n> ")
    b: float = ler_float("Digite o segundo número:\n> ")
    try:
        resultado = Calculadora.calcular(a, b, operador)
        print(f"Resultado: {resultado:g}")
    except Exception as error:
        alertar(str(error))


if __name__ == "__main__":
    try:
        while True:
            main()
            pause()
    except KeyboardInterrupt:
        encerrar()
