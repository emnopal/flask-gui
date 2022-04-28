import os
import argparse

from src import gui
from src import web
from gevent.pywsgi import WSGIServer
from dotenv import load_dotenv
load_dotenv()

parser = argparse.ArgumentParser()

parser.add_argument('-m', '--mode', default='desktop', help='App Running Mode')
parser.add_argument('-p', '--port', default=os.environ('APP_PORT'), help='App Port')
parser.add_argument('-h', '--host', default=os.environ('APP_HOST'), help='App Host')

if __name__  == '__main__':
    args = parser.parse_args()

    if args.mode.lower() == 'desktop':
        gui.ui.run()
    if args.mode.lower() == 'web':
        http_server = WSGIServer((args.host, args.port), web.app)
        http_server.serve_forever()
