print("Olá, tudo bem? aqui avaliamos o consumo de água da sua residência")
## Inicialmente pedimos o tipo de residencia
residencia = input("Diga o nome da sua residência: ")
## Em seguida pedimos o consumo de água em metros cúbicos
consumo = float(input("Digite o consumo de água em metros cúbicos (m³): "))

if residencia.lower() == "comercial": ## aqui aplicamos a unica tarifa comercial
 print("Tarifa comercial aplicada – consulte o plano corporativo.")

if residencia.lower() == "apartamento": ## aqui aplicamos a tarifa de apartamento
    if consumo <= 10: ## caso o consumo seja menor ou igual a 10 metros cúbicos
        print("Consumo econômico – excelente controle de água!")
    elif consumo <= 25: ## caso o consumo seja menor ou igual a 25 metros cúbicos
        print("Consumo moderado – dentro do padrão residencial.")
    else: ## caso o consumo seja maior que 25 metros cúbicos
        print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")

if residencia.lower() == "residencial": ## aqui aplicamos a tarifa residencial
   if consumo <= 25: ## caso o consumo seja menor ou igual a 25 metros cúbicos
        print("Consumo moderado – dentro do padrão residencial.") 
   else: ## caso o consumo seja maior que 25 metros cúbicos
        print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")