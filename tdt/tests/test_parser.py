import os
from ..parser import RCParser, rc_paths
from unittest.mock import patch


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
    assert "New Year's Day_2015" in rc.holidays.keys()
    assert "New Year's Day_2016" in rc.holidays.keys()
    assert "Good Friday_2015" in rc.holidays.keys()
    assert "Good Friday_2016" in rc.holidays.keys()


def test_other_file_metadata(holiday_rc_file):
    rc = RCParser(holiday_rc_file)
    assert rc.language == "en"
    assert rc.country == "GB"


def test_rc_files_in_system():
    with patch('os.listdir', return_value=[
        'holidays.be-BY.rc',
        'holidays.cs-CZ.rc',
        'holidays.da-DK.rc',
        'holidays.de-AT.rc',
        'holidays.de-BE.rc',
        'holidays.de-CH.rc'
    ]):
        ps = rc_paths()
        assert ps[0] == 'holidays.be-BY.rc'
