#!/usr/bin/python3

import sys

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

host = ""

def main():

    user = sys.argv[1]
    password = sys.argv[2]
    home_dir = sys.argv[3]

    authorizer = DummyAuthorizer()
    #authorizer.add_user(user, password, home_dir, perm="elradfmw")
    authorizer.add_anonymous(".", perm="elradfmw")

    handler = FTPHandler
    handler.authorizer = authorizer

    server = FTPServer((host, 21), handler)
    server.serve_forever()

    return

def usage():
    usage = "python3 {} {{user}} {{password}} {{home-directory}}".format(sys.argv[0])
    return usage

if __name__ == '__main__':
    if len(sys.argv) == 4:
        main()
    else:
        print(usage())
