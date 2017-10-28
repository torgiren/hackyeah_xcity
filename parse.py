#!/usr/bin/env python3
import csv
import re
e = []
def prepare(s):
    return s.lower().translate(str.maketrans("ęóąśłżźćńö","eoaslzzcno")).replace('  ', ' ').strip()

def ulica_prepare(s):
    return re.sub("o;", "o", re.sub("^(ulica|ul\.|al\.|os.|aleja|al\.|osiedle|ks\.|.\.|prez\.)\s", "", s))

def numer_prepare(s):
    return re.sub(" ", "", s)
#    return s.replace("ulica", "").replace("al.","").replace("gen.","").replace("aleja", "").replace("os. ","").replace("osiedle ","").strip()

with open("slownik.csv", "r") as f:
    ulice = [(prepare(x[5]),numer_prepare(prepare(x[1]))) for x in csv.reader(f, delimiter=";")]

with open("dane.csv", "r") as f:
    dane = [(ulica_prepare(prepare(x[1])), numer_prepare(prepare(x[2]))) for x in csv.reader(f, delimiter=";")]


for d in dane:
    match = False
    debug = []
    debug.append("d: {a} {b}".format(a=d[0], b=d[1])) 
    #print("d:", d[0], d[1]) 
    for s in ulice:
        debug.append("s:{a} {b}".format(a=s[0], b=s[1]))
        #print("s:", s[0], s[1])
        if (s[1] == d[1] and (s[0] in d[0])):
            debug.append("match")
            #print("match")
            match = True
            break
    debug.append("--- {a}".format(a=match))
    #print("---", match)
    if not match:
        print("\n".join(debug))
