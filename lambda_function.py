import json
from botocore.vendored import requests

VERIFICATION_TOKEN = 'WiZIOhg6d7K22FY1vJGHindS'
ACCESS_TOKEN = 'xoxp-295199771607-293477083728-660133512179-729dd16f7cbc096a49fc776384c7140d'
# uri = os.environ['WEBOOK_URI']
def verify(event, context):
    if (event['token'] == VERIFICATION_TOKEN):
        return event['challenge']

def process_postmessage(event,context):
    text = "Life is solitary, poor, nasty, brutish, and short"
    message = {
        'token': ACCESS_TOKEN,
        'channel': event['event']['channel'],
        'text':text
    }

    r = requests.post('https://slack.com/api/chat.postMessage',data=message)

    return r

def canned_response(event,context):
    text = "Life is solitary, poor, nasty, brutish, and short"
    message = {
        'token': ACCESS_TOKEN,
        'channel': event['event']['channel'],
        'text':text
    }
    r = requests.post('https://slack.com/api/chat.postMessage',data=message)

    return r

def lambda_handler(event, context):
    # AWS calls this in response to a post request from slack

    dispatch = {"app_mention": canned_response}

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
