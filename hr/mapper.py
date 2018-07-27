#!/usr/bin/python

import sys

for line in sys.stdin:
    rowdata = line.split(',')
    # Below we calculated effectiveness index of an employee. It is simply
    # the number of project multiplied by the number of years worked at the
    # company and dividing the total number of hours worked on average.
    # The resulting values were too small so we multiplied by 10000

    clean_element = rowdata[-1].replace('\r\n', '')
    rowdata[-1] = clean_element
    try:
        effectiveness = float(rowdata[2])/(float(rowdata[4])*float(rowdata[3]))*10000 #effectiveness index
    except:
        continue

    print ('{0}\t{1}\t{2}'.format(rowdata[8], rowdata[9], effectiveness))


