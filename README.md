# Global Solution - Pipeline de Dados Espaciais

## Tema do Projeto

Monitoramento de Asteroides Próximos da Terra utilizando a NASA NEO API (Near Earth Objects).

Fonte de dados utilizada:

https://api.nasa.gov/neo/rest/v1/feed?api_key=DEMO_KEY

---

# Objetivo

Desenvolver um pipeline de dados automatizado relacionado ao contexto da Indústria Espacial, realizando a extração, transformação, armazenamento e análise de dados de asteroides próximos da Terra.

O pipeline foi desenvolvido em Python e estruturado para futura orquestração através do Apache Airflow, seguindo as etapas de Engenharia de Dados exigidas no trabalho.

---

# Estrutura do Projeto

GS-Space-Pipeline

├── data

│   ├── raw

│   │   └── asteroids_raw.csv

│   │

│   └── processed

│       └── asteroids_processed.csv

│

├── scripts

│   ├── extract.py

│   ├── transform.py

│   ├── load.py

│   ├── test_db.py

│   ├── queries.py

│   └── query_top10.py

│

├── dags

│

├── sql

│

├── requirements.txt

│

└── space.db

---

# Arquitetura do Pipeline

NASA NEO API

↓

Extração (extract.py)

↓

Armazenamento Temporário (asteroids_raw.csv)

↓

Transformação (transform.py)

↓

Armazenamento Processado (asteroids_processed.csv)

↓

Carga (load.py)

↓

Banco de Dados

↓

Consultas Analíticas SQL

---

# Etapa 1 - Extração dos Dados

Arquivo:

scripts/extract.py

Objetivo:

Consumir a API pública da NASA e coletar dados de asteroides próximos da Terra.

Campos extraídos:

* id
* name
* absolute_magnitude_h
* is_potentially_hazardous

Resultado:

Arquivo gerado:

data/raw/asteroids_raw.csv

Quantidade obtida:

36 registros

Requisito atendido:

✔ Extração de dados de fonte externa (API)

---

# Etapa 2 - Armazenamento Temporário

Os dados coletados foram armazenados em um arquivo CSV bruto para posterior processamento.

Arquivo:

data/raw/asteroids_raw.csv

Requisito atendido:

✔ Armazenamento temporário dos dados

---

# Etapa 3 - Transformação e Tratamento

Arquivo:

scripts/transform.py

Transformações realizadas:

1. Remoção de registros nulos

df.dropna()

2. Conversão de tipos numéricos

pd.to_numeric()

3. Padronização de textos

str.strip()

4. Conversão de campos booleanos

astype(str)

Resultado:

Arquivo gerado:

data/processed/asteroids_processed.csv

Resultado da execução:

Antes: 36 registros

Depois: 36 registros

Requisito atendido:

✔ Limpeza dos dados

✔ Conversão de tipos

✔ Padronização

✔ Tratamento de valores inválidos

---

# Etapa 4 - Carga dos Dados

Arquivo:

scripts/load.py

Banco utilizado durante o desenvolvimento:

SQLite

Arquivo do banco:

space.db

Tabela criada:

CREATE TABLE asteroids (
id TEXT,
name TEXT,
absolute_magnitude_h REAL,
is_potentially_hazardous TEXT
);

Resultado:

36 registros carregados com sucesso.

Requisito parcialmente atendido:

✔ Carga em banco de dados

Pendente:

* Migração para Oracle Database da FIAP

---

# Validação da Carga

Arquivo:

scripts/test_db.py

Objetivo:

Consultar os dados armazenados e validar a carga realizada.

Resultado:

Validação concluída com sucesso.

---

# Consultas Analíticas SQL

## Consulta 1 - Quantidade Total de Asteroides

SELECT COUNT(*)
FROM asteroids;

Objetivo:

Identificar o total de registros processados.

---

## Consulta 2 - Magnitude Média

SELECT AVG(absolute_magnitude_h)
FROM asteroids;

Objetivo:

Calcular a magnitude média dos asteroides monitorados.

---

## Consulta 3 - Maior Magnitude Registrada

SELECT MAX(absolute_magnitude_h)
FROM asteroids;

Objetivo:

Identificar o maior valor de magnitude presente nos dados.

---

## Consulta 4 - Asteroides Perigosos x Não Perigosos

SELECT
is_potentially_hazardous,
COUNT(*)
FROM asteroids
GROUP BY is_potentially_hazardous;

Objetivo:

Comparar a quantidade de asteroides classificados como potencialmente perigosos.

---

## Consulta 5 - Ranking de Magnitude

SELECT
name,
absolute_magnitude_h
FROM asteroids
ORDER BY absolute_magnitude_h DESC;

Objetivo:

Gerar um ranking dos asteroides por magnitude.

---

# Etapas Pendentes

## Oracle Database

Necessário:

* Obter usuário e senha da FIAP
* Criar conexão com o Oracle
* Criar tabela Oracle
* Adaptar load.py para utilizar oracledb
* Carregar os registros no Oracle

Dados fornecidos pela FIAP:

Host: oracle.fiap.com.br

Porta: 1521

SID: ORCL

---

## Apache Airflow

Necessário:

Criar DAG contendo:

extract

↓

transform

↓

load

ou

extract

↓

transform

↓

load

↓

analytics

Arquivo esperado:

dags/asteroid_pipeline.py

Objetivo:

Automatizar a execução completa do pipeline.

---

## Evidências para Entrega

Necessário gerar:

* Print da DAG executando no Airflow
* Print da tabela populada no Oracle
* Print das consultas SQL
* Print dos resultados das consultas

---

# Conclusão

Foi desenvolvido um pipeline de dados para coleta e processamento de informações sobre asteroides próximos da Terra utilizando a NASA NEO API.

O pipeline realiza a extração dos dados, armazenamento temporário, transformação, tratamento e carga em banco de dados, permitindo a execução de análises analíticas através de consultas SQL.

A solução atende aos conceitos de integração de dados, tratamento de informações e arquitetura moderna de dados exigidos pela Global Solution, restando apenas a integração final com Oracle Database e a orquestração através do Apache Airflow para conclusão completa do projeto.
