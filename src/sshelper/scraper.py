import lxml.html as html
import requests


class SimpleScraper:
    def __init__(self):
        self._http_session = None

    def configs(self):
        raise NotImplementedError

    def run(self, *args):
        raise NotImplementedError

    @property
    def http_session(self):
        if not self._http_session:
            self._http_session = requests.Session()
        return self._http_session

    def get_tree(self, url):
        response = self.http_session.get(url)
        response.raise_for_status()
        if response.ok:
            return html.fromstring(response.text)
