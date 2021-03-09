from flask import Blueprint, jsonify, Response
from api.controllers.v1.getdb import *
from os import listdir

api = Blueprint("api", __name__)

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
