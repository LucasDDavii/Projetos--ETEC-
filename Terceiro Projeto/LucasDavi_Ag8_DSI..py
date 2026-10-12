import os

os.system('cls' if os.name == 'nt' else 'clear')
## inicialmente criamos as variaveis para contar a quantidade de entrevistados e os que deram avaliação excelente ou ruim
print('Olá! Bem-vindo ao sistema de avaliação de entrevistas. Hoje vamos entrevistar 50 candidatos')
e = 0
r = 0
i = 1
while i <= 50: ## aqui descolhi "while" para poder reiniciar a entrevista caso o usuário digite uma avaliação inválida
    name = input(f'entrevistado {i}, por favor, insira seu nome: ') ##pdemios o nome do entrevistado
    idade = input(f'{name}, por favor, agora avalie a sua idade: ') ## pedimos a idade do entrevistado
    avaliacao = input(f'{name}, por favor, agora avalie a nosso atendimento em:\n 1-Exelente\n 2-Bom\n 3-Ruim\n') ## pedimos sua avaliação
    if avaliacao == "exelente":
        e = e + 1
        i = i + 1
        ## aqui incrementamos a quantidade de entrevistados que deram avaliação excelente e a quantidade de entrevistados
    elif avaliacao == "ruim":
        r = r + 1
        i = i + 1
        ## aqui incrementamos a quantidade de entrevistados que deram avaliação ruim e a quantidade de entrevistados
    elif avaliacao == "bom":
        i = i + 1
        ## aqui incrementamos a quantidade de entrevistados, somente, pois a avaliação "bom" não é contabilizada
    else:
        print('Avaliação inválida. Por favor, insira "exelente", "bom" ou "ruim".')
        ## aqui caso o usuário digite uma avaliação inválida, ele será informado e a entrevista será reiniciada
        

## aqui exibimos a quantidade de entrevistados que deram avaliação excelente e ruim
print(f'Quantidade de entrevistados que deram avaliação excelente: {e}')
print(f'Quantidade de entrevistados que deram avaliação ruim: {r}')