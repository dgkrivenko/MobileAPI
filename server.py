import sys, os

# Add a custom Python path.
sys.path.insert(0, "/home/sitename.ru")

# Switch to the directory of your project. (Optional.)
# os.chdir("/home/uXXXXX/sitename.ru")

from flup.server.fcgi import WSGIServer
from auth import app

if __name__ == '__main__':
    WSGIServer(app).run()