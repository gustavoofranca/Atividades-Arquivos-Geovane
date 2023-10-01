import random

# Listas de nomes e sobrenomes
nomes = ["Ana", "João", "Maria", "Pedro", "Luísa", "Rafael", "Lara", "Carlos", "Eva", "Lucas",
         "Lívia", "Bruno", "Juliana", "Rodrigo", "Mariana", "Fernando", "Camila", "Daniel", "Patrícia"]
sobrenomes = ["Silva", "Santos", "Oliveira", "Pereira", "Ferreira", "Rodrigues", "Almeida", "Lima", "Souza", "Costa",
              "Carvalho", "Gonçalves", "Ribeiro", "Araújo", "Martins", "Cavalcanti", "Freitas", "Correia", "Vieira"]

def gera_dados_aleatorios(N):
    with open("dados_pessoais.txt", "w") as arquivo:
        for _ in range(N):
            nome_completo = f"{random.choice(nomes)} {random.choice(sobrenomes)}"
            idade = random.randint(18, 60)
            altura = round(random.uniform(1.50, 2.00), 2)
            arquivo.write(f"{nome_completo}, {idade} anos, {altura} m\n")

N = int(input("Digite o número de registros a serem gerados: "))
gera_dados_aleatorios(N)


def escreverNumerosAleatorios(qtdNumeros, nomeArquivo):
    arquivoNumeros = open(nomeArquivo, 'w')
    for i in range(qtdNumeros):
        nome_completo = f"{random.choice(nomes)} {random.choice(sobrenomes)}"
        idade = random.randint(18, 60)
        altura = round(random.uniform(1.50, 2.00), 2)
        arquivoNumeros.write(f"{nome_completo}, {idade} anos, {altura} m\n")
    arquivoNumeros.close()

escreverNumerosAleatorios(100, 'cadastro.txt')