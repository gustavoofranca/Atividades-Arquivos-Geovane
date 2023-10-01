def separar_enderecos_ip(arquivo_entrada, arquivo_validos, arquivo_invalidos):
    with open(arquivo_entrada, "r") as entrada, open(arquivo_validos, "w") as validos, open(arquivo_invalidos, "w") as invalidos:
        for linha in entrada:
            endereco = linha.strip().split(".")
            if len(endereco) == 4:
                octetos_validos = True
                for octeto in endereco:
                    if not (octeto.isdigit() and 0 <= int(octeto) <= 255):
                        octetos_validos = False
                        break
                if octetos_validos:
                    validos.write(linha)
                else:
                    invalidos.write(linha)
            else:
                invalidos.write(linha)

# Exemplo de uso
separar_enderecos_ip("enderecos.txt", "validos.txt", "invalidos.txt")