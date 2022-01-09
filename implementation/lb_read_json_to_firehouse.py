import boto3
import json
import time
import urllib.parse

s3 = boto3.resource('s3')
s3Client = boto3.client('s3')


class KinesisHandler:
    def __init__(self, streamName):
        self.__kinesis = boto3.client('firehose')
        self.__streamName = streamName

    def __prepareDataToFirehoseCall(self, listLine):
        listData = []
        print('Tipo listdata: ', type(listData))
        for line in listLine:
            listData.append(
                {
                    "Data": line
                }
            )

        # print(len(json.dumps(listData)))
        return listData

    def put_record(self, listLine):
        print(self.__prepareDataToFirehoseCall(listLine))
        response = self.__kinesis.put_record_batch(
            DeliveryStreamName=self.__streamName,
            Records=self.__prepareDataToFirehoseCall(listLine)
        )
        # print(listLine)

        if (response['FailedPutCount'] > 0):
            print("FailedPutCount: " + str(response['FailedPutCount']))
            if (response['FailedPutCount'] == len(listLine)):
                time.sleep(1)
                self.put_record(listLine)
            # print(response)

        # print(json.dumps(response))


def lambda_handler(event, context):
    sqs_event = {"event": event}
    # print(sqs_event)
    # bucket_objectkey = {}
    class_kinesis = KinesisHandler('ingested-json')

    for record in event['Records']:
        message = json.loads(record["body"])
        bucket_name = message['bucket_name']
        print(bucket_name)
        key_name = message['key_name']
        print(key_name)
        s3_object = s3Client.get_object(Bucket=bucket_name, Key=key_name)
        data = s3_object['Body'].read()
        contents = data.decode('utf-8')
        # print(contents)

        listajson = []
        # message_body = json.loads(bucket_objectkey)

        lines = contents.split('\n')
        for x in lines:
            # print('Conteúdo do Arquivo: ', contents)
            # bucket_name = message['bucket_name']
            class_kinesis.put_record([x])