import csv
import random

with open(r'C:\Users\Yuhang Du\Desktop\ACT\python\21\Ldata_number_21.csv', 'r') as Ldata:
    with open(r'C:\Users\Yuhang Du\Desktop\ACT\python\21\livsvm_21.txt', 'w') as txt:
        reader = csv.reader(Ldata)
        data = []
        for row in reader:
            data.append(row)
        len_ = len(data)
        for i in range(len_):
            data_str_start = ''.join(str(data[i][28]) + ' ')
            data_str = ' '.join((str(j + 1) + ':' + str(data[i][j + 1])) for j in range(26))
            data_str = data_str_start + data_str + '\n'
            # print(data_str)
            txt.write(data_str)