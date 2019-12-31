from argparse import ArgumentParser
from sshelper.modules.prefeituras_paulistas import PrefeiturasPaulistasScraper


__modules = {
    'pref-paulistas': PrefeiturasPaulistasScraper
}


def setup_prefpaulistas_argparser(subparsers):
    parser = subparsers.add_parser('pref-paulistas')
    parser.add_argument('--show-names', dest='show_names', action='store_true')
    parser.add_argument('--keep-protocol', dest='keep_protocol', action='store_true')


def run(args):
    c = __modules[args.module]()
    c.run(args)


if __name__ == '__main__':
    parser = ArgumentParser(description="Simple Scraper Runner")
    
    subparsers = parser.add_subparsers(dest='module')

    setup_prefpaulistas_argparser(subparsers)
    
    args = parser.parse_args()

    run(args)
