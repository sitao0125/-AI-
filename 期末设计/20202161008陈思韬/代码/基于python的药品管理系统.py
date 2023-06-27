import uuid
import datetime
#6_16_在输入日期的时候将日期转化为年月日输入
#加入异常处理
def generate_batch_number(drug_name, drug_production_year, drug_production_month, drug_production_day):
    batch_number = f"{drug_name}_{drug_production_year}_{drug_production_month:02}_{drug_production_day:02}"

    return batch_number

#6——26  更改了药品批次号格式

def login():
    accounts = {'root': '123456', 'user': '789456'}

    while True:
        username = input('请输入用户名：')
        password = input('请输入密码：')

        if username in accounts and accounts[username] == password:
            print('登录成功！')
            if username == 'root':
                    show_root_menu()
            else:
                    show_user_menu()
        else:
            print('用户名或密码错误，请重新输入。')

def show_root_menu():
    while True:
        print('菜单：')
        print('1. 药品信息录入')
        print('2. 库存管理')
        print('3. 药品生产日期和其他管理')
        print('4. 药品信息查询功能')
        print('5. 药品数量不够需要补充的提醒')
        print('6. 药品分类与标识')
        print('7. 展示清单')
        print('8. 退出')

        choice = input('请输入数字选择功能：')
        if choice == '1':
            drug_information_entry()
        elif choice == '2':
            inventory_management()
        elif choice == '3':
            drug_date_management()
        elif choice == '4':
            drug_information_query()
        elif choice == '5':
            check_low_quantity_drugs()
        elif choice == '6':
            drug_category_query()
        elif choice == '7':
            show_file()
        elif choice == '8':
            print('退出')
            return
        else:
            print('无效的选择，请重新输入。')


def show_user_menu():
    print('菜单：')
    print('1. 药品信息录入')
    print('2. 药品生产日期和其他管理')
    print('3. 药品信息查询功能')
    print('4. 药品种类与标识')
    print('5.退出')
    # 在这里添加其他功能选项
    choice = input('请输入数字选择功能：')
    if choice == '1':
        drug_information_entry()
    elif choice == '2':
        drug_date_management()
    elif choice == '3':
        drug_information_query()
    elif choice == '4':
        drug_category_query()
    elif choice == '5':
        print('退出')
        return
    else:
        print('无效的选择，请重新输入')


def drug_information_entry():#药品信息录入
        file_path = '药品清单.txt'
        drugs = []

        try:
            with open(file_path, 'r') as file:
                for line in file:
                    drug_info = line.strip().split(',')
                    # 使用line.strip()方法去除首尾的空白字符，然后使用split(',')方法将该行内容按逗号进行分割，生成一个药品信息的列表。
                    drugs.append(drug_info)
        except FileNotFoundError:
            print('药品信息文件不存在。')
            return

        drug_name = input('请输入药品名称：')

        while True:
            try:
                drug_number = input('请输入药品编号：')
                if len(drug_number) != 11:
                    raise ValueError('药品编号长度应为11位')
                if not drug_number.isdigit():
                    raise ValueError('药品编号应为纯数字')
                break  # 输入正确，退出循环
            except ValueError as e:
                print(str(e))

            # 此时药品编号长度等于11且只包含数字，将输入的药品编号赋给变量 drug_number
        print('药品编号正确。')


        drug_production_year = input('请输入药品生产日期的年：')
        drug_production_month = input('请输入药品生产日期的月：')
        drug_production_day = input('请输入药品生产日期的天：')

        drug_expiry_year = input('请输入药品有效期的年份')
        drug_expiry_month = input('请输入药品有效期的月份')
        drug_expiry_day = input('请输入药品有效期的天')

        while True:
            drug_shelf = int(input('请输入货架号：'))
            if drug_shelf < 1 or drug_shelf > 10:
                print('货架号超出范围，请重新输入。')
            else:
                break

        while True:
            drug_level = int(input('请输入要存放的层数：'))
            if drug_level < 1 or drug_level > 10:
                print('层数超出范围，请重新输入。')
            else:
                break
        drug_shelf = str(drug_shelf)
        drug_level = str(drug_level)
        # 将年、月、日合并成日期字符串
        drug_production_date = f"{drug_production_year}-{drug_production_month}-{drug_production_day}"
        drug_expiry_date = f"{drug_expiry_year}-{drug_expiry_month}-{drug_expiry_day}"


        while True:
            try:
                drug_quantity = input('请输入药品数量：')
                if not drug_quantity.isdigit():
                    raise ValueError('药片数量应该为数字')
                break
            except ValueError as e:
                print(str(e))

        drug_categories = []

        while True:
            category = input('请输入药品种类（输入0结束输入）：')
            if category == '0':
                break
            drug_categories.append(category)

        batch_number = generate_batch_number(drug_name, drug_production_year, drug_production_month, drug_production_day)
        drug_info = [drug_name, drug_number, drug_production_date, drug_expiry_date, batch_number, str(drug_quantity),drug_shelf,drug_level]
        drug_info.extend(drug_categories)
