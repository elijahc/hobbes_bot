import os
import json
import pytest

from src.responses import EventDispatcher

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

@pytest.fixture(scope="session")
def evd():
    evd = EventDispatcher()

    return evd

def test_standardAppMention(evd, events):
    ev = events['standardAppMention.json']
    context = None
    assert type(ev) == dict, ev

    out = evd.exec(ev,context,verbose=True)
    
    assert 0, out

