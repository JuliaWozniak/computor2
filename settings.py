from variable import Env


def init():
    global env
    global opstr
    env = Env()
    opstr = '+-/*^%'
