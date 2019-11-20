# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 09:55:08 2019

@author: MELYAAGOUBI
"""

import os

def list_files(dir):
    tab =[]
    for path, dirs, files in os.walk(dir):
        for file in files:
            #tab.append(os.path.join(path,file))
            #extension = file.split(".")[-1]
            tab.append([file])
    return tab

all_files = list_files("PGxCorpus")

#len(all_files)

def parse_txt(filename):
    path_txt = "PGxCorpus/" + str(filename[0])
    my_file = open(path_txt, "r")
    my_file_bis= my_file.read()
    parsed_txt = my_file_bis.split(" ")
    return parsed_txt


#phrase=parse_txt(all_files[1])


def parse_ann(filename):
    path_ann = "PGxCorpus/" + str(filename[0])
    my_file_ann = open(path_ann, "r")
    my_file_bis_ann= my_file_ann.read()
    
    parsed = my_file_bis_ann.split("\n")
    new_parsed =  []
    for i in range(0,len(parsed)):
        if len(parsed[i]) != 0 :
            if parsed[i][0] == 'T' and ";" not in parsed[i]:
                new_parsed.append(parsed[i])
    newer_parsed= []
    for j in range(0,len(new_parsed)): 
        chaine1 = new_parsed[j].split('\t')
        del chaine1[0]
        newer_parsed = newer_parsed + chaine1
        
    for k in range(0, len(newer_parsed), 2):
        chaine2 = newer_parsed[k].split(" ")
        newer_parsed[k] =  chaine2[0]
     
    return newer_parsed

#file_ann = parse_ann(all_files[0])

def rmv_occ(file_ann):
    final_ann=[]
    for l in range(1,len(file_ann),2):
        if " " in file_ann[l]:
            boolean=False
            for m in range(1,len(file_ann),2):
                if file_ann[m] in file_ann[l] and m!=l:
                    boolean=True
            if boolean==False:
                final_ann.append(file_ann[l].strip())
                final_ann.append(file_ann[l-1].strip())
        else:
            final_ann.append(file_ann[l].strip())
            final_ann.append(file_ann[l-1].strip())
    return final_ann


#final_ann = rmv_occ(file_ann)


def create_file(file, final_ann,phrase):
    n=0
    while n<len(phrase):
        o=0
        boolean1=True
        while o<len(final_ann) and boolean1:
            if " " in final_ann[o]:
                x=final_ann[o].split(" ")
                boolean2=True
                q=0
                while boolean2 and q<len(x):
                    
                    if x[q]==phrase[n+q]:
                        q+=1
                    else:
                        boolean2=False
                if boolean2:
                    file.write(phrase[n]+" B-"+final_ann[o+1]+"\n")
                    for z in range(1,len(x)):
                        file.write(phrase[n+z]+" I-"+final_ann[o+1]+"\n")
                    n=n+z
                    boolean1=False
            else:
                if phrase[n]==final_ann[o]:
                    file.write(phrase[n]+" B-"+final_ann[o+1]+"\n")
                    boolean1=False
            o=o+2            
        if boolean1:
            file.write(phrase[n]+" O \n")
        n+=1
    file.write("\n")
    
    
#create_file(all_files[0],final_ann,phrase)


def transf_total(tab_files):
    n =  len(tab_files)
    file = open("data_iob.tsv","w")
    file.write("-DOCSTART- O \n\n")
    
    for s in range(0,n-1,2) :
        phrase = parse_txt(all_files[s+1])
        file_ann = parse_ann(all_files[s])
        final_ann = rmv_occ(file_ann)
        create_file(file,final_ann,phrase)

    file.close()



transf_total(all_files)






