from flask import Blueprint, jsonify, Response, request
from api.controllers.v1.getdb import *
from os import listdir

api = Blueprint("api", __name__)

# Account: account name, before slash in repo identification on dolthub
# Repo: repository name, after slash in repo identification on dolthub
# Arg: table type, select from all - view all tables, base - view base tables, system - view system tables
@api.route("/<account>/<repo>/tables/<arg>", methods=["GET"])
def get_allTables(account, repo, arg):
    fullRepo = account + "/" + repo
    if arg == "all":
        return Response(getAllTables(fullRepo), mimetype="application/json"), 200
    elif arg == "base":
        return Response(getBaseTables(fullRepo), mimetype="application/json"), 200
    elif arg == "system":
        return Response(getSystemTables(fullRepo), mimetype="application/json"), 200
    else:
        return jsonify({"Error" : { "Code": 400, "Message": "Invalid Final Param: Final param 'arg' must be equal to either 'all', 'base' or 'system'"}}), 400

# Account: account name, before slash in repo identification on dolthub
# Repo: repository name, after slash in repo identification on dolthub
# Request Body: The request body for this should be json with a single parameter named 'query' that equates to a valid MySQL SELECT statement
@api.route("/<account>/<repo>/select", methods=["GET"])
def get_selectQuery(account, repo):
    fullRepo = account + "/" + repo
    requestJson = request.get_json()
    if requestJson['query']:
        return Response(getDataFromQuery(fullRepo, requestJson['query']), mimetype="application/json"), 200
    elif len(requestJson.keys()) != 1:
        return jsonify({"Error" : { "Code": 400, "Message": "Invalid Number of Arguments: Request body must only contain 'query' and no other fields"}}), 400
    elif not requestJson['query']:
        return jsonify({"Error" : { "Code": 400, "Message": "Invalid Arguments: Request body does not contain 'query'"}}), 400
    else:
        return jsonify({"Error" : { "Code": 400, "Message": "Error: Other"}}), 400