import csv
import random

with open(r'C:\Users\Yuhang Du\Desktop\ACT\python\15\Ldata_number_15.csv', 'r') as Ldata_number:
    reader = csv.reader(Ldata_number)
    data = []
    for row in reader:
        data.append(row)
random.shuffle(data)
len_ = len(data)
with open(r'C:\Users\Yuhang Du\Desktop\ACT\python\15\Ldata_number_train_15.csv', 'w', newline='')\
        as Ldata_number_train:
    train_writer = csv.writer(Ldata_number_train)
    with open(r'C:\Users\Yuhang Du\Desktop\ACT\python\15\Ldata_number_test_15.csv', 'w', newline='') \
            as Ldata_number_test:
        test_writer = csv.writer(Ldata_number_test)
        counter = 1
        for row in data:
            if counter < len_ * 6 // 10:
                train_writer.writerow(row)
            else:
                test_writer.writerow(row)
            counter = counter + 1
