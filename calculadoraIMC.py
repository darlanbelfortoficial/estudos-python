print("Calculadora de IMC  ")

numero1 = float(input("Digite seu peso em kg: "))
numero2 = float(input("Digite sua altura em metros: "))

imc = numero1 / (numero2 ** 2)  

if imc < 18.5:
    print("Você está abaixo do peso. Seu IMC é: {:.2f}".format(imc))
elif 18.5 <= imc < 24.9:
    print("Você está com peso normal. Seu IMC é: {:.2f}".format(imc))
elif 25 <= imc < 29.9:
    print("Você está com sobrepeso. Seu IMC é: {:.2f}".format(imc))
elif 30 <= imc < 34.9:
    print("Você está com obesidade grau 1. Seu IMC é: {:.2f}".format(imc))
elif 35 <= imc < 39.9:
    print("Você está com obesidade grau 2. Seu IMC é: {:.2f}".format(imc))
else:
    print("Você está com obesidade grau 3. Seu IMC é: {:.2f}".format(imc))

