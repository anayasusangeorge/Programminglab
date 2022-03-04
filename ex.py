import csv
with open('d4.csv', newline='') as csvfile:
    data = csv.DictReader(csvfile)
    print("period    Series_title_1")
    for row in data:
        print(row['period'], row['Series_title_1'])
