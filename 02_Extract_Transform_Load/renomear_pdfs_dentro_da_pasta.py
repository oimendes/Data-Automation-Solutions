import os

# Caminho da pasta com as imagens
pasta = r"./input_data/pdfs_originais"

# Iterar sobre os arquivos na pasta
for arquivo in os.listdir(pasta):
    nome, extensao = os.path.splitext(arquivo)
    novo_nome = nome.replace("NF_", "").replace(".", "_") + extensao
    os.rename(os.path.join(pasta, arquivo), os.path.join(pasta, novo_nome))

print("Arquivos renomeados com sucesso.")
