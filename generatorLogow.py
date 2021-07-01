#Generator logów

import datetime
import time


def log(message, dt = datetime.datetime.now()):
    print(dt, message)


def logi(*args):
    for command in args:
        log(command)
        time.sleep(1)

logi('Uruchomienie systemu', 'Logowanie', 'Restart', 'Wylogowanie')
