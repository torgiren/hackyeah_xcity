#!/usr/bin/env python3
import datetime
import csv
import re
import time
from multiprocessing import Process, Queue
dane = []
dane_raw = []
dane_header = None
ulice = []
log_file = open("parse.log", "a")
time_start = None
time_stop = None
matched = Queue()
not_matched = Queue()

def get_headers(filename):
    result = {}
    with open(filename, "r") as f:
        row = csv.reader(f, delimiter=";").__next__()
    for i in enumerate(row):
        result[i[1]] = i[0]
    return result
        
def prepare(s):
    return s.lower().translate(str.maketrans("ęóąśłżźćńö","eoaslzzcno")).replace('  ', ' ').strip()

def ulica_prepare(s):
    return re.sub("o;", "o", re.sub("^(ulica|ul\.|al\.|os.|aleja|al\.|al|osiedle|ks\.|.\.|prez\.|gen\.|rtm\.|sw\.|dr\.|pl\.)\s", "", s))

def numer_prepare(s):
    return re.sub(" ", "", s).split("/")[0].split("-")[0]
#    return s.replace("ulica", "").replace("al.","").replace("gen.","").replace("aleja", "").replace("os. ","").replace("osiedle ","").strip()

def process(data, offset):
    for d in enumerate(data):
        index = d[0] + offset
        match = False
        for s in ulice:
            if (s[1] == d[1][1] and (s[0] in d[1][0])):
                match = True
                dane_raw[index].append(s[2])
                dane_raw[index].append(s[3])
                matched.put(dane_raw[index])
                break
        if not match:
            not_matched.put(dane_raw[index])
    return 0

def load_slownik(filepath):
    global ulice
    with open(filepath, "r") as f:
        ulice = [(prepare(x[5]),numer_prepare(prepare(x[1])),x[10], x[11]) for x in csv.reader(f, delimiter=";")]

    log_file.write("Wczytywanie uluc: {ulice} ulic\n".format(ulice=len(ulice)))
    log_file.flush()

def load_dane(filename, street_col, number_col):
    global dane_header
    global dane_raw
    global dane
    with open(filename, "r") as f:
        csv_reader = csv.reader(f, delimiter=";")
        dane_header = csv_reader.__next__()
        for row in csv_reader:
            dane_raw.append(row)
            dane.append((ulica_prepare(prepare(row[street_col])), numer_prepare(prepare(row[number_col]))))
            #dane.append((ulica_prepare(prepare(row[1])), numer_prepare(prepare(row[2]))))

    log_file.write("Wczytywanie danych: {dane} danych wejsciowych\n".format(dane=len(dane)))
    log_file.flush()

def licz():
    time_start = datetime.datetime.now()
    log_file.write("Zaczynam prace o: {date}\n".format(date=time_start))
    log_file.flush()
    
    l = len(dane)
    threads_num = 8
    split_num = round(l/threads_num + 0.5)
    threads = []
    
    #import threading
    for i in range(threads_num):
        print(i*split_num, (i+1)*split_num)
        t = Process(target=process, args=(dane[i*split_num:(i+1)*split_num],i*split_num))
        t.start()
        threads.append(t)
    
    matched_list = []
    not_matched_list = []
    
    allExited = False
    while not allExited:
        while not matched.empty():
            matched_list.append(matched.get())
        while not not_matched.empty():
            not_matched_list.append(not_matched.get())
        allExited = True
        for i in threads:
            print(i.exitcode)
            if i.exitcode is None:
                allExited = False
        time.sleep(1)
    
    
    
    log_file.write("Matched: {match}\n".format(match=len(matched_list)))
    log_file.write("Not matched: {not_match}\n".format(not_match=len(not_matched_list)))
    log_file.flush()
    
    with open("out.csv","w") as f:
        writer = csv.writer(f, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(dane_header+["X","Y"])
        for r in matched_list:
            writer.writerow(r)
    
    with open("bad.csv","w") as f:
        writer = csv.writer(f, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(dane_header)
        for r in not_matched_list:
            writer.writerow(r)
    
    time_stop = datetime.datetime.now()
    log_file.write("Koncze prace o: {date}\n".format(date=time_stop))
    log_file.write("Pracowalem: {czas}\n".format(czas=time_stop-time_start))
    log_file.flush()
    
    log_file.close()

def main():
    load_slownik("slownik.csv")
    load_dane("dane.csv", 1, 2)
    licz()

if __name__ == "__main__":
    main()
