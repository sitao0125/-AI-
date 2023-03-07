import datetime
_name=str(input("请输入您的姓名："))
_year=int(input("请输入您的出生年份："))
_nowyear=datetime.date.today().year
_useryear=_nowyear-_year
print("您好！{0}。您{1}岁。".format(_name,_useryear))
