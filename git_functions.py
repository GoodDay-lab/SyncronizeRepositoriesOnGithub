import os
import logging


def pull(repository, branch):
    logging.info("[PULL] pulling %s/%s" % (repository, branch))
    pid = os.fork()
    if pid == 0:
        os.execlp("git", "pulling", "pull", "--no-rebase", repository, branch)
    os.wait4(pid, 0)
    logging.info("[PULL FINISHED]")
    return 0


def push(repository, branch):
    logging.info("[PUSH] pushing %s/%s" % (repository, branch))
    pid = os.fork()
    if pid == 0:
        os.execlp("git", "pushing", "push", repository, branch + ":" + branch)
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


def git_init():
    logging.info("[INIT] initing")
    pid = os.fork()
    if pid == 0:
        os.execlp("git", "initing", "init")
    pid = os.fork()
    if pid == 0:
        os.execlp("git", "passwording", "config", "--local", "credential.useHttpPath", "true")
    os.wait4(pid, 0)
    logging.info("[INIT FINISHED]")
    return 0
