"""Exports a WSGI application that can be used to host the application by 1)
   Passenger, when imported into *passenger_wsgi.py* (for example), or 2) a
   CherryPy instance when this file is invoked directly.
"""

import os
import sys
import flask
from gevent import pywsgi

MOD_ROOT, _ = os.path.split(os.path.abspath(__file__))
_, MOD_NAME = os.path.split(MOD_ROOT)
application = flask.Flask(MOD_NAME)

@flask.route("/")
def index():
    """
    """
    return flask.send_file(MOD_ROOT + "/public/index.html")

@flask.route("/<path:path>")
def public():
    """
    """
    return flask.send_from_directory(MOD_ROOT + "/public", path)
    
@flask.route("/test")
def test(self):
    """
    """
    return "This is a test"

def main():
    """
    """
    address = ("127.0.0.1", 8765)
    print("Starting %s client at %s:%u" % (MOD_NAME, address[0], address[1]))
    pywsgi.WSGIServer(address, application).serve_forever()

if __name__ == "__main__":
    main()

