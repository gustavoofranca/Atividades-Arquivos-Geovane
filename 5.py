def alterar_nota_aluno(arquivo_notas, nome_aluno, nota_antiga, nova_nota):
    linhas = []
    with open(arquivo_notas, "r") as arquivo_leitura:
        for linha in arquivo_leitura:
            if nome_aluno in linha:
                linha = linha.replace(nota_antiga, nova_nota)
            linhas.append(linha)
    with open(arquivo_notas, "w") as arquivo_escrita:
        arquivo_escrita.writelines(linhas)

alterar_nota_aluno("notas.txt", "João", "7.5", "8.0")