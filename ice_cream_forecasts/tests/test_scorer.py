import approvaltests
import requests

import scorer
from scorer import get_score, IceCream, get_score_with_weather

def test_get_score_with_weather():
    #assert get_score_with_weather(True, IceCream.Strawberry) == 10
    weathers = [True, False]
    flavours = [IceCream.Strawberry, IceCream.Chocolate, IceCream.Vanilla, None]
    approvaltests.verify_all_combinations(
        get_score_with_weather,
        [
            weathers,
            flavours
        ],
        formatter=print_get_score
    )

def print_get_score(args, result):
    return f"{args} => {result}\n"


class StubWeatherServiceResponse:
    def __init__(self):
        self.status_code = 200

    def json(self):
        return {"weather":{"main":"Sunny"}}


def test_lookup_weather_default_location(monkeypatch):
    def stub_requests_get(*args, **kwargs):
        return StubWeatherServiceResponse();

    monkeypatch.setattr(requests, "get", stub_requests_get)
    assert scorer.lookup_weather()==True