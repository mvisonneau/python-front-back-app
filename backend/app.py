import os
import socket
import json
import uuid

from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/')
def hello():
    provider = str(os.environ.get('PROVIDER', 'world'))
    return 'Hello from backend ' + provider + '!'

@app.route("/generate")
def return_uuid():
    uuid_value = str(uuid.uuid4())
    return jsonify({"uuid": uuid_value})

@app.route("/hostname")
def return_hostname():
    # return "This is an example wsgi app served from {} to {}".format(socket.gethostname(), request.remote_addr)
    return jsonify({"backend hostname": socket.gethostname()})


@app.route("/version")
def return_version():
    return "version 1.26 on host {}".format(socket.gethostname())

@app.route("/headers")
def return_headers():
    return str(request.headers)

@app.route("/http_code")
def return_http_code():
    code = request.args.get('code', default = 200, type = int)
    return str(code), code

@app.route("/health")
def return_health():
    code = request.args.get('code', default = 200, type = int)
    return "Healthy", 200

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('CONTAINER_PORT', 5000))
    app.run(host='0.0.0.0', port=port)
