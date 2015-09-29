#!/usr/bin/env python

from flask import Flask
import socket, redis, os


host = os.getenv("REDIS_PORT_6379_TCP_ADDR")
port = os.getenv("REDIS_PORT_6379_TCP_PORT")

r = redis.Redis(host, port)
r.set("count", 0)

app = Flask(__name__)

@app.route("/")
def index():
  r.incr("count")
  count = int(r.get("count"))
  name = socket.gethostname()
  return "Visit number {0}\nHostname: {1}\n".format(count, name)

if __name__ == "__main__":
  app.run(host="0.0.0.0")
