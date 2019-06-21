import json
import os
import random
from botocore.vendored import requests

from src.responses import random_canned_response, canned_response
from src.util import verify

def lambda_handler(event, context):
    # AWS calls this in response to a post request from slack

    dispatch = {"app_mention": random_canned_response}

    print("Event Passed to Handler: " + json.dumps(event))

    if event['type'] == 'url_verification':
        # Respond with event['challenge'] to verify
        return verify(event, context)

    elif event['type'] == 'event_callback':
        # Process event_callbacks
        print('processing event_callback')
        event_type = event['event']['type']
        print(event_type)
        r = dispatch[event_type](event,context)
        print(r)
    else:
        return {
            'statusCode': 200,
            'body': json.dumps(event),
            # 'body': json.dumps('Hello from Lambda!')
        }
