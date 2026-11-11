# imports internos
from cli_calculator.src.utils.logger import alertar

# imports externos


def ler_float(prompt: str) -> float:
    """Lê um número float do usuário, exibindo o prompt fornecido."""
    while True:
        try:
            valor: float = float(input(prompt))
            return valor
        except ValueError:
            alertar("Entrada inválida. Por favor, digite um número válido.")


def ler_opcao(prompt: str, opcoes: list) -> int:
    """Lê uma opção do usuário dentre as opções fornecidas."""
    while True:
        try:
            valor: int = int(input(prompt))
            if valor in opcoes:
                return valor
            else:
                alertar(f"Opção inválida. Por favor, escolha entre {opcoes}.")
        except ValueError:
            alertar("Entrada inválida. Por favor, digite um número válido.")
