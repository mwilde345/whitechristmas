import csv
with open('City_Pop_2016.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    city_set = set()
    for row in spamreader:
        city_set.add((row[0],row[1]))
    print city_set