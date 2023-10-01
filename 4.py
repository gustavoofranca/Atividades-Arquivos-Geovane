def calcular_media(notas):
    notas = [float(nota) for nota in notas.split()]
    return sum(notas) / len(notas)

def gerar_arquivo_medias(nome_alunos, nome_notas, nome_resultado):
    with open(nome_alunos, "r") as arquivo_alunos, open(nome_notas, "r") as arquivo_notas, open(nome_resultado, "w") as arquivo_resultado:
        for linha_aluno, linha_notas in zip(arquivo_alunos, arquivo_notas):
            nome_aluno = linha_aluno.strip()
            media = calcular_media(linha_notas)
            arquivo_resultado.write(f"{nome_aluno}: {media}\n")

gerar_arquivo_medias("alunos.txt", "notas.txt", "medias.txt")