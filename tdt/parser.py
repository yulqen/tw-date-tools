import re
import datetime


class RCParser:

    date_line = re.compile(r'holiday\.(\w{2})-([A-Z]{2})(\d{1,2})\.date=(\d{8})')
    name_line = re.compile(r'holiday\.(\w{2})-([A-Z]{2})(\d{1,2})\.name=(.+$)')

    def __init__(self, f: str) -> None:
        self.rc_file = f
        self.language = ""
        self.country = ""
        self.index = 0
        self.date = None
        self.holidays: dict = {}
        self._parse()

    def _parse(self) -> None:

        main_data_matched = False

# TODO - needs a way to amend keys because second time round, the keys
# as we have them are being overwritten obviously

        with open(self.rc_file, 'r') as f:
            lines = f.readlines()
            for x in lines:
                n_match = re.match(RCParser.name_line, x.strip())
                if n_match:
                    if not main_data_matched:
                        self.language = n_match.group(1)
                        self.country = n_match.group(2)
                        self.index = int(n_match.group(3))
#                       self.holidays[n_match.group(4)] = None
                        hol = n_match.group(4)
                        main_data_matched = True
                        continue
                    else:
#                       self.holidays[n_match.group(4)] = None
                        hol = n_match.group(4)
                        continue
                d_match = re.match(RCParser.date_line, x.strip())
                if d_match:
                    if d_match.group(4)[4:6][0] == '0':
                        _month = d_match.group(4)[5]
                    else:
                        _month = d_match.group(4)[4:6]
                    self.holidays["_".join([hol, d_match.group(4)[0:4]])] = datetime.date(
                        int(d_match.group(4)[0:4]),
                        int(_month),
                        int(d_match.group(4)[6:8])
                    )
