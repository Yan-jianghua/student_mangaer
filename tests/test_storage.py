import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

import storage
from models import Student


class StorageTests(unittest.TestCase):
    def test_save_and_load_round_trip(self):
        students = [
            Student("001", "小明", 18, 95),
            Student("002", "小红", 17, 88.5),
        ]

        with tempfile.TemporaryDirectory() as temp_dir:
            data_file = Path(temp_dir) / "students.json"

            storage.save_student(students, data_file)
            loaded_students = storage.load_student(data_file)

        self.assertEqual(
            [student.to_dict() for student in loaded_students],
            [student.to_dict() for student in students],
        )
        self.assertTrue(all(isinstance(student, Student) for student in loaded_students))

    def test_load_missing_file_returns_empty_list(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            data_file = Path(temp_dir) / "missing.json"

            self.assertEqual(storage.load_student(data_file), [])

    def test_load_broken_json_returns_empty_list(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            data_file = Path(temp_dir) / "students.json"
            data_file.write_text("{broken", encoding="utf-8")

            with redirect_stdout(io.StringIO()):
                loaded_students = storage.load_student(data_file)

        self.assertEqual(loaded_students, [])

    def test_load_invalid_student_data_returns_empty_list(self):
        invalid_data = [{"name": "缺少字段"}]

        with tempfile.TemporaryDirectory() as temp_dir:
            data_file = Path(temp_dir) / "students.json"
            data_file.write_text(
                json.dumps(invalid_data, ensure_ascii=False),
                encoding="utf-8",
            )

            with redirect_stdout(io.StringIO()):
                loaded_students = storage.load_student(data_file)

        self.assertEqual(loaded_students, [])


if __name__ == "__main__":
    unittest.main()
