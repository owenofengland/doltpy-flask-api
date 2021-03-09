from doltpy.cli import Dolt, DoltException
from os import listdir

def updateData(dolt: Dolt, branchName: str):
    try:
        print("Switch to branch", branchName)
        dolt.pull()
        return dolt
    except DoltException:
        return dolt

def getRepo(repoName: str, branchName: str):
    if repoName.split('/')[1] in listdir('./'):
        localRepoName = './' + repoName.split('/')[1]
        dolt = Dolt(localRepoName)
    else:
        dolt = Dolt.clone(repoName)
    dolt = updateData(dolt, branchName)
    return dolt
        
        