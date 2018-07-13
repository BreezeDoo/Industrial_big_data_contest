import csv
import numpy as np

with open(r'C:\Users\Yuhang Du\Desktop\ACT\python\15\Ldata_number_test_15.csv', 'r') \
        as Ldata_number_test:
    with open(r'C:\Users\Yuhang Du\Desktop\ACT\python\15\Ldata_number_test_sorted_15.csv', 'w', newline='') \
            as Ldata_number_test_sorted:
        reader = csv.reader(Ldata_number_test)
        writer = csv.writer(Ldata_number_test_sorted)
        data = []
        for row in reader:
            data.append(row)
        data = np.array(data)
        data = data[data[:, 0].argsort()]
        for row in data:
            writer.writerow(row)