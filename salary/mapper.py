#!/usr/bin/python
import sys

for line in sys.stdin:
#    print line.split(',')
#    break
# Get the words in each line
    rowdata = line.split(',')
# Generate the count for each word
    agency = rowdata[4]
    try:
        annualSalary = float(rowdata[6].strip())
    except:
        continue
    print '{0}\t{1}'.format(agency, annualSalary)
