# Arquitetura Implementada

Dividimos a arquitetura em 3 partes:
* Parte 1: Conversão dos arquivos csv para json
* Parte 2: Preparação para criação dos pacotes no Kinesis a partir dos arquivos json
* Parte 3: Criação dos pacotes Kinesis, das external tables no Athena e dos pacotes parquet

# Parte 1: Conversão dos arquivos csv para json
<img src="https://github.com/HawaiiDataEngineers/SolutionSprint3/blob/main/implementation/solution_sprint_3_architect_part_1.png"></img>
## 1.1 Criar uma instância Cloud9 e carregar o data set do kaggle
Segue procedimento: [Setup Cloud9](https://github.com/HawaiiDataEngineers/SolutionSprint3/blob/main/implementation/cloud9_setup.pdf)

## 1.2 Criar o bucket S3
Acesse o serviço S3 na AWS e crie um bucket chamado small-files-s3, na região Leste dos EUA (Ohio) us-east-2, como mostrado abaixo. **ATENÇÃO!** Todos os serviços criados nesta arquitetura devem ser criados na região **Leste dos EUA (Ohio) us-east-2**

<img src="https://github.com/HawaiiDataEngineers/SolutionSprint3/blob/main/implementation/create_bucket.png"></img>
## 1.4 Realizar o upload dos arquivos .csv do Cloud9 para o bucket S3


## 1.5 

# Preparação para criação dos pacotes no Kinesis a partir dos arquivos json


# Criação dos pacotes Kinesis, das external tables no Athena e dos pacotes parquet



