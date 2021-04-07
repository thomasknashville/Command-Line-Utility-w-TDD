#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "Karen Thomas"


import sys
import argparse


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    parser = argparse.ArgumentParser('transforms input text')
    parser.add_argument('-l', '--lower',
                        help='Convert text to lowercase', action='store_true')
    parser.add_argument('-u', '--upper',
                        help='Convert text to UPPERCASE', action='store_true')
    parser.add_argument('-t', '--title',
                        help='Convert text to Title Case', action='store_true')
    parser.add_argument(
        'text', help='text to be transformed')
    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    args = parser.parse_args(args)
    text = args.text
    if args.lower:
        text = text.lower()
    if args.upper:
        text = text.upper()
    if args.title:
        text = text.title()
    print(text)


if __name__ == '__main__':
    main(sys.argv[1:])
