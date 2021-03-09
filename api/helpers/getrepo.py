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