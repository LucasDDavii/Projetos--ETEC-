
# Calcula a média das notas de uma disciplina.
def calcular_media(notas):
    return sum(notas) / len(notas)


# Verifica a situação do aluno em uma disciplina.
def verificar_situacao(media):
    if media >= 6:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


# Verifica a situação final do aluno.
def verificar_aprovacao_final(disciplinas):
    recuperacao = False

    for disciplina in disciplinas:
        situacao = disciplinas[disciplina]["situacao"]

        if situacao == "Reprovado":
            return "Reprovado"
        elif situacao == "Recuperação":
            recuperacao = True

    if recuperacao:
        return "Recuperação"

    return "Aprovado"


# Gera um relatório com as médias e situações.
def gerar_relatorio(alunos):
    for matricula in alunos:
        aluno = alunos[matricula]

        print(f"\nAluno: {aluno['nome']}")

        for disciplina in aluno["disciplinas"]:
            dados = aluno["disciplinas"][disciplina]

            print(f"Disciplina: {disciplina}")
            print(f"Média: {dados['media']:.1f}")
            print(f"Situação: {dados['situacao']}")

        print(f"Situação final: {aluno['situacao_final']}")


# Cadastro de exemplo dos alunos.
alunos = {
    "2026001": {
        "nome": "João",
        "disciplinas": {
            "Matemática": {
                "notas": [7, 8, 6],
                "media": None,
                "situacao": None
            }
        }
    },
    "2026002": {
        "nome": "Maria",
        "disciplinas": {
            "Matemática": {
                "notas": [3, 7, 10],
                "media": None,
                "situacao": None
            }
        }
    }
}


# Calcula a média e a situação de cada disciplina.
for matricula in alunos:
    disciplinas = alunos[matricula]["disciplinas"]

    for disciplina in disciplinas:
        dados = disciplinas[disciplina]

        dados["media"] = calcular_media(dados["notas"])
        dados["situacao"] = verificar_situacao(dados["media"])


# Calcula a situação final de cada aluno.
for matricula in alunos:
    disciplinas = alunos[matricula]["disciplinas"]

    alunos[matricula]["situacao_final"] = (
        verificar_aprovacao_final(disciplinas)
    )


# Exibe o relatório final.
gerar_relatorio(alunos)