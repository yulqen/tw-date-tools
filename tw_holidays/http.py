import json
import requests
import io


class APIResource:
    def __init__(self, url):
        self.url = url

    def _fetch(self, url):
        return requests.get(url).text

    def get_string_io(self):
        f = self._fetch(self.url)
        return io.StringIO(f, '\n')


def parse(str_obj: io.StringIO) -> str:
    output_file = '/tmp/holidays.en-GB.rc'
    with open(output_file, 'w') as output_f:
        for x, line in list(enumerate(str_obj, start=1)):
            d = json.loads(line)
            output_f.write(f"holiday.{d['locale']}{x}.name={d['description']}\n")
            output_f.write(f"holiday.{d['locale']}{x}.date={d['date'].replace('-', '')}\n")
    return output_file
