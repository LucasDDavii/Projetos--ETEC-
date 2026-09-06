## Inciamos pedindo ao usuàrio um valor total da compra
print("Olá, tudo bem?")
valor = float(input("Digite o preço total da compra: "))

## enqunto o valor for negatvo, o programa vai pedir para o usuário digitar um valor válido
while valor < 0:
    print("Desculpa, ainda não trabalhamos com valores negativos.")
    valor = float(input("Digite o preço total da compra: "))

## desconto de 5%
if valor < 200:
    valor_final = valor * 0.95
    print(f"O preço final com desconto de 5% é R${valor_final:.2f}")

## desconto de 10%
elif valor >= 200 and valor < 300:
    valor_final = valor * 0.90
    print(f"O preço final com desconto de 10% é R${valor_final:.2f}")

## desconto de 15%
else:
    valor_final = valor * 0.85
    print(f"O preço final com desconto de 15% é R${valor_final:.2f}")