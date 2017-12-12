"""
Over-engineered way to handle holiday and general date data in taskwarrior.

Currently, tw contains holiday data files in the installation at /usr/share/taskwarrior,
in the same location as colour files.

The data is relatively limited - 8 dates for the GB calendar. Whilst this is fine, we
might wish to be able to do things with these dates. Some ideas:

    - quickly chose a calendar to use, without having to find the correct file and
    amend your .taskrc file
    - print a list of holidays current in your calendar
    - warn you if you set a deadline for a holiday date
    - get a richer set of holiday data from the internet and install it in taskwarrior

More general date data requirements:

    - analyse which are your most popular days for completing a task, and which are
    least popular
    - provide basic data about tasks added by week, month, year, etc
    - output your deadlines to Google Calendar
    - automatically schedule due dates based on some criteria, possibly data from
    Google Calendar

"""
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
@patch('tdt.http.APIResource')
def test_get_data(mock_class):
    ar = APIResource('https://holidata.net/en-GB/2017.json')
    ar._fetch = MagicMock(return_value=data)
    assert ar.get_string_io().readline().rstrip() == """{"locale":"en-GB","region":"","date":"2017-01-01","description":"New Year's Day","type":"NF","notes":""}"""

