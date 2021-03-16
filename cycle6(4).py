import csv
with open("C:/Users/student.MCALAB/Documents/cycle5/book1.csv",newline="") as csvfile:
    data = csv.DictReader(csvfile)
    print("name")
    for col in data:
        print(col['name'])

