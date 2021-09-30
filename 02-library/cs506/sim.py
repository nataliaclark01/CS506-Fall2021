import math

def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    summation = 0
    for ind in range(len(x)):
        summation += abs(x[ind]-y[ind])
    return summation

def jaccard_dist(x, y):
    card_intersection = len(list(set(x).intersection(y)))
    card_union = (len(x) + len(y)) - card_intersection
    return card_intersection / card_union
    

def cosine_sim(x, y):
    return 1 - math.cos(x, y)

# Feel free to add more
