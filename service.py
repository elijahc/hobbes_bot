# -*- coding: utf-8 -*-
import json
import os
import random
from botocore.vendored import requests

from src.responses import random_canned_response, canned_response, EventDispatcher
from src.util import verify

D = EventDispatcher()

def handler(event, context):
    # Your code goes here!

    print("Event Passed to Handler: " + json.dumps(event))

    if event.get('type') == 'url_verification':
        # Respond with event['challenge'] to verify
        return verify(event, context)

    elif event['type'] == 'event_callback':
        # Process event_callbacks
        print('processing event_callback')
        resp = D.exec(event,context,verbose=True)
        print(resp)
    else:
        return {
            'statusCode': 200,
            'body': json.dumps(event),
            # 'body': json.dumps('Hello from Lambda!')
        }
