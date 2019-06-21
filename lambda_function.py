import json
import numpy as np
from botocore.vendored import requests

VERIFICATION_TOKEN = 'WiZIOhg6d7K22FY1vJGHindS'
ACCESS_TOKEN = 'xoxp-295199771607-293477083728-660133512179-729dd16f7cbc096a49fc776384c7140d'
QUOTES = [
        "During the time men live without a common power to keep them all in awe, they are in that conditions called war; and such a war, as if of every man, against every man.",
        "Man gives indifferent names to one and the same thing from the difference of their own passions; as they that approve a private opinion call it opinion; but they that mislike it, heresy: and yet heresy signifies no more than private opinion",
        "Words are wise men's counters, they do but reckon by them: but they are the money of fools, that value them by the authority of an Aristotle, a Cicero, or a Thomas, or any other doctor whatsoever, if but a man",
        "Moral philosophy is nothing else but the science of what is good, and evil, in the conversation, and society of mankind. Good, and evil, are names that signify our appetites, and aversions; which in different tempers, customs, and doctrines of men, are different."
        ]
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

def random_canned_response(event, context):
    q_idx = np.random.choice(np.arange(len(QUOTES)))

    text = QUOTES[q_idx]
    message = {
        'token': ACCESS_TOKEN,
        'channel': event['event']['channel'],
        'text':text
    }
    r = requests.post('https://slack.com/api/chat.postMessage',data=message)


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
