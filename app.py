from flask import Flask, request


app = Flask(__name__)

@app.route("/")
def hello():
    fdid = request.headers.get('x-azure-fdid')
    return f"Hello, World! This is my first azure webapp: {fdid}"
