# Extrator de Informações de Notícias

## Descrição
Este repositório contém um script em Python desenvolvido para extrair informações detalhadas de notícias de uma planilha Excel (xlsx) e salvar os resultados de maneira organizada em um arquivo de texto. O script utiliza a poderosa biblioteca pandas para manipulação eficiente de dados.

## Como Utilizar o Script

### Requisitos Prévios
Antes de executar o script, certifique-se de ter o Python instalado em seu ambiente. Para instalar as dependências necessárias, execute o seguinte comando no terminal:

pip install pandas

### Execução
O script pode ser executado a partir do terminal ou de um ambiente Python. Ajuste os caminhos dos arquivos de entrada e saída conforme necessário.

## Funcionamento Detalhado do Script

### Entrada
O script espera um arquivo Excel contendo informações detalhadas sobre notícias. Certifique-se de fornecer o caminho correto para o arquivo no seguinte formato:

path_bd = './caminho/do/seu/arquivo.xlsx'

### Saída Organizada
Os resultados da extração são salvos em um arquivo de texto, seguindo um formato claro e organizado. O caminho e o nome do arquivo de saída podem ser personalizados conforme sua preferência:

path_output = './caminho/do/seu/saida.txt'

## Tratamento Excepcional de Erros
O script incorpora tratamento para diversos tipos de erros, tais como não localização do arquivo Excel, arquivo vazio ou problemas na leitura do Excel. As mensagens de erro fornecidas são informativas para facilitar a resolução de problemas potenciais.

*** 

# News Information Extractor

## Description
This repository contains a Python script developed to extract detailed information from news in an Excel spreadsheet (xlsx) and save the results in an organized manner to a text file. The script utilizes the powerful pandas library for efficient data manipulation.

## How to Use the Script

### Prerequisites
Before running the script, make sure you have Python installed on your environment. To install the necessary dependencies, execute the following command in the terminal:

pip install pandas

### Execution
The script can be executed from the terminal or a Python environment. Adjust the paths of the input and output files as needed.

## Detailed Script Operation

### Input
The script expects an Excel file containing detailed information about news. Make sure to provide the correct path to the file in the following format:

path_bd = './path/to/your/file.xlsx'

### Organized Output
The extraction results are saved to a text file in a clear and organized format. The path and name of the output file can be customized according to your preference:

path_output = './path/to/your/output.txt'

## Exceptional Error Handling
The script incorporates handling for various types of errors, such as the Excel file not being found, an empty file, or issues with reading the Excel file. The provided error messages are informative to facilitate the resolution of potential issues.
