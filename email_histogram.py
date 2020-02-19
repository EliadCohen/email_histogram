#!/usr/bin/env python
import re
#generate_froms_array reads a file and picks lines where the word "From" starts the string
def generate_froms_array(filename="mbox-short.txt"):
    email_file=open(filename,"r")
    all_lines=email_file.readlines()
    email_file.close()
    froms=[]
    for line in all_lines:
        if line.startswith("From "):
            froms.append(line)
    return froms

def generate_time_array(froms):
    times=[]
    regex=re.compile(r'([01]?[0-9]|2[0-3]):[0-5][0-9]')

    for entry in froms:
        match=regex.findall(entry)
        times.append(match[0])
    return times
    
def generate_histogram_list(bins,time_array):
    hist={}
    for bin in bins:
        hist[bin]=time_array.count(bin)
    return hist

filename="mbox-short.txt"
froms_list=generate_froms_array(filename) 
#print(froms_list)
time_array=generate_time_array(froms_list)
bins=set(time_array)
histogram=generate_histogram_list(bins,time_array)
