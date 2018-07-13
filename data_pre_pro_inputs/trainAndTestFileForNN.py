import csv

with open(r'C:\Users\Yuhang Du\Desktop\ACT\python\21\Ldata_21.csv', 'r') as Ldata:
    reader = csv.reader(Ldata)
    with open(r'C:\Users\Yuhang Du\Desktop\ACT\python\21\Ldata_number_21.csv', 'w', newline='') as Ldata_number:
        writer = csv.writer(Ldata_number)
        counter = 1
        for row in reader:
            row[0] = counter
            writer.writerow(row)
            counter = counter + 1
