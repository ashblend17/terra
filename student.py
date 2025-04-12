import csv

def filter_students(filee, threshold):
    with open(filee, 'r') as f:
        data = csv.DictReader(f)
        for entry in data:
            grades = list(map(float, row['grade'].split(',')))
            avg = sum(grades) / len(grades)
            if avg > threshold:
                print(row['name'])

