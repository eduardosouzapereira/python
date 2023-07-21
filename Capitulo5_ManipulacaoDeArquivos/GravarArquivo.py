with open("teste.txt", "w") as arquivo:
    arquivo.write("Nunca foi tão fácil criar um arquivo.")

# Segundo bloco sobrescreve o arquivo
with open("teste.txt", "w") as arquivo:
    arquivo.write("Continuação do texto.")

# Parâmtro "a" não sobrescreve o arquivo
with open("teste.txt", "a") as arquivo:
    arquivo.write("Continuação do texto.")
