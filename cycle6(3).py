import csv
with open("C:/Users/student.MCALAB/Documents/cycle5/book1.csv",newline="") as csvfile:
    data=csv.reader(csvfile,delimiter=" ",quotechar="|")
    for row in data:
        print(",".join(row))