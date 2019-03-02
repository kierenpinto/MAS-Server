import boto3
from boto3.dynamodb.conditions import Key, Attr
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('airsense2')

def save(device_id,timestamp,datetime,data):
    item = {
        'device':str(device_id),
        'time': int(timestamp),
        'utc datetime': str(datetime),
        'data':str(data)
        }
    table.put_item(Item=item)
