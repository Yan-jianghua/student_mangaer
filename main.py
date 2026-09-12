# 学生管理系统 —— 项目入口文件
import service
import storage
# 主菜单
def menu():
    print("欢迎进入学生管理系统")
    while True:
        print("=========学生管理系统启动=============")
        print("请输入你要进行的操作所对应的序号:")
        print("1.添加学生信息")
        print("2.查询学生信息")
        print("3.修改学生信息")
        print("4.删除学生信息")
        print("5.显示全部学生信息")
        print("6.统计班级情况")
        print("0.退出系统")

        try:
            select_num = int(input("请输入您要进行的操作对应的序号:"))
        except ValueError:
            print("请输入正确的序号:")
            continue

        if select_num == 1:
            service.add_student(students)
        elif select_num == 2:
            service.find_student(students)
        elif select_num == 3:
            service.modify_student(students)
        elif select_num == 4:
            service.delete_student(students)
        elif select_num == 5:
            service.show_students(students)
        elif select_num == 6:
            service.statistics_students(students)
        elif select_num == 0:
            storage.save_student(students)
            print("退出系统成功，再见")
            break
        else:
            print("输入有误请输入正确的序号")




students = storage.load_student()

if __name__ == "__main__":
    menu()