#这里使用extend是为了防止drug_info的结构变得更加复杂，
        drugs.append(drug_info)

#也使用。        drug_info = [drug_name, drug_number, drug_production_date, drug_expiry_date, batch_number, str(drug_quantity)]
 #       for category in drug_categories:
  #          drug_info.append(category)

        with open(file_path, 'w') as file:
            for drug in drugs:
                file.write(','.join(drug) + '\n')

        print('药品信息录入成功！')

        drugs.append(drug_info)

def inventory_management():
    file_path = '药品清单.txt'
    drugs = []  # 空列表用于存储药品信息

    try:
        with open(file_path, 'r') as file:
            for line in file:
                drug_info = line.strip().split(',')
                drugs.append(drug_info)
    except FileNotFoundError:
        print('药品信息文件不存在。')
        return

    print('库存管理菜单：')
    print('1. 入库')
    print('2. 出库')
    choice = input('请输入数字选择功能：')

    if choice == '1':
        while True:
            try:
                drug_number = input('请输入药品编号：')
                if len(drug_number) != 11:
                    raise ValueError('药品编号长度应为11位')
                if not drug_number.isdigit():
                    raise ValueError('药品编号应为纯数字')
                break  # 输入正确，退出循环
            except ValueError as e:
                print(str(e))


        available_batches = []
        for batch_info in drugs:
            if len(batch_info) > 1 and batch_info[1] == drug_number:

                available_batches.append(batch_info[4])

        print('可用的药品批次号：')
        for i, batch in enumerate(available_batches):
            print(f"{i+1}. {batch}")

        while True:
            try:
                batch_choice = int(input('请输入药品的批次号编号：'))
                if 1 <= batch_choice <= len(available_batches):
                    break
                else:
                    raise ValueError('无效的选项')
            except ValueError as e:
                print(str(e))

        selected_batch = available_batches[batch_choice - 1]

        while True:
            try:
                quantity = input('请输入入库数量：')
                if not quantity.isdigit():
                    raise ValueError('入库数量应为纯数字')
                break  # 输入正确，退出循环
            except ValueError as e:
                print(str(e))

        update_inventory(drug_number, selected_batch, quantity, '入库')

    elif choice == '2':
        while True:
            try:
                drug_number = input('请输入药品编号：')
                if len(drug_number) != 11:
                    raise ValueError('药品编号长度应为11位')
                if not drug_number.isdigit():
                    raise ValueError('药品编号应为纯数字')
                break  # 输入正确，退出循环
            except ValueError as e:
                print(str(e))

        available_batches = []
        for batch_info in drugs:
            if len(batch_info) > 1 and batch_info[1] == drug_number:
                available_batches.append(batch_info[4])

        print('可用的药品批次号：')
        for i, batch in enumerate(available_batches):
            print(f"{i + 1}. {batch}")

        while True:
            try:
                batch_choice = int(input('请输入药品的批次号编号：'))
                if 1 <= batch_choice <= len(available_batches):
                    break
                else:
                    raise ValueError('无效的选项')
            except ValueError as e:
                print(str(e))

        selected_batch = available_batches[batch_choice - 1]

        while True:
            try:
                quantity = input('请输入出库数量：')
                if not quantity.isdigit():
                    raise ValueError('出库数量应为纯数字')
                break  # 输入正确，退出循环
            except ValueError as e:
                print(str(e))

        update_inventory(drug_number, selected_batch, quantity, '出库')

    else:
        print('无效的选项。')



