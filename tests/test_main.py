import unittest
from unittest.mock import patch

import main


class MainMenuTests(unittest.TestCase):
    @patch("main.storage.save_student")
    @patch("main.service.delete_student")
    @patch("main.service.modify_student")
    @patch("main.service.find_student")
    @patch("builtins.input", side_effect=["2", "3", "4", "0"])
    def test_menu_routes_options_in_documented_order(
        self,
        _input,
        find_student,
        modify_student,
        delete_student,
        save_student,
    ):
        original_students = main.students
        main.students = []
        try:
            main.menu()
        finally:
            main.students = original_students

        find_student.assert_called_once_with([])
        modify_student.assert_called_once_with([])
        delete_student.assert_called_once_with([])
        save_student.assert_called_once_with([])


if __name__ == "__main__":
    unittest.main()
