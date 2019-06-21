import os
import json
import pytest
import subprocess

from src.util import verify

def load_event_from_json(json_path):
    with open(json_path) as f:
        return json.load(f)

@pytest.fixture(scope="session")
def events():
    evs = os.listdir('test/events')
    event_fps = [os.path.join('test','events',f) for f in evs]
    for f in event_fps:
        assert os.path.exists(f)

    evs = {k:load_event_from_json(v) for k,v in zip(evs,event_fps)}

    return evs

def test_urlVerification(events):
    event = events['url_verification.json']
    assert type(event) == dict, event
    out = verify(event, None)
    assert out == event.get('challenge'), out
