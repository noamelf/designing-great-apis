#!/usr/bin/env python
from livereload import Server

server = Server()
server.watch('designing-great-apis.ipyb', 'jupyter-nbconvert --to slides --stdout designing-great-apis.ipynb >! index.html')
server.serve(liveport=35729)
