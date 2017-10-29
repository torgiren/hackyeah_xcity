#!/usr/bin/env python3
import datetime
time_start = datetime.datetime.now()
log_file = open("parse.log", "a")
log_file.write("Zaczynam prace o: {date}\n".format(date=time_start))
log_file.flush()
import csv
import re
e = []
def prepare(s):
    return s.lower().translate(str.maketrans("ęóąśłżźćńö","eoaslzzcno")).replace('  ', ' ').strip()

def ulica_prepare(s):
    return re.sub("o;", "o", re.sub("^(ulica|ul\.|al\.|os.|aleja|al\.|al|osiedle|ks\.|.\.|prez\.|gen\.|rtm\.|sw\.|dr\.|pl\.)\s", "", s))

def numer_prepare(s):
    return re.sub(" ", "", s).split("/")[0].split("-")[0]
#    return s.replace("ulica", "").replace("al.","").replace("gen.","").replace("aleja", "").replace("os. ","").replace("osiedle ","").strip()

with open("slownik.csv", "r") as f:
    ulice = [(prepare(x[5]),numer_prepare(prepare(x[1])),x[10], x[11]) for x in csv.reader(f, delimiter=";")]

log_file.write("Mam {ulice} ulic\n".format(ulice=len(ulice)))
log_file.flush()

dane = []
dane_raw = []
dane_header = None
with open("dane.csv", "r") as f:
    csv_reader = csv.reader(f, delimiter=";")
    dane_header = csv_reader.__next__()
    for row in csv_reader:
        dane_raw.append(row)
        dane.append((ulica_prepare(prepare(row[1])), numer_prepare(prepare(row[2]))))

    #dane = [(ulica_prepare(prepare(x[1])), numer_prepare(prepare(x[2]))) for x in csv.reader(f, delimiter=";")]

log_file.write("Mam {dane} danych wejsciowych\n".format(dane=len(dane)))
log_file.flush()

matched = []
not_matched = []

for d in enumerate(dane):
    match = False
#    debug = []
#    debug.append("d: {a} {b}".format(a=d[0], b=d[1])) 
    #print("d:", d[0], d[1]) 
    for s in ulice:
#        debug.append("s:{a} {b}".format(a=s[0], b=s[1]))
        #print("s:", s[0], s[1])
        if (s[1] == d[1][1] and (s[0] in d[1][0])):
#            debug.append("match")
            #print("match")
            match = True
            dane_raw[d[0]].append(s[2])
            dane_raw[d[0]].append(s[3])
            matched.append(dane_raw[d[0]])
            break
    #print("---", match)
    if not match:
#        print("\n".join(debug))
        not_matched.append(dane_raw[d[0]])

log_file.write("Matched: {match}\n".format(match=len(matched)))
log_file.write("Not matched: {not_match}\n".format(not_match=len(not_matched)))
log_file.flush()

with open("out.csv","w") as f:
    writer = csv.writer(f, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.write(dane_header+["X","Y"])
    for r in matched:
        writer.writerow(r)

with open("bad.csv","w") as f:
    writer = csv.writer(f, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.write(dane_header)
    for r in not_matched:
        writer.writerow(r)

time_stop = datetime.datetime.now()
log_file.write("Koncze prace o: {date}\n".format(date=time_start))
log_file.write("Pracowalem: {czas}\n".format(czas=time_stop-time_start))
log_file.flush()


log_file.close()
