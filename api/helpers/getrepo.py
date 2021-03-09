from doltpy.cli import Dolt
from os import listdir

def getRepo(repoName: str):
    if repoName.split('/')[1] in listdir('./'):
        localRepoName = './' + repoName.split('/')[1]
        dolt = Dolt(localRepoName)
        dolt.pull()
    else:
        dolt = Dolt.clone(repoName)
    return dolt

# This function and branchSupportGetRepo are the beginnings of a way to run queries on specific commits and branches
def updateData(dolt: Dolt, branchName: str):
    dolt.checkout(branchName)
    dolt.pull()
    return repo

def branchSupportGetRepo(repoName: str, branchName: str):
    if repoName.split('/')[1] in listdir('./'):
        localRepoName = './' + repoName.split('/')[1]
        dolt = Dolt(localRepoName)
    else:
        dolt = Dolt.clone(repoName)
    dolt = updateData(dolt, branchName)
    return dolt
        
        