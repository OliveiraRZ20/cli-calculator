# CLI Calculator

Uma calculadora simples, direta e sem distrações para quem gosta de resolver
contas pelo terminal. O projeto nasceu como um exercício prático em Python,
mas já conta com uma experiência de uso organizada: menu interativo, mensagens
coloridas, validação de entradas e tratamento explícito de divisão por zero.

## O que ela faz

- Soma, subtração, multiplicação e divisão.
- Aceita números decimais.
- Repete a operação até o usuário escolher sair.
- Informa entradas inválidas sem interromper o programa.
- Impede divisão por zero.
- Possui testes unitários para a lógica de cálculo e leitura de dados.

## Como executar

Com o Python instalado, na raiz do projeto:

```bash
python -m cli_calculator
```

O programa exibirá um menu no terminal. Escolha uma operação, informe os dois
números e confira o resultado.

## Como testar

```bash
python -m unittest discover -s test -v
```

## Estrutura

```text
cli_calculator/
├── __main__.py              # Interface e fluxo principal da aplicação
└── src/
    ├── objects/
    │   └── calculadora.py   # Operações matemáticas
    └── utils/
        ├── logger.py        # Mensagens no terminal
        ├── terminal.py      # Limpeza, pausa e encerramento
        └── user_input.py    # Leitura e validação das entradas
test/                        # Testes automatizados
```

## Tecnologias

- Python
- `unittest`
- Terminal

## Licença

Este projeto está disponível sob a [licença MIT](./LICENSE).

Confira o [changelog](./changelog.md) para acompanhar as alterações do projeto.
