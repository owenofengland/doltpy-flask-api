from doltpy.cli.read import read_pandas_sql
from api.helpers.getrepo import getRepo
import pandas as pd

def getBaseTables(repo: str, branch: str):
    query = '''SELECT * FROM information_schema.tables WHERE table_type = "BASE_TABLE"'''
    repo = getRepo(repo, branch)
    result = read_pandas_sql(repo, query)
    return result.to_json()

def getSystemTables(repo: str, branch: str):
    query = '''SELECT * FROM information_schema.tables WHERE table_type = "SYSTEM VIEW"'''
    repo = getRepo(repo, branch)
    result = read_pandas_sql(repo, query)
    return result.to_json()

def getAllTables(repo: str, branch: str):
    query = '''SELECT * FROM information_schema.tables'''
    repo = getRepo(repo, branch)
    result = read_pandas_sql(repo, query)
    return result.to_json()

def getDataFromQuery(repo: str, branch: str, query: str):
    if query.split(' ')[0] == 'SELECT':
        repo = getRepo(repo, branch)
        result = read_pandas_sql(repo, query)
        return result.to_json()
    else:
        return None