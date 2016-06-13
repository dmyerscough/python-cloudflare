from __future__ import (absolute_import, unicode_literals,
                        division, print_function)

from future import standard_library
standard_library.install_aliases()

import os
import re
import configparser


def read_configs():
    # envioronment variables override config files
    email = os.getenv('CF_API_EMAIL')
    token = os.getenv('CF_API_KEY')
    certtoken = os.getenv('CF_API_CERTKEY')

    # grab values from config files
    config = configparser.RawConfigParser()
    config.read(['.cloudflare.cfg',
                 os.path.expanduser('~/.cloudflare.cfg'),
                 os.path.expanduser('~/.cloudflare/cloudflare.cfg')])

    if email is None:
        try:
            email = re.sub(r"\s+", '', config.get('CloudFlare', 'email'))
        except Exception:
            email = None

    if token is None:
        try:
            token = re.sub(r"\s+", '', config.get('CloudFlare', 'token'))
        except Exception:
            token = None

    if certtoken is None:
        try:
            certtoken = re.sub(r"\s+", '',
                               config.get('CloudFlare', 'certtoken'))
        except Exception:
            certtoken = None

    try:
        extras = re.sub(r"\s+", ' ',
                        config.get('CloudFlare', 'extras'))
    except Exception:
        extras = None

    try:
        extras = extras.split(' ')
    except AttributeError:
        extras = []

    return [email, token, certtoken, extras]
