import math 

def score(x, y):
    r = math.sqrt(x*x + y*y)

    if r > 10:
        score = 0
    elif r > 5:
        score = 1
    elif r > 1:
        score = 5
    else:
        score = 10

    return score


print(score(-1,1))