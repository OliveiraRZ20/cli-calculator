# Changelog

Todas as mudanças relevantes deste projeto serão registradas neste arquivo.

## [1.0.1] - 2026-11-15

## Modificado

1. Alterao nome da função de `ler_float()` para `solicitar_numero()` e `ler_opcao()` para `solicitar_operador()`
2. Retira a funcionalidade de especificar a mensagem do `input()` nas funções `solicitar_numero()` e `solicitar_operador()` e substitui para um texto fixo definido na função
3. Altera o `__main__.py` para contemplar as alterações realizadas em `user_input.py`
4. Altera o `test_user_input.py` para contemplar as alterações realizadas em `user_input.py`

## [1.0.0] - 2026-11-10

### Adicionado

- Licença MIT para definir os termos de uso, modificação e distribuição.
- README com a descrição do projeto, instruções de execução, testes e
  organização dos arquivos.
- Calculadora de terminal com operações de soma, subtração, multiplicação e
  divisão.
- Validação de números e opções do menu.
- Tratamento de divisão por zero e mensagens coloridas no terminal.
- Testes unitários para os cálculos e para a leitura de entradas.
