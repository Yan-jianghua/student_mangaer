import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

import main


class MainMenuTests(unittest.TestCase):
    @patch("main.storage.save_student")
    @patch("main.service.statistics_students")
    @patch("main.service.show_students")
    @patch("main.service.delete_student")
    @patch("main.service.modify_student")
    @patch("main.service.find_student")
    @patch("main.service.add_student")
    @patch("builtins.input", side_effect=["1", "2", "3", "4", "5", "6", "0"])
    def test_menu_routes_all_options(
        self,
        _input,
        add_student,
        find_student,
        modify_student,
        delete_student,
        show_students,
        statistics_students,
        save_student,
    ):
        original_students = main.students
        main.students = []

        try:
            with redirect_stdout(io.StringIO()):
                main.menu()
        finally:
            main.students = original_students

        add_student.assert_called_once_with([])
        find_student.assert_called_once_with([])
        modify_student.assert_called_once_with([])
        delete_student.assert_called_once_with([])
        show_students.assert_called_once_with([])
        statistics_students.assert_called_once_with([])
        save_student.assert_called_once_with([])

    @patch("main.storage.save_student")
    @patch("builtins.input", side_effect=["abc", "9", "0"])
    def test_menu_handles_invalid_options(self, _input, save_student):
        original_students = main.students
        main.students = []
        output = io.StringIO()

        try:
            with redirect_stdout(output):
                main.menu()
        finally:
            main.students = original_students

        text = output.getvalue()
        self.assertIn("请输入正确的序号", text)
        self.assertIn("输入有误请输入正确的序号", text)
        save_student.assert_called_once_with([])


if __name__ == "__main__":
    unittest.main()
