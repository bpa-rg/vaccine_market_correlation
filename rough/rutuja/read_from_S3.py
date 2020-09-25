import boto3
import json

ACCESS_KEY = 'AKIAQJ7HRZ3USL7TURBO'
SECRET_KEY = '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'

def read_from_S3(file_location):
    s3 = boto3.resource(
    service_name='s3',
    region_name='us-east-2',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
    )
    #file_name='devs/aman/2020-09-25162605.755894.json'
    #file_name=file_location
    obj = s3.Object('bpa-rg-rough',file_location)
    #obj = s3.Object('bpa-rg-rough',file_name)
    body = obj.get()['Body'].read()
    print(body)
    return (body)
    dict=body
    a = json.loads(dict)
    print(a["name"])
    find_name=(a["name"])
    print(find_name)
    return (find_name)