
import os
import fitz  # PyMuPDF
import re

# Caminho da pasta com os PDFs
pasta = r"./input_data/pdfs_originais"

# Nome do arquivo de saída consolidado
arquivo_saida = "NotasFiscais_Completo.txt"

# Lista para armazenar os resultados
resultados = []

# Expressão regular para capturar NFS-e e Data e Hora da Emissão
padrao = re.compile(r"NFS-e\s+(\d+).*?Data e Hora da Emissão\s+(\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2})", re.DOTALL)

# Percorrer todos os arquivos da pasta
for arquivo in os.listdir(pasta):
    if arquivo.lower().endswith(".pdf"):
        caminho_pdf = os.path.join(pasta, arquivo)

        # Abre o PDF atual
        with fitz.open(caminho_pdf) as doc:
            for pagina in doc:
                texto = pagina.get_text()
                encontrados = padrao.findall(texto)

                for nfs, datahora in encontrados:
                    resultados.append(f"{arquivo}\t{nfs}\t{datahora}")

# Salva os resultados no arquivo TXT
with open(arquivo_saida, "w", encoding="utf-8") as f:
    f.write("Arquivo\tNFS-e\tData e Hora de Emissão\n")
    for linha in resultados:
        f.write(f"{linha}\n")

print(f"Extração concluída! {len(resultados)} notas salvas em {arquivo_saida}.")
