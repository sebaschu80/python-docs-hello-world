from flask import Flask, request


app = Flask(__name__)

@app.route("/")
def hello():
    fdid = request.headers.get('x-azure-fdid')
    sfdid = request.headers.get('sx-azure-fdid')
    return f"x-azure-fdid: {fdid}\nsx-azure-fdid: {sfdid}\n"
