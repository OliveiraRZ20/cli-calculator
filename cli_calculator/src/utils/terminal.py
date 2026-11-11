# imports internos
from cli_calculator.src.utils.logger import confirmar

# imports externos
from os import name
from subprocess import run
from sys import exit

def cls():
    """Limpa o terminal (adaptado para qualquer OS)"""
    run('cls' if name == 'nt' else 'clear', shell=True)

def pause():
    """Pausa a execução do programa até o usuário pressionar 'Enter'."""
    input("Pressione Enter para continuar...")

def encerrar():
    """Finaliza o programa com uma mensagem diferente controlada pelo `exit_code`"""
    confirmar("Programa finalizado com sucesso!")
    exit(0)
