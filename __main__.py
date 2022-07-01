from flask import Flask
from flask import request
from git_functions import *
import logging
import argparse
import os
import json


cmdargs = None
remotes = []
branches = []
scriptpath = os.path.abspath(os.curdir)

logging.basicConfig(level=logging.INFO)


def cmdline(line):
    pid = os.fork()
    if pid == 0:
        cmd = line.split()
        cmd.insert(1, cmd[0])
        os.execlp(*cmd)
    os.wait4(pid, 0)
    return 0


def create_secure_url(url, username, password):
    ind = url.find("://") + 3
    return url[:ind] + username + ":" + password + "@" + url[ind:]


def get_repository_name(url):
    return os.path.splitext(os.path.split(url)[-1])[0]


def init():
    global cmdargs, remotes, branches

    parser = argparse.ArgumentParser()
    parser.add_argument("--localrepo", default="./localrepo")
    parser.add_argument("--replist")
    parser.add_argument("--username")
    parser.add_argument("--password")
    parser.add_argument("--host", default="localhost")
    parser.add_argument("--port", default=9999, type=int)
    args = parser.parse_args()
    cmdargs = args

    # Creaing local repo
    if os.path.exists(cmdargs.localrepo):
        logging.warn("dir '%s' already exists!" % cmdargs.localrepo)
        exit(1)
    os.mkdir(cmdargs.localrepo)

    # Parsing 'replist' file
    number = 1
    with open(cmdargs.replist, "r") as src:
        for line in src:
            url, branch, user, *_ = line.split()
            name = "repo_" + str(number)
            number += 1
            remotes.append({
                    "url": url,
                    "name": name,
                    "branch": branch,
                    "email": user
                })
            branches.append(branch)

    try:
        os.chdir(cmdargs.localrepo)
        git_init(branch)

        # Uniting remote repostories into local repo
            
        for remote in remotes:
            remote_add(remote.get('name'), remote.get('url')) 
            pull(remote.get('name'), remote.get('branch'))

        for remote in remotes:
            push(remote.get('name'), remote.get('branch'))
    finally:
        os.chdir(scriptpath)


def close():
    # Deleting an repo
    for root, dirs, files in os.walk(cmdargs.localrepo, topdown=False):
        for file in files:
            os.remove(os.path.join(root, file))
        for direct in dirs:
            os.rmdir(os.path.join(root, direct))
    os.rmdir(cmdargs.localrepo)


def main():
    app = Flask("Syncronizer")

    @app.route("/", methods=["POST"])
    def general():
        payload = json.loads(request.form.to_dict()['payload'])

        if request.headers['X-GitHub-Event'] == 'push':
            repository = None
            flag_in = False
            for rep in remotes:
                flag_in = get_repository_name(rep['url']) == payload['repository']['name'] or flag_in
                if flag_in:
                    repository = rep
                    break
            if not flag_in: return "error"
            
            try:
                os.chdir(cmdargs.localrepo) 
                pull(repository.get('name'), repository.get('branch'), nocommit=True)
                for remote in remotes:
                    if remote == repository: continue
                    change_user(remote['name'], remote['branch'], "Good", remote['email'])
                    pull(remote['name'], remote['branch'], nocommit=True, rebase=True)
                    commit(payload['commits'][0]['message'], remote['email'])
                    if remote['branch'] in branches:
                        push(remote['name'], remote['branch'])
            finally:
                os.chdir(scriptpath)
        return "Error"

    app.run(host=cmdargs.host, port=cmdargs.port)


if __name__ == '__main__':
    try:
        init()
        main()
    finally:
        close()
