# ⚙️ ETL & Data Quality: Ferramentas de Transformação de Dados Logísticos

Esta categoria agrupa scripts de **automação focados na qualidade e preparação de dados** (*ETL - Extract, Transform, Load*), essenciais para transformar documentos não estruturados (PDFs) em bases de dados limpas e prontas para uso em auditoria, análise ou outros processos.

---

## 1. Desafio de Negócio

* **Problema:** A área de transportes lida com um grande volume de documentos (Notas Fiscais, Conhecimentos de Embarque - CT-e, etc.) em formato PDF, que exigiam **conferência manual** demorada para garantir a integridade dos dados (Data de Emissão, Valores, etc.).
* **Requisito:** Criar ferramentas robustas e modulares para **automatizar a extração, comparação e manipulação** desses documentos, assegurando a **Data Quality** e reduzindo o tempo de preparação para análises e pagamentos.

## 2. Solução Técnica e Impacto

O conjunto de scripts demonstra proficiência em manipulação de arquivos e tratamento de strings complexas, utilizando bibliotecas Python como **Pandas**, **PyMuPDF (fitz)** e **Pathlib/OS**.

| Script | Funcionalidade Principal | Benefício de Negócio | Tecnologias |
| :--- | :--- | :--- | :--- |
| `le_pdf_transforma_para_excel.py` | Extrai campos específicos de **PDFs não estruturados** (NFs, NDs, CT-e) e consolida os dados em uma planilha Excel (ETL). | Transforma uma pilha de documentos em uma base de dados pronta para análise em segundos. | PyMuPDF (fitz), Pandas, RegEx |
| `compara_lista_e_informa_faltante.py` | Compara uma lista de números de NFs (do sistema) com os arquivos PDF existentes na pasta. | **Garante a integridade do processo:** Identifica rapidamente quais documentos estão faltando para evitar atrasos no pagamento e falhas na auditoria. | Pathlib, RegEx |
| `trazer_data_emissao_nf.py` | Extrai a **Data de Emissão** de NFs-e/CT-e de múltiplos PDFs e gera um arquivo consolidado (TXT ou CSV). | Permite uma **auditoria rápida** e agrupamento de documentos por data, um processo puramente manual antes da automação. | PyMuPDF (fitz), RegEx |
| `renomear_pdfs_dentro_da_pasta.py` | Padroniza e limpa nomes de arquivos PDF em massa (ex: remove prefixos indesejados). | **Organização e rastreabilidade:** Prepara os arquivos para sistemas legados ou para facilitar a busca manual. | os, Pathlib |
| *Outros (Exclusão/Extração Seletiva)* | Scripts como `excluir_pdfs_de_nfs.py` e `extrair_pdfs_especificos.py` oferecem filtros booleanos (sim/não) e extração seletiva de páginas. | **Agilidade e limpeza:** Permite trabalhar apenas com o subconjunto de dados necessário para a tarefa atual. | os, PyPDF2 |
