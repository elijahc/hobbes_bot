import os

def verify(event, context):
    if (event['token'] == os.environ['VERIFICATION_TOKEN']):
        return event['challenge']
