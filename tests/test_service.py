import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

import service
from models import Student


class ServiceTests(unittest.TestCase):
    @patch("service.storage.save_student")
    @patch("builtins.input", side_effect=["001", "小明", "abc", "18", "101", "95"])
    def test_add_student_retries_invalid_values(self, _input, save_student):
        students = []

        with redirect_stdout(io.StringIO()):
            service.add_student(students)

        self.assertEqual(len(students), 1)
        self.assertEqual(
            students[0].to_dict(),
            {"id": "001", "name": "小明", "age": 18, "score": 95.0},
        )
        save_student.assert_called_once_with(students)

    @patch("service.storage.save_student")
    @patch("builtins.input", side_effect=["001", "002", "小红", "16", "88"])
    def test_add_student_rejects_duplicate_id(self, _input, save_student):
        students = [Student("001", "已有", 17, 80)]

        with redirect_stdout(io.StringIO()):
            service.add_student(students)

        self.assertEqual(students[-1].student_id, "002")
        save_student.assert_called_once_with(students)

    def test_show_students(self):
        students = [Student("001", "小明", 18, 95)]
        output = io.StringIO()

        with redirect_stdout(output):
            service.show_students(students)

        self.assertEqual(
            output.getvalue().splitlines(),
            ["学号\t姓名\t年龄\t成绩", "001\t小明\t18\t95"],
        )

    def test_show_students_handles_empty_list(self):
        output = io.StringIO()

        with redirect_stdout(output):
            service.show_students([])

        self.assertIn("暂无学生", output.getvalue())

    @patch("builtins.input", side_effect=["3", "90", "90", "0"])
    def test_find_students_accepts_single_score_interval(self, _input):
        students = [Student("001", "小明", 18, 90)]
        output = io.StringIO()

        with redirect_stdout(output):
            service.find_student(students)

        self.assertIn("001\t小明\t18\t90", output.getvalue())

    @patch("service.storage.save_student")
    @patch("builtins.input", side_effect=["002"])
    def test_delete_student(self, _input, save_student):
        students = [
            Student("001", "小明", 18, 95),
            Student("002", "小红", 17, 88),
        ]

        with redirect_stdout(io.StringIO()):
            service.delete_student(students)

        self.assertEqual([student.student_id for student in students], ["001"])
        save_student.assert_called_once_with(students)

    @patch("service.storage.save_student")
    @patch("builtins.input", side_effect=["001", "003"])
    def test_modify_id_rejects_duplicate(self, _input, save_student):
        first = Student("001", "小明", 18, 95)
        second = Student("002", "小红", 17, 88)
        students = [first, second]

        with redirect_stdout(io.StringIO()):
            service.modify_id(second, students)

        self.assertEqual(second.student_id, "003")
        save_student.assert_called_once_with(students)

    @patch("service.storage.save_student")
    @patch("builtins.input", side_effect=["小华"])
    def test_modify_name(self, _input, save_student):
        student = Student("001", "小明", 18, 95)
        students = [student]

        with redirect_stdout(io.StringIO()):
            service.modify_name(student, students)

        self.assertEqual(student.name, "小华")
        save_student.assert_called_once_with(students)

    @patch("service.storage.save_student")
    @patch("builtins.input", side_effect=["101", "96"])
    def test_modify_score_retries_invalid_value(self, _input, save_student):
        student = Student("001", "小明", 18, 95)
        students = [student]

        with redirect_stdout(io.StringIO()):
            service.modify_score(student, students)

        self.assertEqual(student.get_score(), 96)
        save_student.assert_called_once_with(students)

    def test_statistics_students(self):
        students = [
            Student("001", "小明", 18, 100),
            Student("002", "小红", 17, 80),
        ]
        output = io.StringIO()

        with redirect_stdout(output):
            service.statistics_students(students)

        text = output.getvalue()
        self.assertIn("班级总人数2", text)
        self.assertIn("最高分为['小明'],100分", text)
        self.assertIn("最低分为['小红'],80分", text)
        self.assertIn("平均分90.00", text)

    def test_statistics_students_handles_empty_list(self):
        output = io.StringIO()

        with redirect_stdout(output):
            service.statistics_students([])

        self.assertIn("暂无学生", output.getvalue())


if __name__ == "__main__":
    unittest.main()
