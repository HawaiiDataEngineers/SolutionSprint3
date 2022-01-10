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

Na parte de código coloque os comandos contidos no script [lbd_csv_to_json.py](https://github.com/HawaiiDataEngineers/SolutionSprint3/blob/main/implementation/lbd_csv_to_json.py)

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
<img src="https://github.com/HawaiiDataEngineers/SolutionSprint3/blob/main/implementation/cloud_watch_lbd_csv_to_json.png"></img>

## 1.7 Criar lambda de conversão dos arquivos csv em json
Crie uma lamdba chamada lbd_sqs contendo o script [lbd_sqs.py](https://github.com/HawaiiDataEngineers/SolutionSprint3/blob/main/implementation/lbd_sqs.py)

## 1.8 Criar SQS com saída para a lambda de conversão
<img src="https://github.com/HawaiiDataEngineers/SolutionSprint3/blob/main/implementation/sqs_small-files-csv-2.png"></img>

## 1.9 Criar SQS com saída para ser utilizada com DLQ
<img src="https://github.com/HawaiiDataEngineers/SolutionSprint3/blob/main/implementation/sqs_small-files-csv-dlq.png"></img>

## 1.10 Validar a criação dos arquivos json
<img src="https://github.com/HawaiiDataEngineers/SolutionSprint3/blob/main/implementation/output_json.png"></img>

# Parte 2: Preparação para criação dos pacotes no Kinesis a partir dos arquivos json
<img src="https://github.com/HawaiiDataEngineers/SolutionSprint3/blob/main/implementation/solution_sprint_3_architect_part_2.png"></img>
## 2.1 Criação da lambda de leitura dos arquivos json
Crie lambda com gatilho para a pasta outpu do S3, chamada lb_read_from_output_sqs contendo o script [lb_read_from_output_sqs.py](https://github.com/HawaiiDataEngineers/SolutionSprint3/blob/main/implementation/lb_read_from_output_sqs.py)
<img src="https://github.com/HawaiiDataEngineers/SolutionSprint3/blob/main/implementation/lbd_read_from_output_sqs.png"></img>

## 2.2 Criar SQS para envio das informações que irão criar o pacote no Kinesis 
Crie uma fila SQS denominada raw-json que receberá o bucket e o nome das keys contidas na pasta output. 
<img src="https://github.com/HawaiiDataEngineers/SolutionSprint3/blob/main/implementation/raw_json.png"></img>

Criar outra fila, raw-json-dlq para DLQ.
<img src="https://github.com/HawaiiDataEngineers/SolutionSprint3/blob/main/implementation/raw_json_dlq.png"></img>

## 2.3 Criar Lambda de prepação dos dados para criação dos pacotes no Kinesis
Crie uma lambda chamada lb_read_from_output_sqs e adicione o gatilho para pasta /uploads/output, para o evento ObjectCreatedbyPut. 

<img src="https://github.com/HawaiiDataEngineers/SolutionSprint3/blob/main/implementation/lb_read_from_output_sqs.png"></img>

Por fim na parte de código inclua o conteúdo do script [lb_read_from_output_sqs.py](https://github.com/HawaiiDataEngineers/SolutionSprint3/blob/main/implementation/lb_read_from_output_sqs.py)

# Parte 3: Criação dos pacotes Kinesis em external tables no Athena e dos pacotes parquet
<img src="https://github.com/HawaiiDataEngineers/SolutionSprint3/blob/main/implementation/solution_sprint_3_architect_part_3.png"></img>

## 3.1 Criação do Kinesis
<img src="https://github.com/HawaiiDataEngineers/SolutionSprint3/blob/main/implementation/kinesis_ingested_json.png"></img>

## 3.2 Validação da criação do pacote no S3
<img src="https://github.com/HawaiiDataEngineers/SolutionSprint3/blob/main/implementation/s3_ingested-json.png"></img>

## 3.3 Leitura dos dados no Athena


## 3.4 Criação dos arquivos parquet



