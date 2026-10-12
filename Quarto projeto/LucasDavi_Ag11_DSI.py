
from colorama import Fore, Style, init ## icluindo a biblioteca colorama para colorir o texto no terminal

init(autoreset=True)## resetando a cor do texto após cada loop

niveis = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)"
]## lista com os níveis do reservatório de água, do mais crítico ao mais alto.


def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE
    ## função que define a cor do texto com base no nível

print("Bem-vindo ao monitoramento do reservatório de água")
nivel_atual = int(input("Informe o nível do reservatório (1 a 5): "))## pedindo ao usuário para informar o nível de água

if 1 <= nivel_atual <= 5: ## padronizando o nível de água para que seja entre 1 e 5
    situacao = niveis[nivel_atual - 1] ## obtendo a situação correspondente ao nível informado, usando "-1" pois a lista começa do índice 0
    cor = definir_cor(nivel_atual) ## definindo a cor do texto 

    print(cor + f"Nível {nivel_atual}: {situacao}" + Style.RESET_ALL) ## resultado
else:
    print("Nível inválido! Informe um valor entre 1 e 5.") ## caso seja um valor invalido
