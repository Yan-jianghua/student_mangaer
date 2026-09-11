import storage


def add_student(students):
    """增加一名学生。"""
    name = input("请输入学生姓名：")

    while True:
        sid = input("请输入学生的学号：")
        if any(student["id"] == sid for student in students):
            print("学号重复，请重新输入")
            continue
        break

    while True:
        try:
            age = int(input("年龄："))
        except ValueError:
            print("请输入正确的年龄")
            continue
        if 1 <= age <= 100:
            break
        print("请输入正确的年龄")

    while True:
        try:
            score = float(input("成绩："))
        except ValueError:
            print("请输入正确的成绩")
            continue
        if 0 <= score <= 100:
            break
        print("请输入正确的成绩")

    students.append({"name": name, "id": sid, "age": age, "score": score})
    storage.save_student(students)
    print("添加成功")


def show_students(students):
    """显示全部学生信息。"""
    if not students:
        print("暂无学生，请添加")
        return

    print("姓名\t学号\t年龄\t成绩")
    for student in students:
        print(f"{student['name']}\t{student['id']}\t{student['age']}\t{student['score']}")


def find_student(students):
    """按学号或姓名查询学生。"""
    while True:
        print("通过学号查找 -- 1")
        print("通过姓名查找 -- 2")
        print("返回主菜单 -- 0")

        try:
            query_method = int(input("请输入你要查找的方式："))
        except ValueError:
            print("请输入正确的查询方式序号")
            continue

        if query_method == 1:
            sid = input("请输入你要查询学生的学号：")
            matches = [student for student in students if student["id"] == sid]
        elif query_method == 2:
            name = input("请输入你要查找的学生姓名：")
            matches = [student for student in students if student["name"] == name]
        elif query_method == 0:
            return
        else:
            print("请输入正确的查询方式序号")
            continue

        if not matches:
            print("未查询到学生信息")
            continue

        print("姓名\t学号\t年龄\t成绩")
        for student in matches:
            print(f"{student['name']}\t{student['id']}\t{student['age']}\t{student['score']}")


def delete_student(students):
    """按学号删除学生。"""
    while True:
        print("这里是删除学生信息界面，返回主菜单请输入*")
        delete_id = input("请输入您要删除的学生学号：")
        if delete_id == "*":
            return

        for student in students:
            if student["id"] == delete_id:
                students.remove(student)
                storage.save_student(students)
                print("删除成功")
                return

        print("未查询到该学生信息")


def modify_id(student, students):
    """修改学生学号。"""
    while True:
        sid = input("请输入修改后的学号：")
        duplicate = any(
            other_student is not student and other_student["id"] == sid
            for other_student in students
        )
        if duplicate:
            print("学号重复，请重新输入")
            continue

        student["id"] = sid
        storage.save_student(students)
        print("修改成功")
        return


def modify_name(student, students):
    """修改学生姓名。"""
    student["name"] = input("请输入修改后学生的姓名：")
    storage.save_student(students)
    print("修改成功")


def modify_score(student, students):
    """修改学生成绩。"""
    while True:
        try:
            score = float(input("请输入修改后学生的成绩："))
        except ValueError:
            print("输入成绩有误，请重新输入")
            continue

        if not 0 <= score <= 100:
            print("成绩输入有误，请重新输入")
            continue

        student["score"] = score
        storage.save_student(students)
        print("修改成功")
        return


def modify_student(students):
    """根据学号选择并修改学生信息。"""
    while True:
        print("这里是修改学生信息界面，若需返回主菜单请输入：*")
        modify_sid = input("请输入你要修改的学生学号：")
        if modify_sid == "*":
            return

        student = next(
            (item for item in students if item["id"] == modify_sid),
            None,
        )
        if student is None:
            print("没有该学生信息")
            continue

        while True:
            print("修改姓名请按-------1")
            print("修改学号请按-------2")
            print("修改成绩请按-------3")
            print("修改其他学生请按---0")
            try:
                modify_select = int(input("请输入你要进行的操作："))
            except ValueError:
                print("请输入有效数字")
                continue

            if modify_select == 1:
                modify_name(student, students)
            elif modify_select == 2:
                modify_id(student, students)
            elif modify_select == 3:
                modify_score(student, students)
            elif modify_select == 0:
                break
            else:
                print("输入有误，请输入正确的编号")


def statistics_students(students):
    """统计班级人数、平均分、最高分和最低分。"""
    if not students:
        print("暂无学生，无法统计")
        return

    scores = [student["score"] for student in students]
    max_score = max(scores)
    min_score = min(scores)
    first_students = [
        student["name"] for student in students if student["score"] == max_score
    ]
    last_students = [
        student["name"] for student in students if student["score"] == min_score
    ]

    print(f"班级总人数{len(students)}")
    print(f"最高分为{first_students},{max_score}分")
    print(f"最低分为{last_students},{min_score}分")
    print(f"平均分{sum(scores) / len(scores):.2f}")
