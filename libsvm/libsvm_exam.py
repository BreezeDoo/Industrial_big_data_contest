from svmutil import *
import csv
from grid import *

y, x = svm_read_problem(r'C:\Users\Yuhang Du\Desktop\ACT\python\15\livsvm_15.txt')#读入训练数据
prob = svm_problem(y, x)
m = svm_train(prob, '-c 1.0 -g 0.5')#训练
svm_save_model('svm.model', m)

yt_10, xt_10 = svm_read_problem(r'C:\Users\Yuhang Du\Desktop\ACT\复赛\ice2_final\比赛一 最终数据集\最终数据集\10\libsvm_10.txt')#训练测试数据
yt_14, xt_14 = svm_read_problem(r'C:\Users\Yuhang Du\Desktop\ACT\复赛\ice2_final\比赛一 最终数据集\最终数据集\14\libsvm_14.txt')#训练测试数据
p_labs_10, p_acc_10, p_vals_10 = svm_predict(yt_10, xt_10, m)#测试
p_labs_14, p_acc_14, p_vals_14 = svm_predict(yt_14, xt_14, m)#测试

with open(r'C:\Users\Yuhang Du\Desktop\ACT\复赛\ice2_final\比赛一 最终数据集\最终数据集\10\libsvm_record_10.txt', 'w') as rec_10:
    rec_10.writelines(str(p_labs_10))

with open(r'C:\Users\Yuhang Du\Desktop\ACT\复赛\ice2_final\比赛一 最终数据集\最终数据集\14\libsvm_record_14.txt', 'w') as rec_14:
    rec_14.writelines(str(p_labs_14))

with open(r'C:\Users\Yuhang Du\Desktop\ACT\复赛\ice2_final\比赛一 最终数据集\最终数据集\10\Ldata_10.csv', 'r') as test:
    with open(r'C:\Users\Yuhang Du\Desktop\ACT\复赛\ice2_final\比赛一 最终数据集\最终数据集\10\Ldata_libsvm_predict_10.csv',
              'w', newline='') as predict:
        reader = csv.reader(test)
        writer = csv.writer(predict)
        counter = 0
        for row in reader:
            row.append(p_labs_10[counter])
            counter += 1
            writer.writerow(row)

with open(r'C:\Users\Yuhang Du\Desktop\ACT\复赛\ice2_final\比赛一 最终数据集\最终数据集\14\Ldata_14.csv', 'r') as test:
    with open(r'C:\Users\Yuhang Du\Desktop\ACT\复赛\ice2_final\比赛一 最终数据集\最终数据集\14\Ldata_libsvm_predict_14.csv',
              'w', newline='') as predict:
        reader = csv.reader(test)
        writer = csv.writer(predict)
        counter = 0
        for row in reader:
            row.append(p_labs_10[counter])
            counter += 1
            writer.writerow(row)