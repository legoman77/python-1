"""These are my personal quiz questions."""

import colors as c
from utils import ask

intro = ("Prepare thyself!")

def q1():
    answer = ask("Am I a taco?")
    if answer == "yes":
        return True
    return False

def q2():
    answer = ask("How many Mr. Fluffys have I killed?")
    if answer ==  ("ten"):
        return True
    return False

def q3():
    answer = ask("Can I do a Falcon Punch?")
    if answer == ("i wish"):
        return True
    return False
    
questions = [q1,q2,q3]
