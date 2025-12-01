
from pathlib import Path

# Caminho da pasta
pasta = Path("./input_data/pdfs_originais")

# Lista de NFs fornecida
lista_nfs = [
    747285, 747289, 743381, 743437, 744425, 743387, 743933, 744995, 747300, 748180,
    737389, 748092, 748077, 748084, 748096, 743944, 746289, 726435, 741352, 741367,
    741412, 742966, 737819, 735281, 729233, 715947, 730741, 727483, 730698, 732779,
    730717, 729239, 729229, 730735
]

# Listar arquivos PDF na pasta
arquivos = [f.name for f in pasta.glob("*.pdf")]

# Extrair números das NFs dos nomes dos arquivos
nfs_arquivos = []
for arquivo in arquivos:
    if arquivo.startswith("NFS-E_"):
        try:
            numero = int(arquivo.split("_")[1].split(".")[0])
            nfs_arquivos.append(numero)
        except ValueError:
            pass

# Descobrir quais NFs estão faltando
faltando = [nf for nf in lista_nfs if nf not in nfs_arquivos]
sobrando = [nf for nf in nfs_arquivos if nf not in lista_nfs]

print(f"Total na lista: {len(lista_nfs)}")
print(f"Total de arquivos PDF: {len(nfs_arquivos)}")
print("Notas faltando:", faltando)
print("Notas sobrando:", sobrando)
