
import os

# Caminho da pasta com os PDFs
pasta = r"./input_data/pdfs_originais"

# Lista de notas que NÃO podem ser lançadas
notas_proibidas = [
    "2030353","2030354","2030357","2030427","2031698","2031702","2031713","2031716",
    "2034762","2034771","2034775","2034786","2034822","2034829","2034843","2034867",
    "2034907","2034912","2034928","2040011","2040012","2040014","2040028","2040039",
    "2040136","2040138","2040141","2040142","2040144","2040149","2040825","2040826",
    "2040829","2040830","2040831","2040832","2040833","2040834","2040835","2040855",
    "2045691","2045732","2045926","2046009","2046047","2046090","2047711","2049951",
    "2050161","2050205","2054668","2055254"
]

# Percorrer os arquivos da pasta
for arquivo in os.listdir(pasta):
    if arquivo.lower().endswith(".pdf"):
        # Verifica se algum número proibido está no nome do arquivo
        if any(nota in arquivo for nota in notas_proibidas):
            caminho_arquivo = os.path.join(pasta, arquivo)
            try:
                os.remove(caminho_arquivo)
                print(f"Arquivo removido: {arquivo}")
            except Exception as e:
                print(f"Erro ao remover {arquivo}: {e}")

print("Processo concluído! Arquivos proibidos foram excluídos.")
