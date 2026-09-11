import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

import service


class ServiceTests(unittest.TestCase):
    @patch("service.storage.save_student")
    @patch("builtins.input", side_effect=["001", "小明", "abc", "18", "101", "95"])
    def test_add_student_retries_invalid_values(self, _input, save_student):
        students = []

        service.add_student(students)

        self.assertEqual(
            students,
            [{"id": "001", "name": "小明", "age": 18, "score": 95.0}],
        )
        save_student.assert_called_once_with(students)

    @patch("service.storage.save_student")
    @patch("builtins.input", side_effect=["001", "002", "小红", "16", "88"])
    def test_add_student_rejects_duplicate_id(self, _input, _save_student):
        students = [{"id": "001", "name": "已有", "age": 17, "score": 80}]

        service.add_student(students)

        self.assertEqual(students[-1]["id"], "002")

    @patch("service.storage.save_student")
    @patch("builtins.input", side_effect=["002"])
    def test_delete_student(self, _input, save_student):
        students = [
            {"id": "001", "name": "小明", "age": 18, "score": 95},
            {"id": "002", "name": "小红", "age": 17, "score": 88},
        ]

        service.delete_student(students)

        self.assertEqual([student["id"] for student in students], ["001"])
        save_student.assert_called_once_with(students)

    def test_statistics_students(self):
        students = [
            {"id": "001", "name": "小明", "age": 18, "score": 100},
            {"id": "002", "name": "小红", "age": 17, "score": 80},
        ]
        output = io.StringIO()

        with redirect_stdout(output):
            service.statistics_students(students)

        text = output.getvalue()
        self.assertIn("班级总人数2", text)
        self.assertIn("最高分为['小明'],100分", text)
        self.assertIn("最低分为['小红'],80分", text)
        self.assertIn("平均分90.00", text)

    def test_show_students_uses_documented_column_order(self):
        students = [{"id": "001", "name": "小明", "age": 18, "score": 95}]
        output = io.StringIO()

        with redirect_stdout(output):
            service.show_students(students)

        lines = output.getvalue().splitlines()
        self.assertEqual(lines[0], "学号\t姓名\t年龄\t成绩")
        self.assertEqual(lines[1], "001\t小明\t18\t95")

    @patch("builtins.input", side_effect=["3", "90", "90", "0"])
    def test_find_students_accepts_single_score_interval(self, _input):
        students = [{"id": "001", "name": "小明", "age": 18, "score": 90}]
        output = io.StringIO()

        with redirect_stdout(output):
            service.find_student(students)

        self.assertIn("001\t小明\t18\t90", output.getvalue())


if __name__ == "__main__":
    unittest.main()
