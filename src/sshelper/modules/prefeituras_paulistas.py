import os

from sshelper.scraper import SimpleScraper
from sshelper.util import remove_http_protocol

from dynaconf import settings


os.environ['ENV_FOR_DYNACONF'] = 'prefeituras_paulistas'


class PrefeiturasPaulistasScraper(SimpleScraper):
    def configs(self):
        print(f"SITES_URL = '{settings.SITES_URL}'")

    def run(self, args):
        tree = self.get_tree(settings.SITES_URL)
        elements = tree.xpath("//div[@class='alphabetic-glossary']/ul/li/ul/li/a")
        links = self.get_links(elements, args.keep_protocol)

        if args.show_names:
            names = [el.text for el in elements]
            print('\n'.join([f'{name.strip()},{link}' for name, link in zip(names, links)]))
        else:
            print('\n'.join(links))

    def get_links(self, elements, keep_protocol):
        links = [el.get('href') for el in elements]
        if not keep_protocol:
            links = self.remove_links_protocol(links)
        return links

    def remove_links_protocol(self, links):
        http_mark = '://'
        return [remove_http_protocol(link) for link in links]
