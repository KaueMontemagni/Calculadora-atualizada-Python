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
