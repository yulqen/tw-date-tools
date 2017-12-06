from unittest.mock import MagicMock
from ..http import get_json


def test_get_json():
    data = get_json('https://holidata.net/en-GB/2017.json')
