"""Exports a WSGI application that can be used to host the application by 1)
   Passenger, when imported into *passenger_wsgi.py* (for example), or 2) a
   CherryPy instance when this file is invoked directly.
"""

import os
import csv
import sys
import random
import cherrypy

class Server(object):
    """CherryMy points can be identified in this object for non-static routing.
       *test()* is included as an example.
    """

    @cherrypy.expose
    def test(self):
        """
        """
        yield "This is a test"

# define module-level *application* symbol for Passenger WSGI mounting
application = cherrypy.Application(Server(), config={
    "/": {
        "tools.sessions.on": True
    }
})

# define scripted execution for alternate local testing mode
if __name__ == "__main__":
    cherrypy.tree.graft(application, "/")
    cherrypy.config.update({
        "global": {
            "server.socket_host": "127.0.0.1",
            "server.socket_port": 8000,
            "tools.staticdir.on": True,
            "tools.staticdir.dir": os.path.abspath("public"),
            "tools.staticdir.index": "index.html"
        }
    })
    cherrypy.engine.signals.subscribe()
    cherrypy.engine.start()
    cherrypy.engine.block()
