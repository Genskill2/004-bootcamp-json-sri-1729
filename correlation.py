# Add the functions in this file
import json

def load_journal(x):
    page = open(x)
    return json.load(page)

def compute_phi(x, event):
    journ = load_journal(x)
    table = [0, 0, 0, 0] # 0 -> nosq,noev 1 -> nosq,ev 2 -> sq, noev 3 -> sq, ev
    for day in journ:
        index = 0
        if event in day['events']:
            index += 1
        if day['squirrel']:
            index += 2
        table[index] += 1
    n1t = table[1] + table[3]
    n2t = table[2] + table[3]
    n1f = table[0] + table[2]
    n2f = table[0] + table[1]
    phi = (table[3] * table[0] - table[2]*table[1]) / (n1t * n2t * n1f * n2f)**0.5
    return phi

def compute_correlations(x):
    journ = load_journal(x)
    evs = []
    res = {}
    for day in journ:
        for event in day['events']:
            if not event in evs:
                evs.append(event)
    for event in evs:
        res[event] = compute_phi(x, event)
    return res

def diagnose(x):
    ans = compute_correlations(x)
    mi = 1
    ma = -1
    for ev, cor in ans.items():
        if cor < mi:
            mi = cor
            evmi = ev
        if cor > ma:
            ma = cor
            evma = ev
    return evma, evmi

