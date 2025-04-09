import math
import csv # comma separated values (tsv - tab separated values)

flowCol = 4 # column where flow data is
lineSkip = 28 # skip this number of lines in header

with open("waterservices.usgs.gov.txt", newline="") as csvfile:
    gaugeReader = csv.reader(csvfile, delimiter = '\t', quotechar = '|') 
    count = 0
    N = 0
    Sum = 0
    Sum2 = 0 # squared
    Max = 0
    Min = 0
    first = True #first number seen
    for row in gaugeReader:
        # print(', '.join(row)) # replaces the delimiter (tab) with a comma
        count += 1
        if len(row) >= flowCol and count > lineSkip:
            # print(row[flowCol])
            value = float(row[flowCol])
            N += 1
            Sum += value
            Sum2+= value * value
            if first: 
                Max = value
                Min = value
                first = False # no longer first number
            if value > Max and not first:
                Max = value
            if value < Min and not first:
                Min = value
mean = Sum / N
variance = Sum2 / N - mean * mean
print("Average is", mean) # average water depth
print("Standard Deviation is", math.sqrt(variance))
print("Min is", Min)
print("Max is", Max)