n = 10

gaodu= 100
fantan = 0
sum = 0
for i in range(1,n+1):
    sum += gaodu+fantan
    gaodu = fantan = gaodu/2

print("小球在第十次落地时共经过：{0}米，第十次反弹高度：{1}米".format(sum,fantan))
