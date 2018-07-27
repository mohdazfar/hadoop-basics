import sys
from collections import defaultdict

data = defaultdict(dict)

for row in sys.stdin:
    data_mapped = row.strip().split("\t")
    if len(data_mapped) != 3:
        continue # If len != 3 then somethings went wrong in the line so skip it

    department, salary_type, effectiveness = data_mapped
    try:
        effectiveness = float(effectiveness)
    except:
        continue

    try:
        data[department][salary_type].append(effectiveness)
    except KeyError:
        data[department][salary_type] = []
        data[department][salary_type].append(effectiveness)

for dept in data:
    for salary in data[dept]:
        print('{0}\t{1}\t{2}'.format(dept, salary,
            sum(data[department][salary])/len(data[department][salary]) ))
