from __future__ import (absolute_import, unicode_literals,
                        division, print_function)

from future.builtins import *


class CloudFlareError(Exception):
    def __init__(self, code, message):
        super().__init__()
        self.code = code
        self.message = message

    def __int__(self):
        return self.code

    def __str__(self):
        return self.message


class CloudFlareAPIError(CloudFlareError):
    pass


class CloudFlareInternalError(CloudFlareError):
    pass
