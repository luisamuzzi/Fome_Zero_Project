# Projeto Fome Zero:

## 1. Problema de negócio

A empresa Fome Zero é uma marketplace de restaurantes. Ou seja, seu core business é facilitar o encontro e negociações de clientes e restaurantes. Os restaurantes fazem o cadastro dentro da plataforma da Fome Zero, que disponibiliza informações como endereço, tipo de culinária servida, se possui reservas, se faz entregas e também uma nota de avaliação dos serviços e produtos do restaurante, dentre outras informações.

Você acaba de ser contratado como Cientista de Dados da empresa Fome Zero, e a sua principal tarefa nesse momento é ajudar o CEO a identificar pontos chaves da empresa, respondendo às perguntas que ele fizer utilizando dados. O CEO também foi recém contratado e precisa entender melhor o negócio para conseguir tomar as melhores decisões estratégicas e alavancar ainda mais a Fome Zero, e para isso, ele precisa que seja feita uma análise nos dados da empresa e que sejam gerados dashboards, a partir dessas análises, para responder às seguintes perguntas:

### Informações gerais:

1. Quantos restaurantes únicos estão registrados?
2. Quantos países únicos estão registrados?
3. Quantas cidades únicas estão registradas?
4. Qual o total de avaliações feitas?
5. Qual o total de tipos de culinária registrados?

### Informações por país:

1. Qual o número de restaurantes registrados por país?
2. Quantas são as cidades registradas por país?
3. Qual a média de avaliações feitas por país?
4. Qual a média de preço de um prato para duas pessoas por país?

### Informações por cidade:

1. Quais são as cidades com mais restaurantes na base de dados?
2. Quais são as cidades com mais restaurantes com média de avaliação acima de 4?
3. Quais são as cidades com mais restaurantes com média de avaliação abaixo de 2,5?
4. Quais são as cidades com o maior número de tipos culinários distintos?

### Informações por tipo de culinária:

1. Quais são os melhores restaurantes dos principais tipos culinários?
2. Quais são os melhores tipos culinários?
3. Quais são os piores tipos culinários?

O objetivo desse projeto é criar um conjunto de gráficos e/ou tabelas que exibam essas métricas da melhor forma possível para o CEO.

## 2. Premissas assumidas para a análise

1. Marketplace foi o modelo de negócio assumido.
2. As 4 principais visões do negócio foram: Visão geral, visão países, visão cidades e visão tipos culinários.

## 3. Estratégias da solução

O painel estratégico foi desenvolvido utilizando as métricas que refletem as 4 principais visões da empresa:

1. Visão do geral
2. Visão por país
3. Visão por cidade
4. Visão por tipos culinários

Cada visão é representada pelo seguinte conjunto de métricas:

1. Visão geral
    1. Número de restaurantes cadastrados
    2. Número de países cadastrados
    3. Número de cidades cadastradas
    4. Número de avaliações feitas na plataforma  
    5. Número de tipos culinários cadastrados na plataforma
2. Visão países
    1. Distribuição da quantidade de restaurantes registrados por país
    2. Distribuição da quantidade de cidades registradas por país
    3. Distribuição da média de avaliações feitas por país
    4. Distribuição da média de preço de um prato para duas pessoas por país
3. Visão cidades
    1. Distribuição das 10 cidades com mais restaurantes cadastrados na base de dados
    2. Distribuição das 10 cidades com restaurantes com média de avaliação acima de 4
    3. Distribuição das 10 cidades com restaurantes com média de avaliação abaixo de 2,5
    4. Distribuição das 10 cidades com restaurantes com o maior número de tipos de culinária distintos
4. Visão tipos de culinária
    1. Média de avaliação dos melhores restaurantes dos principais tipos culinários (Italian, American, Arabian, Japanese e Home-made)
    2. Top restaurantes por média de avaliação
    3. Top melhores tipos de culinária
    4. Top piores tipos de culinária

## 4. Top 3 Insights de dados

1. A Índia é o país com mais restaurantes e cidades cadastradas e o segundo país com maior número médio de avaliações (atrás da Indonésia).
2. Emirados Árabes Unidos, Índia, Turquia e EUA tem as top 10 cidades com mais restaurantes registrados. Sendo a Índia o país que possui mais cidades no top 10 cidades com média de avaliação acima de 4 e no top 10 cidades com média de avaliação abaixo de 2,5 (nesse último, juntamente com o Brasil).
3. O tipo culinário mais bem avaliado é Outros e os piores avaliados são Somente drinks e Mineiro.

## 5. O produto final do projeto

Painel online, hospedado em um Cloud e disponível para acesso em qualquer dispositivo conectado à internet.

O painel pode ser acessado através desse link: https://lm-fome-zero.streamlit.app/

## 6. Conclusão

O objetivo desse projeto é criar um conjunto de gráficos e/ou tabelas que exibam essas métricas da melhor forma possível para o CEO.

Das visões apresentadas, podemos concluir que a Índia é o país com o maior número de restaurantes e cidades cadastradas. Além de ter o maior número de restaurantes no top 10 com média acima de 4 e com média abaixo de 2,5.

## 7. Próximos passos

1. Reduzir o número de métricas.
2. Criar novos filtros.
3. Adicionar novas visões de negócio.
