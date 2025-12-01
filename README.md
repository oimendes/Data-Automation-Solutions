# 🚀 Portfólio de Soluções de Automação e Data Analytics

**Camila Mendes** | Análise de Dados | Supply Chain Analytics | Power BI (DAX/Modelagem) | RPA | Automação de Processos | Python

Minha experiência em Supply Chain e Logística me permitiu identificar gargalos operacionais do dia a dia e desenvolver soluções de impacto financeiro e de produtividade, como os projetos de automação detalhados abaixo.

**Foco Principal:** Transformar dados não estruturados em *insights* acionáveis para otimização de custos e performance, usando código (Python) para a etapa de ETL (Extração, Transformação e Carga).

---

### Destaques do Portfólio

| Projeto Principal | Impacto de Negócio | Tecnologias Chave |
| :--- | :--- | :--- |
| **[1. Full RPA - Lançamento Fiscal Automatizado](#1-full-rpa---lançamento-fiscal-automatizado)** | **Redução de 25h/mês** de trabalho manual nos lançamentos de NFs direto no sistema. | Python (Selenium/Webdriver), OpenPyXL, Pandas |
| **[2. ETL & Data Quality Logística](#2-etl--data-quality-logística)** | Assegura a integridade de dados para auditoria e automatiza processos manuais para conter mais agilidade no dia a dia. | Python (Pathlib, Pandas, PyMuPDF) |
| **[3. Web Scraping & Monitoramento de Contêineres](#3-web-scraping--monitoramento-de-contêineres)** | Preenchimento da data de devolução do container vazio ao armador para ter controle de *demurrage* (sobrestadia) com monitoramento em tempo real a fim de evitar custos excessivos e rastreabilidade operacional. | Python (Playwright), OpenPyXL |

---

### 1. Full RPA - Lançamento Fiscal Automatizado

Scripts de automação completa para interagir com sistemas via navegador, lendo dados de uma planilha e realizando lançamentos e buscas.

* **Ver Código e Detalhes:** [Ver Pasta `01_Full_RPA_Fiscal`](./01_Full_RPA_Fiscal)

* **Scripts:** `lancar_nfs_navegador_google.py`, `lancar_nfs_navegador_edge.py`

### 2. ETL & Data Quality Logística

Ferramentas focadas em transformar documentos não estruturados (PDFs) em bases de dados limpas e prontas para análises.

* **Ver Código e Detalhes:** [Ver Pasta `02_ETL_Data_Prep`](./02_ETL_Data_Prep)

* **Scripts:** `le_pdf_transforma_para_excel.py`, `compara_lista_e_informa_faltante.py`, `extrair_pdfs_especificos.py`, `excluir_pdfs_de_nfs.py`, `renomear_pdfs_dentro_da_pasta.py`, `trazer_data_emissao_nf.py`

### 3. Web Scraping & Monitoramento de Contêineres

Bot de Web Scraping que acessa portais externos e rastreia o status de devolução de contêineres vazios, atualizando automaticamente planilhas de controle.

* **Ver Código e Detalhes:** [Ver Pasta `03_WebScraping_Monitoring`](./03_WebScraping_Monitoring)

* **Script:** `procurar_data_devolucao_vazio.py`
