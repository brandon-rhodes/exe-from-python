import sys
def fix():
    import io
    sys.modules['StringIO'] = io
    real_StringIO = io.StringIO

    class StringIO(real_StringIO):
        def __init__(self, content):
            if isinstance(content, bytes):
                content = content.decode('ascii')
            return real_StringIO.__init__(self, content)

    io.StringIO = StringIO

    import configparser
    sys.modules['ConfigParser'] = configparser
    __builtins__['StandardError'] = Exception
    import urllib.parse
    sys.modules['urlparse'] = urllib.parse
    def cmp(a, b):
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return 0
    __builtins__['cmp'] = cmp
    import urllib.request
    sys.modules['urllib2'] = urllib.request
    import http.client
    sys.modules['httplib'] = http.client
    import queue
    sys.modules['Queue'] = queue
    import email.message
    sys.modules['rfc822'] = email.message
    import hmac
    real_HMAC = hmac.HMAC

    class HMAC(real_HMAC):
        def __init__(self, key, msg = None, digestmod = None):
            key = key.encode('ascii')
            return real_HMAC.__init__(self, key, msg, digestmod)
        def update(self, msg):
            if isinstance(msg, str):
                msg = msg.encode('ascii')
            return real_HMAC.update(self, msg)

    hmac.HMAC = HMAC

    import urllib.parse
    real_quote = urllib.parse.quote
    def quote(value):  # fix bucket.py:386
        if isinstance(value, str) and value.startswith("b'"):
            value = eval(value).decode('ascii')
        result = real_quote(value)
        return result
    urllib.quote = quote

    import base64
    real_encodestring = base64.encodestring
    def encodestring(s):
        result = real_encodestring(s)
        return result.decode('ascii')
    base64.encodestring = encodestring

fix()
del fix

#import logging
#logging.basicConfig(filename="boto.log", level=logging.DEBUG)

