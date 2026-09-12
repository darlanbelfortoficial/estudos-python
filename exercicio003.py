while True:
    print("=====CALCULADORA=SIMPLES=====")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Sair")

    operador = int(input("Informe o operador por favor: "))

    if operador == 0:
        print("calculadora encerrada")
        break
    elif operador >= 5:
        print("Número inválido!")
        break

    num1 = int(input("Informe um número por favor: "))
    num2 = int(input("Informe outro número por favor: "))

    if operador == 1:
        print("Resultado: ",num1+num2)

    elif operador == 2:
        print("Resultado: ",num1-num2)
    elif operador == 3:
        print("Resultado: ",num1*num2)
    elif operador == 4:
        print("Resultado: ",num1/num2)
    print("Obrigado por usar nosso sistema ✅")
