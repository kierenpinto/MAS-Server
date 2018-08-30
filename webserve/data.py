import time
import dynamodb
# Data to serve with our API
RESULTS = [
    {
    "device": "Doug",
    "timestamp": "Farrell",
    "level": int(time.time())
    }
]

# Create a handler for our read (GET) events
def live():
    """
    This function responds to a request for /api/live
    with the complete lists of events

    :return:        sorted list of events
    """
    # Create the list of events from our data 1535183060
    query_response = dynamodb.query_points(0,1535186094,0,'9E65F900F57B')
    entries = query_response['Items']
    RESULTS = list()
    for item in entries:
        result = {
            "device": item['device'],
            "timestamp": item['time']*1000,
            "level": item['data'] 
        }
        RESULTS.append(result)
    return RESULTS


def query(start_ts,end_ts):
    """
    This function responds to a request for /api/live
    with the complete lists of events

    :return:        sorted list of events
    """
    # Create the list of events from our data
    if type(start_ts)==int and type (end_ts) == int:
        query_response = dynamodb.query_points(start_ts/1000,end_ts/1000,0,'9E65F900F57B')
        entries = query_response['Items']
        RESULTS = list()
        for item in entries:
            result = {
                "device": item['device'],
                "timestamp": item['time']*1000,
                "level": item['data'] 
            }
            RESULTS.append(result)
        return RESULTS
    else:
        return list()