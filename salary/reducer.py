#!/usr/bin/python
import sys

agency_salary_sum = 0
current_agency = {}
n_occurences = 0
previous_agency = None
for row in sys.stdin:
    data_mapped = row.strip().split("\t")

    if len(data_mapped) != 2:
    # Something has gone wrong. Skip this line.
        continue
    agency, salary = data_mapped
    try: salary = float(salary)
    except: continue
    if agency not in current_agency:
        current_agency[agency] = []
        current_agency[agency].append(salary)
        if previous_agency != None:
            print '{0}\t{1}'.format(previous_agency, sum(current_agency[previous_agency])/len(current_agency[previous_agency]))
    else:
        current_agency[agency].append(salary)
        previous_agency = agency
