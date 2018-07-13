import csv

with open(r'C:\Users\Yuhang Du\Desktop\ACT\复赛\ice2_final\比赛一 最终数据集\最终数据集\10\10_data.csv', 'r') as data:
    with open(r'C:\Users\Yuhang Du\Desktop\ACT\复赛\ice2_final\比赛一 最终数据集\最终数据集\10\Ldata_10.csv',
              'w', newline='') as Ldata:
        reader = csv.reader(data)
        writer = csv.writer(Ldata)
        next(reader)
        for row in reader:
            row.append(0)
            writer.writerow(row)