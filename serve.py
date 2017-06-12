#!/usr/bin/env python
from livereload import Server

server = Server()
server.watch('designing-pythonic-apis.ipynb', 'jupyter-nbconvert --to slides --stdout designing-pythonic-apis.ipynb >! index.html')
server.serve(liveport=35729)
