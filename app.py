from flask import Flask, request, json
import requests
import socket


app = Flask(__name__)

@app.route("/")
def index():
    hostname = socket.gethostname()

    str = f"Request:\n  Hostname: {hostname}\n"
    for h in request.headers.keys():
        str += f"  {h}: {request.headers[h]}\n"

    return str


@app.route("/post", methods=['POST'])
def repost():
    data = json.loads(request.data)
    x = requests.get(data["url"])

    str = "Response:\n"
    for h in x.headers.keys():
        str += f"  {h}: {x.headers[h]}\n"

    return f"{x.text}\n{str}"