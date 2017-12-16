import datetime
from ..parser import RCParser

def test_file_presence(holiday_rc_file):
    with open(holiday_rc_file, 'r') as f:
        line = f.readline()
        assert line[0] == '#'


def test_rc_language(holiday_rc_file):
    rc = RCParser(holiday_rc_file)
    assert rc.language == 'en'
    assert rc.country == 'GB'


def test_rc_holiday_dict(holiday_rc_file):
    rc = RCParser(holiday_rc_file)
    assert "New Year's Day" in rc.holidays.keys()
    assert "Good Friday" in rc.holidays.keys()

#def test_contains_date_line(holiday_rc_file):
#    rc_parser = rc_parser(holiday_rc_file)
#    assert rc_parser.language == 'en'
