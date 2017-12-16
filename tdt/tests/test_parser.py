def test_file_presence(holiday_rc_file):
    with open(holiday_rc_file, 'r') as f:
        line = f.readline()
        assert line[0] == '#'
