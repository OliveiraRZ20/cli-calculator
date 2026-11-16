# imports internos
from cli_calculator.src.utils.logger import alertar

# imports externos


def solicitar_numero() -> float:
    """Lê um número float do usuário, exibindo o prompt fornecido."""
    while True:
        try:
            valor: float = float(input("Digite um número:\n> ").replace(",", "."))
            return valor
        except ValueError:
            alertar("Entrada inválida. Por favor, digite um número válido.")


def solicitar_operador(opcoes: list[int]) -> int:
    """Lê uma opção do usuário dentre as opções fornecidas."""
    while True:
        try:
            valor: int = int(input("Escolha a operação desejada:\n> "))
            if valor in opcoes:
                return valor
            else:
                alertar(f"Opção inválida. Por favor, escolha entre {opcoes}.")
        except ValueError:
            alertar("Entrada inválida. Por favor, digite um número válido.")
