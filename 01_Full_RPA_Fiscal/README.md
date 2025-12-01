# 🤖 Automação Full RPA: Lançamento Fiscal (NF-e/NFS-e)

Este projeto demonstra a criação de um robô de RPA (Robotic Process Automation) para automatizar o processo que antes era 100% manual de lançamento de notas fiscais em um sistema web interno.

---

## 1. Desafio de Negócio

* **Problema:** O processo manual de lançamento de NFs (Notas Fiscais de Serviço) era repetitivo e de alta demanda, propenso a erros de digitação e consumia, em média, **25 horas de trabalho mensal** da equipe.
* **Requisito:** Necessidade de um método robusto e rápido que garantisse a inserção de dados corretos e a captura do protocolo de lançamento para auditoria.

## 2. Solução Técnica

Desenvolvimento de um bot utilizando **Python** e a biblioteca **Selenium** (para interação com o navegador).

* **Entrada de Dados:** O bot lê um arquivo Excel (`PROTOCOLO.xlsx`) que contém todos os dados essenciais (número da nota, CNPJ, valores, etc.) em formato estruturado.
* **Navegação e Input:** Utiliza XPATHs e CSS Selectors para navegar no sistema web, fazer login, preencher formulários complexos e simular a interação humana (cliques, digitação e seleções).
* **Saída de Dados:** Após o lançamento bem-sucedido, o bot realiza o *Web Scraping* do **ID de Lançamento/RR** gerado pelo sistema e o insere automaticamente de volta na planilha Excel original, fechando o ciclo de automação.

## 3. Scripts e Drivers

O projeto inclui duas versões do script, garantindo a compatibilidade com os navegadores mais utilizados na empresa.

| Script | Tecnologia Chave | Descrição |
| :--- | :--- | :--- |
| `lancar_nfs_navegador_google.py` | Python + Selenium (Chrome) | Versão otimizada para o Google Chrome. |
| `lancar_nfs_navegador_edge.py` | Python + Selenium (Edge) | Versão otimizada para o Microsoft Edge. |

## 4. Estrutura de Pastas

Para simular o ambiente de produção, este projeto espera o arquivo de entrada na pasta `../input_data`.

* `../input_data/PROTOCOLO.xlsx`: Planilha de entrada contendo os dados a serem lançados.
* `lancar_nfs_navegador_google.py`: Script principal de automação.
