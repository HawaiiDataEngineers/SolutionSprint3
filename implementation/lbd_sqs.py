import json
import csv
import boto3
import os
import datetime as dt
from io import StringIO
import uuid

s3 = boto3.resource('s3')
s3Client = boto3.client('s3')


def lambda_handler(event, context):
    datestamp = dt.datetime.now().strftime("%Y/%m/%d")
    timestamp = dt.datetime.now().strftime("%s")

    filename_json = "/tmp/file_{ts}.json".format(ts=timestamp)
    filename_csv = "/tmp/file_{ts}.csv".format(ts=timestamp)
    keyname_s3 = "uploads/output/{ds}/{ts}.json".format(ds=datestamp, ts=timestamp)
    collumns = ["BibNum", "Title", "Author",
                "ISBN", "PublicationYear", "Publisher", "Publisher",
                "Subjects", "ItemType", "ItemCollection", "FloatingItem",
                "ItemLocation", "ReportDate", "ItemCount"]
    json_data = []
    listRows = []
    sql_event = {"event": event}
    for record in event["Records"]:
        message = json.loads(record["body"])
        print(json.dumps(message))
        bucket_name = message['bucket_name']
        print(bucket_name)
        key_name = message['key_name']
        print(key_name)
        s3_object = s3Client.get_object(Bucket=bucket_name, Key=key_name)
        print(s3_object)
        data = s3_object['Body'].read()
        # contents = data.decode('utf-8')
        # print(contents)

        s = StringIO(data.decode("utf-8"))
        linha = csv.reader(s, skipinitialspace=True)

        for row in linha:
            data = {}
            data["id"] = str(uuid.uuid4())
            for i in range(len(collumns) - 1):
                data[collumns[i]] = row[i]
            listRows.append(data)

        fileContent = ""
        escapeChar = "\n"
        for row in listRows:
            fileContent += json.dumps(row)
            fileContent += escapeChar

        removal = escapeChar
        reverse_removal = removal[::-1]

        replacement = ""
        reverse_replacement = replacement[::-1]
        fileContent = fileContent[::-1].replace(reverse_removal,
                                                reverse_replacement, 1)[::-1]
        filename2 = key_name.split("/")[2]
        filename = filename2.split(".")[0] + ".json"
        print(filename)

        object = s3.Object(bucket_name, "uploads/output/" + filename)
        object.put(Body=fileContent.encode())