import json
from botocore.vendored import requests

VERIFICATION_TOKEN = 'WiZIOhg6d7K22FY1vJGHindS'
ACCESS_TOKEN = 'xoxb-295199771607-673384390295-FtiRuYAFrJnqKqoDiTM5Wb2v'
# uri = os.environ['WEBOOK_URI']
def verify(event, context):
    #if (event['token'] == VERIFICATION_TOKEN):
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
    '''
    {
    "token": "XXYYZZ",
    "team_id": "TXXXXXXXX",
    "api_app_id": "AXXXXXXXXX",
    "event": {
            "type": "name_of_event",
            "event_ts": "1234567890.123456",
            "user": "UXXXXXXX1",
            ...
    },
    "type": "event_callback",
    "authed_users": [
            "UXXXXXXX1",
            "UXXXXXXX2"
    ],
    "event_id": "Ev08MFMKH6",
    "event_time": 1234567890
    }
    '''

    dispatch = {
            "app_mention": canned_response,
            }

    print("Event Passed to Handler: " + json.dumps(event))

    if event['type'] == 'url_verification':
        # Respond with event['challenge'] to verify
        return verify(event, context)

    elif event['type'] == 'event_callback':
        # Process event_callbacks
        event_type = event['event']['type']
        dispatch[event_type](event,context)
    else:
        return {
            'statusCode': 200,
            'body': json.dumps(event),
            # 'body': json.dumps('Hello from Lambda!')
        }