#更新函数
def update_inventory(drug_number, drug_uuid, quantity_change, operation):
    file_path = '药品清单.txt'
    drugs = []
    quantity_change = int(quantity_change)

    try:
        with open(file_path, 'r') as file:
            for line in file:
                drug_info = line.strip().split(',')
                drugs.append(drug_info)
    except FileNotFoundError:
        print('药品信息文件不存在。')
        return

    updated_drugs = []
    updated = False

    for drug in drugs:
        if len(drug) > 4 and drug[1] == drug_number and drug[4] == drug_uuid:

            if len(drug) > 5:
                current_quantity = int(drug[5])
            else:
                current_quantity = 0

            if operation == '出库' and current_quantity < quantity_change:
                print('药品数量不足，无法出库。')
                print(f'出库数量超过了可用数量！药品编号为 {drug_number}，批次号为 {drug_uuid} 的可用数量为 {current_quantity}.')
                return

            if operation == '出库':
                new_quantity = current_quantity - quantity_change
            elif operation == '入库':
                new_quantity = current_quantity + quantity_change

            drug[5] = str(new_quantity)
            updated = True

        updated_drugs.append(drug)

    if updated:
        with open(file_path, 'w') as file:
            for drug in updated_drugs:
                file.write(','.join(drug) + '\n')

        if operation == '出库':
            print(f'药品数量更新成功！药品编号为 {drug_number}，批次号为 {drug_uuid} 的数量变更为 {new_quantity}.')
        elif operation == '入库':
            print(f'药品数量更新成功！药品编号为 {drug_number}，批次号为 {drug_uuid} 的数量变更为 {new_quantity}.')
    else:
        print(f'未找到匹配的药品记录。请检查药品编号和批次号是否正确。')


def drug_date_management():
    file_path = '药品清单.txt'
    drugs = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                drug_info = line.strip().split(',')
                drugs.append(drug_info)
    except FileNotFoundError:
        print('药品信息文件不存在。')
        return

    while True:
        print('药品生产日期和其他管理菜单：')
        print('1. 显示临期药品')
        print('2. 显示过期药品')
        print('0. 返回上一级菜单')
        choice = input('请输入数字选择功能：')

        if choice == '1':
            today = datetime.datetime.now().date()
            for drug in drugs:
                expiry_date = datetime.datetime.strptime(drug[3], '%Y-%m-%d').date()
                days_left = (expiry_date - today).days
                if days_left < 45 and days_left > 0:
                    print(f'药品编号: {drug[1]}')
                    print(f'药品名称: {drug[0]}')
                    print(f'生产日期: {drug[2]}')
                    print(f'有效期: {drug[3]}')

                    print('层数', drug[7])
                    print('种类', drug[8])
                    print(f'剩余天数: {days_left}')
                    print('---')
        elif choice == '2':
            today = datetime.datetime.now().date()
            for drug in drugs:
                expiry_date = datetime.datetime.strptime(drug[3], '%Y-%m-%d').date()
                days_left = (expiry_date - today).days
                if days_left < 0:
                    print(f'药品编号: {drug[1]}')
                    print(f'药品名称: {drug[0]}')
                    print(f'生产日期: {drug[2]}')
                    print(f'有效期: {drug[3]}')
                    print('层数', drug[7])
                    print('种类', drug[8])
                    print('---')
        elif choice == '0':
            return
        else:
            print('无效的选项。')


