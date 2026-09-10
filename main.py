# 学生管理系统 —— 项目入口文件
import json
from pathlib import Path


DATA_FILE = Path(__file__).with_name("students.json")


def load_students():
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
        return data if isinstance(data, list) else []
    except (OSError, json.JSONDecodeError):
        print("学生数据文件读取失败，将使用空数据启动")
        return []


def save_students():
    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(students, file, ensure_ascii=False, indent=2)
    except OSError as error:
        print(f"学生数据保存失败：{error}")


students = load_students()
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
                show_statistics()
                continue
            elif select_num == 0:
                save_students()
                print("退出系统成功")
                break
            else:
                print("输入有误请输入正确的序号")
    except Exception as e:
        print("系统出错请联系工作人员")
        print(e)


#增加学生操作
def add_student():
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
    age = input_age()
    score = input_score()
    student={"name":name,"id":sid,"age":age,"score":score}
    students.append(student)
    save_students()
    print("添加成功")

#显示全部学生信息
def show_students():
    if not students:
        print("暂无学生，请添加")
        return
    else:
        print("姓名\t学号\t年龄\t成绩")
        for student in students:
            print(f"{student['name']}\t{student['id']}\t{student['age']}\t{student['score']}")

#查询学生信息
def find_student():
    while True:
        try:
            print("通过学号查找 -- 1")
            print("通过姓名查找 -- 2")
            print("返回主菜单 -- 0")
            query_method = int(input("请输入你要查找的方式:"))
        except ValueError:
            print("请输入正确的查询方式的序号")
            continue
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
                print("未查询到该学生,请重新输入")
            else:
                break
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
def delete_student():
    delete_id = input("请输入你要删除的学生学号:")
    for index, student in enumerate(students):
        if student["id"] == delete_id:
            students.pop(index)
            save_students()
            print("删除成功")
            return
    print("查无此人")


def modify_student():
    student_id = input("请输入要修改的学生学号:")
    student = find_by_id(student_id)
    if student is None:
        print("查无此人")
        return

    print("直接回车表示保留原值")
    name = input(f"姓名（{student['name']}）：")
    if name:
        student["name"] = name

    age_text = input(f"年龄（{student['age']}）：")
    if age_text:
        while True:
            try:
                age = int(age_text)
                if 1 <= age <= 100:
                    student["age"] = age
                    break
                print("请输入 1 到 100 之间的年龄")
            except ValueError:
                print("请输入正确的年龄")
            age_text = input("请重新输入年龄：")

    score_text = input(f"成绩（{student['score']}）：")
    if score_text:
        while True:
            try:
                score = float(score_text)
                if 0 <= score <= 100:
                    student["score"] = score
                    break
                print("请输入 0 到 100 之间的成绩")
            except ValueError:
                print("请输入正确的成绩")
            score_text = input("请重新输入成绩：")
    save_students()
    print("修改成功")


def show_statistics():
    if not students:
        print("暂无学生，无法统计")
        return
    total = len(students)
    average = sum(student["score"] for student in students) / total
    highest = max(students, key=lambda student: student["score"])
    lowest = min(students, key=lambda student: student["score"])
    print(f"总人数：{total}")
    print(f"平均分：{average:.2f}")
    print(f"最高分：{highest['score']}（{highest['name']}）")
    print(f"最低分：{lowest['score']}（{lowest['name']}）")


def find_by_id(student_id):
    for student in students:
        if student["id"] == student_id:
            return student
    return None


def input_age():
    while True:
        try:
            age = int(input("年龄："))
            if 1 <= age <= 100:
                return age
            print("请输入 1 到 100 之间的年龄")
        except ValueError:
            print("请输入正确的年龄")


def input_score():
    while True:
        try:
            score = float(input("成绩："))
            if 0 <= score <= 100:
                return score
            print("请输入 0 到 100 之间的成绩")
        except ValueError:
            print("请输入正确的成绩")


if __name__ == "__main__":
    menu()
