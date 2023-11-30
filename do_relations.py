import numpy as np


def is_reflexive(r):
    reflexive = True
    for i in range(0, len(r)):
        if reflexive is False:
            return reflexive
        for j in range(0, len(r[0])):
            if i == j and r[i][j] != 1:
                reflexive = False
                break
            else:
                reflexive = True
    return reflexive


def is_irreflexive(r):
    irreflexive = True
    for i in range(0, len(r)):
        if irreflexive is False:
            return irreflexive
        for j in range(0, len(r[0])):
            if i == j and r[i][j] != 0:
                irreflexive = False
                break
            else:
                reflexive = True
    return irreflexive


def is_symmetric(r):
    symmetric = False
    rt = np.empty((len(r), len(r[0])))
    for i in range(0, len(r)):
        for j in range(0, len(r[0])):
            rt[j][i] = r[i][j]
    if np.array_equal(rt, r):
        symmetric = True
    return symmetric


def is_antisymmetric(r):
    antisymmetric = True
    for i in range(0, len(r)):
        for j in range(0, len(r[0])):
            if r[i][j] == r[j][i] == 1 and i != j:
                antisymmetric = False
    return antisymmetric


def is_transitive(r):
    transitive = True
    c = 0
    for i in range(len(r)):
        for j in range(len(r[0])):
            for k in range(len(r[0])):
                if r[i][j] == 1 and r[j][k] == 1 and r[i][k] != 1:
                    transitive = False
                elif r[i][j] == 0:
                    c += 1
    if c == len(r) ** 2:
        transitive = False
    return transitive


def make_reflective(r):
    for i in range(len(r)):
        for j in range(len(r[0])):
            if i == j and r[i][j] != 1:
                r[i][j] = 1
    return r


def make_symmetric(r):
    for i in range(len(r)):
        for j in range(len(r[0])):
            if r[i][j] == 1 and r[j][i] != 1:
                r[j][i] = 1
    return r


def make_transitive(r):
    for i in range(len(r)):
        for j in range(len(r[0])):
            for k in range(len(r[0])):
                if r[i][j] == 1 and r[j][k] == 1 and r[i][k] != 1:
                    r[i][k] = 1
    return r


def power(r, p):
    if p <= 1:
        return r
    for i in range(0, len(r)):
        for j in range(0, len(r[0])):
            for k in range(0, len(r[0])):
                if r[i][j] != 0 and r[j][k] != 0:
                    r[i][j] = 2
                    r[i][k] = 1
    for i in range(0, len(r)):
        for j in range(0, len(r[0])):
            if r[i][j] == 2:
                r[i][j] = 0
    p -= 1
    if p == 1:
        return r
    else:
        return power(r, p)
