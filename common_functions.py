import os
from datetime import datetime


def read_start_trace():
    return datetime.strptime(open('start-trace.txt', 'r').read(), '%Y-%m-%d %H:%M:%S.%f')


def update_git():
    os.system("git add . > /dev/null")
    os.system("git commit -m \"Aggiornamento bash;\" > /dev/null")
    os.system("git push > /dev/null")