def drug_information_query():
    file_path = '药品清单.txt'
    drugs = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                drug_info = line.strip().split(',')
                drugs.append(drug_info)
    except FileNotFoundError:
        print('药品信息文件不存在。')
        return

    drug_number = input('请输入要查询的药品编号：')

    found_drugs = []  # 用于存储符合条件的药品信息

    for drug in drugs:
        if drug[1] == drug_number:
            found_drugs.append(drug)

    if found_drugs:
        print(f'药品编号为 {drug_number} 的药品信息：')
        for drug in found_drugs:
            print('药品名称:', drug[0])
            print('药品编号:', drug[1])
            print('生产日期:', drug[2])
            print('有效期:', drug[3])
            print('批次号:', drug[4])
            print('数量:', drug[5])
            print('货架号',drug[6])
            print('层数',drug[7])
            print('种类',drug[8])
    else:
        print(f'未找到药品编号为 {drug_number} 的药品。')

def check_low_quantity_drugs():
    file_path = '药品清单.txt'
    low_quantity_drugs = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                drug_info = line.strip().split(',')
                if len(drug_info) > 5:
                    drug_quantity = int(drug_info[5])
                    if drug_quantity <= 50:
                        low_quantity_drugs.append(drug_info)
    except FileNotFoundError:
        print('药品信息文件不存在。')
        return

    if len(low_quantity_drugs) > 0:
        with open('需要补充药品.txt', 'w') as file:
            for drug in low_quantity_drugs:
                file.write(','.join(drug) + '\n')

        print('需要补充的药品信息已写入文件 "需要补充药品.txt"。')
    else:
        print('当前没有需要补充的药品。')
def drug_category_query():
    file_path = '药品清单.txt'
    drugs = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                drug_info = line.strip().split(',')
                drugs.append(drug_info)
    except FileNotFoundError:
        print('药品信息文件不存在。')
        return

    category_mapping = {
        '1': '退烧药',
        '2': '消炎药',
        '3': '感冒药',
        '4': '维生素',

    }

    show_menu()

    category_input = input("请输入药品种类编号：")

    if category_input in category_mapping:
        category = category_mapping[category_input]

        found_drugs = []  # 用于存储符合条件的药品信息

        for drug in drugs:
            if len(drug) > 6 and category in drug[6:]:
                found_drugs.append(drug)

        if found_drugs:
            print(f'种类为 {category} 的药品信息：')
            for drug in found_drugs:
                print('药品名称:', drug[0])
                print('药品编号:', drug[1])
                print('生产日期:', drug[2])
                print('有效期:', drug[3])
                print('批次号:', drug[4])
                print('数量:', drug[5])
                print('货架号', drug[6])
                print('层数', drug[7])
                print('---')
        else:
            print(f'未找到种类为 {category} 的药品。')
    else:
        print("输入的药品种类编号无效")
def show_menu():
    print("请选择药品种类：")
    print("1. 退烧药")
    print("2. 消炎药")
    print("3. 感冒药")
    print("4. 维生素")



def show_file_content(file_path):
    try:
        with open(file_path, 'r') as file:
            content = [line.strip().split(',') for line in file.readlines()]

            # 计算每个字段的最大长度
            max_lengths = [max(len(item) for item in column) for column in zip(*content)]

            # 对于数字字段，使用固定的宽度
            for i in range(len(max_lengths)):
                if i == 1 or i == 5 or i == 6 or i == 7:  # 药品编号、库存、最小库存、最大库存
                    max_lengths[i] = max(max_lengths[i], 10)

            # 打印内容
            print('药品名称 |   药品编号    | 生产日期    |  有效期     |  批次号             |库存         |货架        |层数         |药品类别')

            for row in content:
                row_line = ' | '.join('{:<{}}'.format(item, max_length) for item, max_length in zip(row, max_lengths))
                print(row_line)
    except FileNotFoundError:
        print(f'文件 {file_path} 不存在。')


def show_file():
    while True:
        print("1. 展示药品清单文件")
        print("2. 展示需要补充药品清单")
        print("0. 返回上级菜单")
        choice = int(input("请选择你要展示的文件: "))

        if choice == 1:
            show_file_content('药品清单.txt')
        elif choice == 2:
            show_file_content('需要补充药品.txt')
        elif choice == 0:
            break  # 跳出循环返回到上级菜单
        else:
            print("无效的选择")


# 调用函数来展示文件内容


login()
