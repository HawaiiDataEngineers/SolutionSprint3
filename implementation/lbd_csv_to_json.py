import json
import boto3
import os
import csv
import urllib.parse
import logging
from botocore.exceptions import ClientError
import json

# logger config
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')
s3 = boto3.client('s3')
sqs_client = boto3.client("sqs", region_name="us-east-2")


def send_queue_message(queue_url, msg_attributes, msg_body):
    """
    Sends a message to the specified queue.
    """
    try:
        response = sqs_client.send_message(QueueUrl=queue_url,
                                           MessageAttributes=msg_attributes,
                                           MessageBody=msg_body)
    except ClientError:
        logger.exception(f'Could not send meessage to the - {queue_url}.')
        raise
    else:
        return response


def lambda_handler(event, context):
    urlSQS = 'https://sqs.us-east-2.amazonaws.com/776734997000/small-files-csv-2'
    MSG_ATTRIBUTES = {
        'Title': {
            'DataType': 'String',
            'StringValue': 'SQS CSV TO JSON'
        },
        'Author': {
            'DataType': 'String',
            'StringValue': 'Grupo 3'
        }
    }

    bucket_key = {}

    for record in event['Records']:
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        key_name = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
        message = s3.get_object(Bucket=event['Records'][0]['s3']['bucket']['name'], Key=key_name)
        # s3_object = s3.get_object(Bucket=bucket_name, Key=key_name)
        bucket_key["bucket_name"] = bucket_name
        bucket_key["key_name"] = key_name

        print('Bucket', bucket_name)
        print('Objeto', key_name)
        print('Messagebody', bucket_key)

        bucket_key = json.dumps(bucket_key)
        message_body = json.loads(bucket_key)

        msg = send_queue_message(urlSQS, MSG_ATTRIBUTES, bucket_key)
        json_msg = json.dumps(msg, indent=4)
        # json_set = json.dumps(message)
        # message_json = json.loads(json_set)
        # response = sqs_client.send_message(
        #             QueueUrl=urlSQS,
        #             MessageBody=s3_object
        #            )
        print('Message sent to', urlSQS)  