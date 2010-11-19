'''
Created on Nov 18, 2010

@author: aloneroad
'''
from bottle import run, route, static_file

@route("/:filename#.+#")
def fake_mogstored(filename):
  return static_file(filename, "/tmp/mogilelocal")

if __name__ == "__main__":
  run(port=7500)
