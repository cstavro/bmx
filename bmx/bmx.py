#!/usr/bin/python3

import sys
import argparse

from . import bmxaws
from . import bmxwrite
from . import bmxprint

class Parser:
    def __init__(self):

        parser = argparse.ArgumentParser(
            add_help=False,
            description='Okta time-out helper for AWS CLI',
            epilog='Copyright 2017 D2L Corporation')

        subparsers = parser.add_subparsers(title='commands')
        aws_parser = subparsers.add_parser('aws',
            help='awscli with automatic STS token renewal',
            add_help=False)
        aws_parser.set_defaults(func=self.aws)

        write_parser = subparsers.add_parser('write',
            help='write default credentials',
            add_help=False)
        write_parser.set_defaults(func=self.write)

        print_parser = subparsers.add_parser('print',
            help='write default credentials and print to console',
            add_help=False)
        print_parser.set_defaults(func=self.print)

        self._parser = parser

    def aws(self, unknown_args):
        return bmxaws.cmd(unknown_args)

    def write(self, unknown_args):
        return bmxwrite.cmd(unknown_args)

    def print(self, unknown_args):
        return bmxprint.cmd(unknown_args)

    def parse_args(self, args):
        return self._parser.parse_known_args(args)

    def usage(self):
        return self._parser.format_help()

def main():
    argv = sys.argv
    parser = Parser()
    if len(argv) == 1:
        print(parser.usage())
        return 1

    [known_args, unknown_args] = parser.parse_args(argv[1:])
    if 'func' in known_args:
        return known_args.func(unknown_args)

    print(parser.usage())
    return 1

if __name__ == "__main__":
    sys.exit(main())
