import json
import tempfile
import unittest
from pathlib import Path

import storage


class StorageTests(unittest.TestCase):
    def test_save_and_load_round_trip(self):
        students = [{"id": "001", "name": "小明", "age": 18, "score": 95.0}]
        with tempfile.TemporaryDirectory() as temp_dir:
            data_file = Path(temp_dir) / "students.json"

            storage.save_student(students, data_file)

            self.assertEqual(storage.load_student(data_file), students)

    def test_load_rejects_invalid_student_shape(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            data_file = Path(temp_dir) / "students.json"
            data_file.write_text(json.dumps([{"name": "缺少字段"}]), encoding="utf-8")

            self.assertEqual(storage.load_student(data_file), [])

    def test_load_handles_broken_json(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            data_file = Path(temp_dir) / "students.json"
            data_file.write_text("{broken", encoding="utf-8")

            self.assertEqual(storage.load_student(data_file), [])


if __name__ == "__main__":
    unittest.main()
