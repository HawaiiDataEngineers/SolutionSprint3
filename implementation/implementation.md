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

## 1.3 Criar a trigger lambda para leitura dos arquivos e envio ao SQS
Crie uma lambda chamada lbd_csv_to_json
<img src="https://github.com/HawaiiDataEngineers/SolutionSprint3/blob/main/implementation/create_lamdba.png"></img>

Configure o bucket S3 como gatilho para ser ativado na criação de qualquer arquivo no bucket, clicando no botão **Adicionar Gatilho**
<img src="https://github.com/HawaiiDataEngineers/SolutionSprint3/blob/main/implementation/trigger_config.png"></img>

Na parte de código coloque os comandos contido no script [lbd_csv_to_json.py](https://github.com/HawaiiDataEngineers/SolutionSprint3/blob/main/implementation/lbd_csv_to_json.py)
<img src="https://github.com/HawaiiDataEngineers/SolutionSprint3/blob/main/implementation/lambda_code.png"></img>

## 1.4 Realizar o upload dos arquivos .csv do Cloud9 para o bucket S3
Dentro da instância do cloud9, no shell, vá parada pasta que foi baixado o dataset e execute os seguintes comandos:
```shell
#spliting files in csv
split -d -l 100000 --additional-suffix=.csv library-collection-inventory.csv files-small/inventory_part_ --verbose 

#test upload 3 csv files to S3 bucket for 
mkdir test_upload
cp files-small/inventory_part_0[0-2]*.csv test_upload/
aws s3 cp test_upload s3://small-files-s3/uploads/input/ --recursive

#upload all csv files to S3 bucket
aws s3 cp files-small s3://train-convert-json/small-files/ --recursive
 ```

## 1.5 Valide o upload dos arquivos
Acesse o bucket e veja se os arquivos estão lá.
<img src="https://github.com/HawaiiDataEngineers/SolutionSprint3/blob/main/implementation/upload_files.png"></img>

## 1.6 Ver  no cloud watch, se a lambda lbd_csv_to_json foi ativada

## 1.7 Criar lambda de conversão dos arquivos csv em json

## 1.8 Criar SQS com saída para a lambda de conversão

## 1.9 Validar a criação dos arquivos json

# Preparação para criação dos pacotes no Kinesis a partir dos arquivos json


# Criação dos pacotes Kinesis em external tables no Athena e dos pacotes parquet



