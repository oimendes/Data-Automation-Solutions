
import os
import PyPDF2

# Caminho da pasta com os PDFs
pasta = r'./input_data/pdfs_originais'

# Percorrer todos os arquivos da pasta
for arquivo in os.listdir(pasta):
    if arquivo.lower().endswith('.pdf'):
        caminho_pdf = os.path.join(pasta, arquivo)

        # Abrir o PDF atual
        with open(caminho_pdf, 'rb') as pdf_file:
            leitor = PyPDF2.PdfReader(pdf_file)
            escritor = PyPDF2.PdfWriter()

            # Verificar cada página
            for pagina in leitor.pages:
                texto = pagina.extract_text()
                if texto and "Número da NFS-e" in texto:
                    escritor.add_page(pagina)

            # Se encontrou páginas, salvar novo arquivo
            if len(escritor.pages) > 0:
                nome_saida = f"filtrado_{arquivo}"
                caminho_saida = os.path.join(pasta, nome_saida)
                with open(caminho_saida, 'wb') as novo_pdf:
                    escritor.write(novo_pdf)

print("Processo concluído! PDFs filtrados foram salvos na mesma pasta.")
