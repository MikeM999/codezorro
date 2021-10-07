import csv
from einstein.models import Narrative

with open('templates/Python.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        vCode = "PY" + str(row[0])
        _, created = Narrative.objects.get_or_create(
                code=vCode,
                text=row[1]
                )
        
              
