class Calculadora:

    @staticmethod
    def _somar(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def _subtrair(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def _multiplicar(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def _dividir(a: float, b: float) -> float:
        return a / b

    @staticmethod
    def calcular(a: float, b: float, operador: int) -> float:
        if operador not in (1, 2, 3, 4):
            raise ValueError("Operador inválido, tente novamente...")
        elif operador == 4 and b == 0:
            raise ZeroDivisionError("Divisão por 0 não permitida, tente novamente...")
        else:
            match operador:
                case 1:
                    resultado: float = Calculadora._somar(a, b)
                case 2:
                    resultado: float = Calculadora._subtrair(a, b)
                case 3:
                    resultado: float = Calculadora._multiplicar(a, b)
                case 4:
                    resultado: float = Calculadora._dividir(a, b)
            return resultado
