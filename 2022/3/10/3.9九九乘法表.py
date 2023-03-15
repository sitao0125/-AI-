#python打印下三角99乘法表
print("#python打印下三角99乘法表")
for i in range(1,10):
    for j in range(1,i+1):
        print('{}*{}={}\t'.format(j,i,i*j),end='')
    print()

print('\n')
#python打印上三角99乘法表
print("#python打印上三角99乘法表")
for i in range(1,10):
    for j in range(1,10-i+1,):
        print('{}*{}={}\t'.format(i, j, j*i), end='')
    print('')

#python打印矩阵块99乘法表
print("python打印矩阵块99乘法表")
for i in range(1,10):
    for j in range(1,10):
        print('{}*{}={}\t'.format(i,j,i*j),end='')
    print()

