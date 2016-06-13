#!/usr/bin/env python

from __future__ import (absolute_import, unicode_literals,
                        division, print_function)

import sys

from .cli4 import cli4


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    cli4(args)

if __name__ == '__main__':
    main()
