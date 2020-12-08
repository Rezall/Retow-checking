import csv
import datetime
import pandas as pd
import os 


#Importing file
"""
try:
    read_file = pd.read_excel (r'workinstruction.xls')
    read_file.to_csv (r'workinstruction.csv', index = None, header=True)
except:
    print("here")
"""
#Importing and Parsing file
parsed_wi = []

try :
    with open('workinstruction.csv', newline='') as csv_file:
        output = csv.reader(csv_file, delimiter=',')
        for x in output:
            if x[0] != "91N050N":
                continue
            else:
                parsed_wi.append(x)
except :
    print("error loading file")
    exit()

#Report creation
reslt = []

for i in range(len(parsed_wi)):
    if i not in reslt:
        for j in range(i+1, len(parsed_wi)):
            if parsed_wi[i][1] == parsed_wi[j][1]:
                i_date = datetime.datetime.strptime(parsed_wi[i][2], '%d-%b-%y %H%M ')
                j_date = datetime.datetime.strptime(parsed_wi[j][2], '%d-%b-%y %H%M ')
                if i_date > j_date and str(parsed_wi[i][3]) == "Discharge" or i_date < j_date and str(parsed_wi[i][3]) == "Load": 
                    reslt.append(parsed_wi[j][1])

#Report Output
print("Connections Report:")
print("-------------------")

if len(reslt) > 0:
    print("connections errors for : ")
    for x in reslt:
        print(x)
else:
    print("no restow connection errors found")
