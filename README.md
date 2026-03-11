# product-registration-automation

#README EN

This project is a Python automation script that automatically registers products on a web platform.
The script simulates user interaction with the system using PyAutoGUI and reads product data from a CSV dataset.

## Features

- Automatically opens the browser
- Logs into the system
- Reads product data from a CSV file
- Fills the product registration form automatically
- Registers multiple products sequentially

## Technologies

- Python
- PyAutoGUI
- Pandas

## Project Structure

main.py → main automation script  
pegar_posicao.py → utility script to capture mouse coordinates  
produtos.csv → dataset containing product information

## Dataset

The dataset contains the following fields:

- codigo
- marca
- tipo
- categoria
- preco_unitario
- custo
- obs

Each row represents a product that will be registered automatically in the system.

## How it works

1. The script opens the browser.
2. It accesses the target website.
3. Performs login automatically.
4. Reads the CSV file using Pandas.
5. Iterates through all products in the dataset.
6. Uses PyAutoGUI to fill the form fields.
7. Submits each product.

## Note

The automation uses fixed screen coordinates.  
Because of that, the script may require adjusting mouse positions depending on screen resolutio

# -------------- #

#README PT-BR

Este projeto é um script de automação em Python que realiza o cadastro automático de produtos em um sistema web.
O script simula a interação de um usuário com a interface do site utilizando a biblioteca PyAutoGUI e utiliza uma base de dados em formato CSV para preencher os campos do formulário automaticamente.

## Funcionalidades

- Abre automaticamente o navegador
- Acessa o sistema web
- Realiza login automaticamente
- Lê os dados de produtos a partir de um arquivo CSV
- Preenche os campos do formulário de cadastro automaticamente
- Realiza o cadastro de múltiplos produtos de forma sequencial

## Tecnologias utilizadas

- Python
- PyAutoGUI
- Pandas

## Estrutura do projeto

main.py → script principal de automação 
pegar_posicao.py → script auxiliar para capturar coordenadas do mouse  
produtos.csv → base de dados contendo as informações dos produtos

## Estrutura da base de dados

O arquivo CSV contém as seguintes colunas:

- codigo
- marca
- tipo
- categoria
- preco_unitario
- custo
- obs

Cada linha representa um produto que será cadastrado automaticamente no sistema.

## Como o script funciona

1. O script abre o navegador automaticamente.
2. Acessa o site alvo.
3. Realiza o login no sistema.
4. Lê o arquivo CSV utilizando a biblioteca Pandas.
5. Percorre todos os produtos da base de dados.
6. Utiliza o PyAutoGUI para preencher os campos do formulário.
7. Realiza o cadastro de cada produto no sistema.

## Observação

A automação utiliza coordenadas fixas da tela para interagir com os elementos da interface.
Por isso, pode ser necessário ajustar as posições do mouse dependendo da resolução da tela ou do ambiente onde o script será executado.
