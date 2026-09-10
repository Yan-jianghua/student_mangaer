# 学生管理系统 —— 项目入口文件

students = []
#主菜单
def menu():
# 1. 打印系统启动提示
    try:
        print("欢迎进入学生管理系统")
        while True:
            print("=========学生管理系统启动=============")
            print("请输入你要进行的操作所对应的序号:")
            print("1.添加学生信息")
            # 依次输入 学号 / 姓名 / 年龄 / 成绩，组成一个学生存入列表。
            # 学号不能重复：重复则提示并让用户重新输入。
            # 年龄必须是数字；成绩必须是 0–100 的数字。非法则提示原因并重新输入。
            print("2.删除学生信息")
            # 按学号删除：删除后提示成功；删不存在的学号提示“查无此人”。
            print("3.修改学生信息")
            # - 按学号找到后，可修改其 姓名 / 年龄 / 成绩；改完提示。
            print("4.查询学生信息")
            #按学号查找：找到打印该学生信息；找不到提示“查无此人”。
            print("5.显示全部学生信息")
            # 以整齐的表格打印全部学生（学号 / 姓名 / 年龄 / 成绩），一行一个，方便阅读。
            print("6.统计班级情况")
            #输出：总人数、平均分、最高分（含对应姓名）、最低分（含对应姓名）。
            print("0.退出系统")
            try:
                select_num = int(input("请输入您要进行的操作对应的序号:"))
            except ValueError:
                print("请输入正确的序号:")
                continue
            if select_num == 1:
                add_student()
                continue
            elif select_num == 2:
                delete_student()
                continue
            elif select_num == 3:
                modify_student()
                continue
            elif select_num == 4:
                find_student()
                continue
            elif select_num == 5:
                show_students()
                continue
            elif select_num == 6:
                statistics_students()
                continue
            elif select_num == 0:
                print("退出系统成功")
                break
            else:
                print("输入有误请输入正确的序号")
    except Exception as e:
        print("系统出错请联系工作人员")
        print(e)


#增加学生操作
def add_student():
    add_operation = "添加学生"
    name = input("请输入学生姓名：")
    while True:
        sid = input("请输入学生的学号")
        duplicate = False
        for student in students:
            if student["id"] == sid:
                print("学号重复请重新输入")
                duplicate = True
                break
        if duplicate:
            continue
        else:
            break
    while True:
        try:
            age = int(input("年龄："))
            if 100 >= age >= 1:
                break
            else:
                print("请输入正确的年龄")
        except ValueError:
            print("请输入正确的年龄:")
    while True:
        try:
            score = float(input("成绩"))
            if 0 <= score <= 100:
                break
            else:
                print("请输入正确的成绩")
        except ValueError:
            print("请输入正确的成绩")
    student={"name":name,"id":sid,"age":age,"score":score}
    students.append(student)
    print("添加成功")

#显示全部学生信息
def show_students():
    """
    显示出全部学生信息
    :return:
    """
    if not students:
        print("暂无学生，请添加")
        return
    else:
        print("姓名\t学号\t年龄\t成绩")
        for student in students:
            print(f"{student['name']}\t{student['id']}\t{student['age']}\t{student['score']}")

#查询学生信息
def find_student():
    find_operation = "查找学生"
    try:
        while True:
            print("通过学号查找 -- 1")
            print("通过姓名查找 -- 2")
            print("返回主菜单 -- 0")
            query_method = int(input("请输入你要查找的方式:"))

            if query_method == 1:
                sid = input("请输入你要查询学生的学号:")
                found = False
                for student in students:
                    if student["id"] == sid:
                        print("姓名\t学号\t年龄\t成绩")
                        print(f"{student['name']}\t{student['id']}\t{student['age']}\t{student['score']}")
                        found = True
                        break
                if not found:
                    print("未查询到该学生")
            elif query_method == 2:
                name = input("请输入你要查找的学生姓名")
                found = False
                for student in students:
                    if student["name"] == name:
                        print("姓名\t学号\t年龄\t成绩")
                        print(f"{student['name']}\t{student['id']}\t{student['age']}\t{student['score']}")
                        found = True
                        break
                if not found:
                    print("未查询到学生信息")
            elif query_method == 0:
                return
            else:
                print("请输入正确的查询方式的序号")
                continue
    except ValueError:
        print("请输入正确的查询方式的序号")

#删除学生信息
def delete_student():
    while True:
        print("这里是删除学生信息界面，返回主菜单请输入*")
        delete_id = input("请输入您要删除的学生学号:")
        if delete_id == "*":
            return
        else:
            found = False
            for student in students:
                if student["id"] == delete_id:
                    students.remove(student)
                    print("删除成功")
                    found = True
                    break
            if not found:
                print("未查询到该学生信息")
                continue
            else:
                break

#修改学号
def modify_id(student):
    while True:
        sid = input("请输入修改后的学号:")
        duplicate = False
        for other_student in students:
            if other_student is not student and other_student["id"] == sid:
                print("学号重复请重新输入")
                duplicate = True
                break
        if duplicate:
            continue
        else:
            student["id"] = sid
            print("修改成功")
            return
#修改姓名
def modify_name(student):
    name = input("请输入修改后学生的姓名：")
    student["name"] = name
    print("修改成功")
    return
#修改成绩
def modify_score(student):
    while True:
        try:
            score = float(input("请输入修改后学生的成绩："))
        except ValueError:
            print("输入成绩有误请重新输入")
            continue
        if score < 0 or score > 100:
            print("成绩输入有误请重新输入")
        else:
            student["score"] = score
            print("修改成功")
            return
#修改学生信息
def modify_student():
    while True:
        s = []
        print("这里是修改学生信息界面若需返回主菜单请输入：*")
        modify_sid = input("请输入你要修改的学生的学号:")
        if modify_sid == "*":
            return
        else:
            found = False
            for student in students:
                if student["id"] == modify_sid:
                    found = True
                    s = student
                    break
            if not found:
                print("没有该学生信息")
            else:
                while True:
                    print("修改姓名请按-------1\n修改学号请按-------2\n修改成绩请按------3\n修改其他学生请按------0")
                    try:
                        modify_select = int(input("请输入你要进行的操作："))
                    except ValueError:
                        print("请输入有效数字")
                        continue
                    if modify_select == 1:
                        modify_name(s)
                    elif modify_select == 2:
                        modify_id(s)
                    elif modify_select == 3:
                        modify_score(s)
                    elif modify_select == 0:
                        break
                    else:
                        print("输入有误请输入正确的编号")
#统计
def statistics_students():
    if not students:
        print("暂无学生，无法统计")
        return
    else:
        print(f"班级总人数{len(students)}")
        max_score = 0
        min_score = 100
        total_score = 0
        first_student = []
        last_student = []
        for student in students:
            total_score += student["score"]
            if student["score"] >= max_score:
                max_score = student["score"]
            if student["score"] <= min_score:
                min_score = student["score"]
        for student in students:
            if student["score"] == max_score:
                first_student.append(student["name"])
            if student["score"] == min_score:
                last_student.append(student["name"])
        print(f"最高分为{first_student},{max_score}分")
        print(f"最低分为{last_student},{min_score}分")
        print(f"平均分{total_score/len(students):.2f}")
        return



if __name__ == "__main__":
    menu()

