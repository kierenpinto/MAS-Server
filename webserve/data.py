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

# Create a handler for our read (GET) people
def live():
    """
    This function responds to a request for /api/people
    with the complete lists of people

    :return:        sorted list of people
    """
    # Create the list of people from our data 1535183060
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