gongzi = float(input("请输入有固定工资收入的党员的月工资："))
if gongzi  <= 3000: dues = gongzi *0.005
elif gongzi  <= 5000: dues = gongzi *0.01
elif gongzi  <= 10000: dues = gongzi *0.15
else: dues = gongzi*0.02

print("交纳党费：",dues)
