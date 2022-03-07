import csv
fn = 'full_parking_violations_2016.csv'
f = open(fn, 'r')
reader = csv.reader(f)
n=0
for row in reader:
    n+=1
print(n)
