# 🚢 Web Scraping & Monitoramento de Contêineres (Transportes)

Este projeto utiliza técnicas de Web Scraping para automatizar o monitoramento de contêineres marítimos e rastrear a data de devolução do vazio, um processo crucial para evitar custos logísticos adicionais.

---

## 1. Desafio de Negócio

* **Problema:** A falta de controle sobre a devolução de contêineres vazios ao armador (após o descarregamento da carga) gera custos altos e inesperados com **Demurrage** (sobrestadia) ou multas. A verificação manual do status em diversos portais de rastreamento (VGM, Booking) não existia ou se existisse estava sendo feito de forma manual.
* **Requisito:** Implementar um sistema de monitoramento proativo que atualize automaticamente a data de devolução do contêiner vazio (`Empty to Shipper` ou similar) em uma planilha centralizada.

## 2. Solução Técnica

Desenvolvimento de um robô de Web Scraping robusto usando **Python** com a biblioteca **Playwright** (uma alternativa moderna e eficiente ao Selenium).

* **Tecnologia (Playwright):** O Playwright oferece melhor estabilidade e velocidade em ambientes modernos (Single Page Applications - SPAs), sendo ideal para portais de rastreamento que dependem de JavaScript.
* **Fluxo do Bot:**
    1.  Lê a lista de IDs de contêineres de uma planilha Excel (`../input_data/Controle Containers.xlsx`).
    2.  Navega até o portal de rastreamento (a URL da transportadora).
    3.  Insere o ID do contêiner e executa a busca.
    4.  Faz a raspagem (scraping) da página para encontrar a data de devolução e o status (`Empty to Shipper`).
    5.  Atualiza a planilha Excel na hora (usando `openpyxl`), salvando a data de devolução e o status.

## 3. Impacto e Resultado

* **Rastreabilidade Operacional:** Fornece rastreamento em tempo real do ciclo de vida do contêiner.
* **Economia de Custos:** Permite à equipe agir preventivamente, evitando as elevadas taxas de **Demurrage** por contêiner.
* **Ganho de Produtividade:** Elimina a necessidade de acessar dezenas de portais e atualizar as planilhas manualmente.

## 4. Script Destaque

| Script | Tecnologia Chave | Descrição |
| :--- | :--- | :--- |
| `procurar_data_devolucao_vazio.py` | Python + Playwright | Script principal que orquestra a leitura do Excel, o acesso ao navegador (modo *headless* ou visível) e a atualização dos dados do contêiner. |
