import os
import re
import datetime

from typing import List

rc_file_format = re.compile(r'holidays\.(\w{2})-([A-Z]{2})\.rc')
date_line = re.compile(r'holiday\.(\w{2})-([A-Z]{2})(\d{1,2})\.date=(\d{8})')
name_line = re.compile(r'holiday\.(\w{2})-([A-Z]{2})(\d{1,2})\.name=(.+$)')

rc_locs = [
    '/usr/share/taskwarrior',
    # other platforms
]


def rc_paths() -> List[str]:
    return os.listdir(rc_locs[0])



class RCParser:


    def __init__(self, f: str) -> None:
        self.rc_file = f
        self.language = ""
        self.country = ""
        self.holidays: dict = {}
        self._parse()

    def _parse(self) -> None:

        main_data_matched = False

        with open(self.rc_file, 'r') as f:
            lines = f.readlines()
            for x in lines:
                n_match = re.match(name_line, x.strip())
                if n_match:
                    if not main_data_matched:
                        self.language = n_match.group(1)
                        self.country = n_match.group(2)
                        hol = n_match.group(4)
                        main_data_matched = True
                        continue
                    else:
                        hol = n_match.group(4)
                        continue
                d_match = re.match(date_line, x.strip())
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
