def copia_arquivo_sem_comentarios(origem, destino):
    with open(origem, "r") as arquivo_origem, open(destino, "w") as arquivo_destino:
        for linha in arquivo_origem:
            if not linha.strip().startswith("//"):
                arquivo_destino.write(linha)

copia_arquivo_sem_comentarios("arquivo_origem.txt", "arquivo_destino.txt")