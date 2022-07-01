import os
import logging


def create_branch(repository, branch):
    logging.info("[BRANCH] checking")
    pid = os.fork()
    if pid == 0:
        os.execlp("git", "create branch", "checkout", "-b", branch, repository + "/" + branch)
    os.wait4(pid, 0)
    logging.info("[BRANCH FINISHED]")
    return 0


def pull(repository, branch, nocommit=False, rebase=False):
    logging.info("[PULL] pulling %s/%s" % (repository, branch))
    pid = os.fork()
    if pid == 0:
        os.execlp("git", "pulling", "pull", "--rebase" if rebase else "--no-rebase", repository, branch,
                "--allow-unrelated-histories", "--no-commit" if nocommit else "--commit")
    os.wait4(pid, 0)
    logging.info("[PULL FINISHED]")
    return 0


def push(repository, branch):
    logging.info("[PUSH] pushing %s/%s" % (repository, branch))
    pid = os.fork()
    if pid == 0:
        os.execlp("git", "pushing", "push", repository, branch, "--force")
    os.wait4(pid, 0)
    logging.info("[PUSH FINISHED]")
    return 0


def remote_add(name, remoterep):
    logging.info("[REMOTE ADD] adding")
    pid = os.fork()
    if pid == 0:
        os.execlp("git", "adding", "remote", "add", name, remoterep)
    os.wait()
    logging.info("[REMOTE ADD FINISHED]")
    return 0


def git_init(branch):
    logging.info("[INIT] initing")
    pid = os.fork()
    if pid == 0:
        os.execlp("git", "initing", "init")
    os.wait4(pid, 0)
    pid = os.fork()
    if pid == 0:
        os.execlp("git", "passwording", "branch", "-m", branch)
    os.wait4(pid, 0)
    logging.info("[INIT FINISHED]")
    return 0


def get_fetch():
    pid = os.fork()
    if pid == 0:
        os.execlp("git", "fetching", "fetch", "--all")
    os.wait4(pid, 0)
    return 0


def change_user(repository, branch, name, email):
    pid = os.fork()
    if pid == 0:
        os.execlp("git", "changing", "commit", "--amend", "--author", "{} <{}>".format(name, email), "--no-edit")
    os.wait4(pid, 0)

    pid = os.fork()
    if pid == 0:
        os.execlp("git", "changing", "replace", branch, repository + "/" + branch)
    os.wait4(pid, 0)
    return 0


def change_userV2(email):
    pid = os.fork()
    if pid == 0:
        os.execlp("git", "config", "config", "--local", "user.email", email)
    os.wait4(pid, 0)
    return 0


def git_add_all():
    pid = os.fork()
    if pid == 0:
        os.execlp("git", "adding", "add", ".")
    os.wait4(pid, 0)
    return 0


def commit(msg, author):
    pid = os.fork()
    print("hello world")
    if pid == 0:
        os.execlp("git", "commiting", "commit", "-am", msg, "--author", f"Jhon Doe <{author}>")
    os.wait4(pid, 0)
    return 0


