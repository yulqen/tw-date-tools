from unittest.mock import patch, MagicMock

from ..http import APIResource, parse

data = """{"locale":"en-GB","region":"","date":"2017-01-01","description":"New Year's Day","type":"NF","notes":""}
{"locale":"en-GB","region":"","date":"2017-01-02","description":"New Year's Day (observed)","type":"NV","notes":""}
{"locale":"en-GB","region":"","date":"2017-04-14","description":"Good Friday","type":"NRV","notes":""}
{"locale":"en-GB","region":"","date":"2017-04-17","description":"Easter Monday","type":"NRV","notes":""}
{"locale":"en-GB","region":"","date":"2017-05-01","description":"Early May Bank Holiday","type":"NV","notes":""}
{"locale":"en-GB","region":"","date":"2017-05-29","description":"Spring Bank Holiday","type":"NV","notes":""}
{"locale":"en-GB","region":"","date":"2017-08-28","description":"August Bank Holiday","type":"NV","notes":""}
{"locale":"en-GB","region":"","date":"2017-12-25","description":"Christmas Day","type":"NRF","notes":""}
{"locale":"en-GB","region":"","date":"2017-12-26","description":"Boxing Day","type":"NF","notes":""}"""


# don't need the decorator here but leaving it for educational purposes for the moment
@patch('tw_holidays.http.APIResource')
def test_get_data(mock_class):
    ar = APIResource('https://holidata.net/en-GB/2017.json')
    ar._fetch = MagicMock(return_value=data)
    assert ar.get_string_io().readline().rstrip() == """{"locale":"en-GB","region":"","date":"2017-01-01","description":"New Year's Day","type":"NF","notes":""}"""

