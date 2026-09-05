print("Olá, tudo bem?")

aparelho = input("Digite o nome do aparelho: ")

potencia = float(input(f"Digite a potência do {aparelho} em Watts (W): "))

horasDia = float(input(f"Digite quantas horas por dia o {aparelho} é utilizado: "))

while potencia < 0 or horasDia < 0:
    print("Valor inválido. Por favor, digite valores positivos.")

    potencia = float(input(f"Digite a potência do {aparelho} em Watts (W): "))
    horasDia = float(input(f"Digite quantas horas por dia o {aparelho} é utilizado: "))

while  horasDia>24:
    print("Seu dia tem mais que 24 horas?")

    horasDia = float(input(f"Digite quantas horas por dia o {aparelho} é utilizado: "))

consumoMensal = (potencia * horasDia * 30) / 1000

preco = consumoMensal * 0.75

print(f"\nAparelho: {aparelho}")
print(f"Consumo estimado: {consumoMensal:.2f} kWh/mês")
print(f"Custo estimado: R$ {preco:.2f} por mês")