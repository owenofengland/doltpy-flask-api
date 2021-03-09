from doltpy.cli.read import read_pandas_sql
from api.helpers.getrepo import getRepo
import pandas as pd

def getBaseTables(repo):
    query = '''SELECT * FROM information_schema.tables WHERE table_type = "BASE_TABLE"'''
    repo = getRepo(repo)
    result = read_pandas_sql(repo, query)
    return result.to_json()

def getSystemTables(repo):
    query = '''SELECT * FROM information_schema.tables WHERE table_type = "SYSTEM VIEW"'''
    repo = getRepo(repo)
    result = read_pandas_sql(repo, query)
    return result.to_json()

def getAllTables(repo):
    query = '''SELECT * FROM information_schema.tables'''
    repo = getRepo(repo)
    result = read_pandas_sql(repo, query)
    return result.to_json()

def getDataFromQuery(repo, query):
    if query.split(' ')[0] == 'SELECT':
        repo = getRepo(repo)
        result = read_pandas_sql(repo, query)
        return result.to_json()
    else:
        return None