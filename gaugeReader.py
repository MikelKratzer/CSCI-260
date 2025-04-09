import math
import csv

dataCol = 4 # column where flow data is
lineSkip = 28 # skip this number of lines in header

with open("Gauge Readings Assignment.txt", newline="") as csvfile:
    gaugeReader = csv.reader(csvfile, delimiter = '\t', quotechar = '|') 
    count = 0
    N = 0
    Sum = 0
    Sum2 = 0
    first = True
    for row in gaugeReader:
        count += 1
        if len(row) >= dataCol and count > lineSkip:
            value = float(row[dataCol])
            N += 1
            Sum += value
            Sum2 += value ** 2
            if first: 
                Max = value
                Min = value
                first = False
            if value > Max and not first:
                Max = value
            if value < Min and not first:
                Min = value
mean = Sum / N
variance = Sum2 / N - mean ** 2

print("During the period from January 1 to January 26, 2025,", N, "gauge depth readings were made.")
print("The average gauge depth was", round(mean,5) , "ft.")
print("The standard deviation was " + str(round(math.sqrt(variance), 5)) + ".")
print("The minimum gauge depth was", Min, "ft, while the maximum was", Max, "ft.")