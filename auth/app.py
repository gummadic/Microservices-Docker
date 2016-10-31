#!/usr/bin/python3
from flask import Flask, request, json, Response, render_template
from MongoDao import MongoDao
from bson import json_util
import os

app = Flask(__name__)
logger = app.logger
dao = MongoDao(
    os.environ['DB_1_PORT_27017_TCP_ADDR']);

@app.route('/create')
def create_user():
    logger.debug("Create User");
    email = request.args.get('email');
    key = request.args.get('key');
    secret = request.args.get('secret');
    result = dao.new(key, secret, email);
    if result:
        return Response(json_util.dumps({"User Details":result}), status=201);
    else:
        return Response(status=401);


@app.route("/token")
def token():
    logger.debug("Get Token");
    key = request.args.get('key');
    secret = request.args.get('secret');
    result = dao.authenticateClient(key, secret);
    if result:
        return Response(json_util.dumps({"token":result}), status=201);
    else:
        return Response(status=401);

@app.route("/health")
def health():
    logger.debug("Get Health");
    return json.jsonify(healthy='true');

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
