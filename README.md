*CODIGO NO FINAL DA EXPLICAÇÃO*
# Calculadora-atualizada-Python
Criei essa calculadora básica, com operações matemáticas básicas como adição, subtração, multiplicação e divisão. foi feita melhoria dela para que, possa calcula porcentagem.

Projeto prático de uma calculadora interativa em linha de comando (CLI) desenvolvida em Python. O projeto foi construído com foco em boas práticas de programação, modularização de código e tratamento defensivo de erros.

---

## 🚀 Funcionalidades

- ➕ **Adição (`+`):** Soma dois valores numéricos.
- ➖ **Subtração (`-`):** Calcula a diferença entre dois números.
- ✖️ **Multiplicação (`*`):** Realiza o produto entre dois números.
- ➗ **Divisão (`/`):** Divide dois números com validação contra divisão por zero (evitando falhas matemáticas).
- 📊 **Porcentagem (`%`):** Calcula uma porcentagem sobre um valor base (ex: 20% de 150 = 30).
- 🛡️ **Tratamento de Entradas Inválidas:** Captura erros caso o usuário digite letras ou símbolos onde são esperados números.
- 🔄 **Menu Interativo com Loop:** Permite realizar múltiplos cálculos consecutivos sem precisar reiniciar o programa.

---

## 🛠️ Tecnologias e Conceitos Utilizados

- **Linguagem:** Python 3
- **Funções (`def`):** Modularização da lógica matemática em funções independentes e reutilizáveis (`somar`, `subtrair`, `multiplicar`, `dividir`, `porcentagem`).
- **Estruturas de Repetição (`while`):** Laço `while True` para manter a aplicação em execução contínua até o usuário optar por sair.
- **Estruturas Condicionais (`if`, `elif`, `else`):** Controle de fluxo baseado na escolha do menu e validação de regras de negócio.
- **Tratamento de Exceções (`try / except`):** Captura do erro `ValueError` para impedir que o sistema trave ao receber entradas não numéricas.
- **Entrada e Saída de Dados:** Uso de `input()` para captura e `print()` com interpolação de strings (*f-strings*) para exibição formatada.
- **Métodos de String:** Métodos utilitários como `.strip()` (remoção de espaços) e `.lower()` (conversão para minúsculas).
- **Tipagem Dinâmica e Conversão:** Conversão explícita de tipos usando `float()`.

---

## 📂 Estrutura de Arquivos

```text
Calculadora basica em Python/
├── calculadora_completa.py   # Código-fonte principal com funções e loop interativo
└── README.md                 # Documentação do projeto
```

---

## ▶️ Como Executar

1. Certifique-se de ter o Python 3 instalado em seu computador.
2. Abra o terminal na pasta do projeto e execute:

```bash
python calculadora_completa.py
```
*(ou utilize o botão **Run / Executar** do seu editor de código favorito, como o VS Code).*
# ==========================================================
# CALCULADORA PYTHON PROFISSIONAL (LOOP + TRATAMENTO DE ERROS)
# ==========================================================


def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return None  # Indica erro de divisão por zero
    return a / b

def porcentagem(a, b):
    return (a * b) / 100

# Início do laço principal do programa
while True:
    print("\n" + "=" * 45)
    print("         CALCULADORA INTERATIVA")
    print("=" * 45)
    print("1 -> Adição (+)")
    print("2 -> Subtração (-)")
    print("3 -> Multiplicação (*)")
    print("4 -> Divisão (/)")
    print("5 -> Porcentagem (%)")
    print("0 -> Sair do programa")
    print("=" * 45)

    opcao = input("Escolha uma opção (0-5): ").strip()

    if opcao == "0":
        print("\nObrigado por usar a calculadora! Até logo! 👋")
        break  # Interrompe o laço while e encerra o programa

    if opcao not in ["1", "2", "3", "4", "5"]:
        print("\n❌ Opção inválida! Por favor, escolha entre 0 e 5.")
        continue  # Volta para o início do laço

    # Tratamento de erro com try/except para impedir travamentos caso digitem letras
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("\n❌ Erro: Por favor, digite apenas números válidos!")
        continue

    # Execução baseada na opção escolhida
    if opcao == "1":
        print(f"\n✅ Resultado: {num1} + {num2} = {somar(num1, num2)}")
    elif opcao == "2":
        print(f"\n✅ Resultado: {num1} - {num2} = {subtrair(num1, num2)}")
    elif opcao == "3":
        print(f"\n✅ Resultado: {num1} * {num2} = {multiplicar(num1, num2)}")
    elif opcao == "4":
        resp = dividir(num1, num2)
        if resp is None:
            print("\n❌ Erro: Não é possível dividir nenhum número por zero!")
        else:
            print(f"\n✅ Resultado: {num1} / {num2} = {resp}")
    elif opcao == "5":
        print(f"\n✅ Resultado: {num1}% de {num2} = {porcentagem(num1, num2)}")

    # Pergunta se quer continuar
    continuar = input("\nDeseja fazer outro cálculo? (s/n): ").strip().lower()
    if continuar != "s":
        print("\nObrigado por usar a calculadora! Encerrando... 👋")
        break

