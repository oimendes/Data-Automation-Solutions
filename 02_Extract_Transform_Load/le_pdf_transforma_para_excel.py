import fitz
import re
import pandas as pd
import os

pasta_pdfs = r"./input_data/pdfs_originais"
lista_dados = []

def extrair_data(linhas, chave):
    for i, linha in enumerate(linhas):
        if chave in linha:
            for prox in linhas[i+1:i+6]:
                match = re.search(r"(\d{2}/\d{2}/\d{2,4})", prox)
                if match:
                    return match.group(1)
    return None

def extrair_awb(linhas):
    for i, linha in enumerate(linhas):
        if "AWB / BL No. / Ref. DHL" in linha:
            # Busca nas próximas 6 linhas após o cabeçalho
            for prox in linhas[i+1:i+7]:
                if re.match(r"[A-Z]{4,}[0-9]+", prox):
                    return prox
    # Busca alternativa: qualquer linha que seja um código alfanumérico com 8+ caracteres
    for linha in linhas:
        if re.match(r"[A-Z]{4,}[0-9]{4,}", linha):
            return linha
    return None

def extrair_origem(linhas):
    for i, linha in enumerate(linhas):
        if linha == "ORIGEM" and i + 1 < len(linhas):
            origem = linhas[i + 1]
            if re.match(r"[A-Z]{2}\s*-\s*[A-Z]+", origem):
                return origem
    for linha in linhas:
        if re.match(r"[A-Z]{2}\s*-\s*[A-Z]+", linha):
            return linha
    return None

def extrair_destino(linhas):
    for i, linha in enumerate(linhas):
        if linha == "DESTINO" and i + 1 < len(linhas):
            destino = linhas[i + 1]
            if re.match(r"BR\s*-\s*[A-Z]+", destino):
                return destino
    for linha in linhas:
        if re.match(r"BR\s*-\s*[A-Z]+", linha):
            return linha
    return None

def extrair_peso(linhas):
    # Busca o cabeçalho "PESO BRUTO" e pega o próximo valor numérico
    for i, linha in enumerate(linhas):
        if linha == "PESO BRUTO":
            # Busca nas próximas 5 linhas
            for prox in linhas[i+1:i+6]:
                if re.match(r"\d{4,}\.\d{2}", prox):
                    return prox
    # Busca alternativa: qualquer linha que seja um número grande com ponto
    for linha in linhas:
        if re.match(r"\d{4,}\.\d{2}", linha):
            return linha
    return None

for arquivo in os.listdir(pasta_pdfs):
    if arquivo.lower().endswith(".pdf"):
        caminho_pdf = os.path.join(pasta_pdfs, arquivo)
        texto = ""
        with fitz.open(caminho_pdf) as doc:
            for pagina in doc:
                texto += pagina.get_text() + "\n"
        linhas = [linha.strip() for linha in texto.splitlines() if linha.strip()]
        dados = {
            "Numero Nota Fiscal": None,
            "AWB / BL No": None,
            "PESO BRUTO": None,
            "ORIGEM": None,
            "DESTINO": None,
            "VALOR DO USD": None,
            "VR. LIQUIDO A PAGAR": None,
            "Data de Emissão": None,
            "Data de Vencimento": None
        }
        # Numero Nota Fiscal
        for i, linha in enumerate(linhas):
            if linha == "Número Nota Fiscal" and i + 1 < len(linhas):
                dados["Numero Nota Fiscal"] = linhas[i + 1]
        # Data de Emissão
        dados["Data de Emissão"] = extrair_data(linhas, "Data e Hora da Emissão")
        # Data de Vencimento
        dados["Data de Vencimento"] = extrair_data(linhas, "Data de Vencimento")
        # AWB / BL No
        dados["AWB / BL No"] = extrair_awb(linhas)
        # ORIGEM
        dados["ORIGEM"] = extrair_origem(linhas)
        # DESTINO
        dados["DESTINO"] = extrair_destino(linhas)
        # PESO BRUTO
        dados["PESO BRUTO"] = extrair_peso(linhas)
        # VALOR DO USD
        for linha in linhas:
            if "USD" in linha:
                match = re.search(r"(\d{1,3}[.,]\d{2})\s*USD", linha)
                if match:
                    dados["VALOR DO USD"] = match.group(1)
        # VR. LIQUIDO A PAGAR
        for linha in linhas:
            if "VR. LIQUIDO A PAGAR" in linha:
                match = re.search(r"([\d.,]+)$", linha)
                if match:
                    dados["VR. LIQUIDO A PAGAR"] = match.group(1)
        lista_dados.append(dados)

# Salvar em Excel
colunas_desejadas = [
    "Numero Nota Fiscal",
    "AWB / BL No",
    "PESO BRUTO",
    "ORIGEM",
    "DESTINO",
    "VALOR DO USD",
    "VR. LIQUIDO A PAGAR",
    "Data de Emissão",
    "Data de Vencimento"
]
df = pd.DataFrame(lista_dados)[colunas_desejadas]
df.to_excel("notas_fiscais_extraidas.xlsx", index=False)
print("Arquivo Excel 'notas_fiscais_extraidas.xlsx' gerado com sucesso!")