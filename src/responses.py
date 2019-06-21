import os
import random
from botocore.vendored import requests

QUOTES = [
        "During the time men live without a common power to keep them all in awe, they are in that conditions called war; and such a war, as if of every man, against every man.",
        "Man gives indifferent names to one and the same thing from the difference of their own passions; as they that approve a private opinion call it opinion; but they that mislike it, heresy: and yet heresy signifies no more than private opinion",
        "Words are wise men's counters, they do but reckon by them: but they are the money of fools, that value them by the authority of an Aristotle, a Cicero, or a Thomas, or any other doctor whatsoever, if but a man",
        "Moral philosophy is nothing else but the science of what is good, and evil, in the conversation, and society of mankind. Good, and evil, are names that signify our appetites, and aversions; which in different tempers, customs, and doctrines of men, are different.",
        "Life is solitary, poor, nasty, brutish, and short",
        ]

def random_canned_response(event, context):
    q_idx = random.randrange(len(QUOTES))

    text = QUOTES[q_idx]
    message = {
        'token': os.environ['ACCESS_TOKEN'],
        'channel': event['event']['channel'],
        'text':text
    }
    r = requests.post('https://slack.com/api/chat.postMessage',data=message)
    return r

def canned_response(event,context):
    text = "Life is solitary, poor, nasty, brutish, and short"
    message = {
        'token': os.environ['ACCESS_TOKEN'],
        'channel': event['event']['channel'],
        'text':text
    }
    r = requests.post('https://slack.com/api/chat.postMessage',data=message)

    return r

class EventDispatcher(object):
    def __init__(self):
        pass

    def app_mention(self, event, context):
        resp = random_canned_response(event, context)
        return resp

    def exec(self, event, context, verbose=False):
        event_type = event['event']['type']
        if verbose:
            print(event_type)

        resp = getattr(self, event_type)(event, context)

        if verbose:
            print(resp.content)
            print(resp)
        return resp


def process_postmessage(event,context):
    text = "Life is solitary, poor, nasty, brutish, and short"
    message = {
        'token': ACCESS_TOKEN,
        'channel': event['event']['channel'],
        'text':text
    }

    r = requests.post('https://slack.com/api/chat.postMessage',data=message)

    return r
