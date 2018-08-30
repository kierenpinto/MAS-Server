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


def query_number_points(minsec,maxsec,device):
    """ Find the number of points between a range at timestamp minsec and maxsec on a specific device
    dateex = {
    'year': 2018,
    'month': 8,
    'day': 22,
    'hour':21,
    'min':24,
    'sec':0
    }
    
    """
    response = table.query(
        KeyConditionExpression=Key('device').eq('abc123')&Key('time').lt(int(maxsec))
        )
    return dict('items',response['items'],'count',response['count'])

def query_points(minsec,maxsec,number,device):
    ''' Return a certain number of datapoints between minsec and maxsec timestamps on a device'''
    response = table.query(
        KeyConditionExpression=Key('device').eq(device)&Key('time').lt(int(maxsec))&Key('time').gt(int(minsec))
        )
    return dict('items',response['items'],'count',response['count'])
