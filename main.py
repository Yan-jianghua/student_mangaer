# 学生管理系统 —— 项目入口文件
students = []
def menu():
# 1. 打印系统启动提示
    try:
        print("欢迎进入学生管理系统")

        #2.主菜单
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
                pass
            elif select_num == 3:
                pass
            elif select_num == 4:
                pass
            elif select_num == 5:
                show_students()
                continue
            elif select_num == 6:
                pass
            elif select_num == 0:
                print("退出系统成功")
                break
            else:
                print("输入有误请输入正确的序号")
    except Exception as e:
        print("系统出错请联系工作人员")
        print(e)

def add_student():
    name = input("请输入学生姓名：")
    sid = input("请输入学生的学号")
    try:
        age = int(input("年龄："))
    except ValueError:
        print("请输入正确的年龄:")
    try:
        score = float(input("成绩"))
    except ValueError:
        print("请输入正确的成绩")
    student={"name":name,"id":sid,"age":age,"score":score}
    students.append(student)
    print("添加成功")

def show_students():
    if not students:
        print("暂无学生，请添加")
        return
    else:
        print("姓名\t学号\t年龄\t成绩")
        for student in students:
            print(f"{student['name']},{student['id']},{student['age']},{student['score']}")




if __name__ == "__main__":
    menu()

