# holiday convertor for taskwarrior
#

import json

meta_data = """

###############################################################################
# International Holiday Data provided by Holidata.net
# http://holidata.net/en-GB/2015.json
# http://holidata.net/en-GB/2016.json
#
# Copyright 2006 - 2016, Paul Beckingham, Federico Hernandez.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# http://www.opensource.org/licenses/mit-license.php
#
###############################################################################
"""

input_json_file = "gb_holidays_2017.json"
output_file = "holidays.en=GB.rc"


def main():
    with open(input_json_file, 'r') as f:
        with open(output_file, 'w') as output_f:
            output_f.write(meta_data)
            for x, line in list(enumerate(f, start=1)):
                d = json.loads(line)
                output_f.write(f"holiday.{d['locale']}{x}.name={d['description']}\n")
                output_f.write(f"holiday.{d['locale']}{x}.date={d['date'].replace('-', '')}\n")


if __name__ == '__main__':
    main()

