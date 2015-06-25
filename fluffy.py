"""These are my pink fluffy unicorn questions."""

import colors as c
from utils import ask

intro = ("Let's test your knowledge and see what you've learned so far!")

def q1():  
    answer = ask("What color are the unicorns?") 
    if answer == "pink":
        return True
    return False
    
def q2():
    answer = ask("Where are they dancing?")
    if answer.startswith("rainbow"):
        return True
    return False

def q3():
    answer = ask("Please use one word to describe the texture of their magical fur.")
    if answer.startswith("smile"):
        return True
    return False

questions = [q1,q2,q3]
