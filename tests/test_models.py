import unittest

from models import Student


class StudentTests(unittest.TestCase):
    def test_create_student(self):
        student = Student("001", "小明", 18, 95)

        self.assertEqual(student.id, "001")
        self.assertEqual(student.name, "小明")
        self.assertEqual(student.get_age(), 18)
        self.assertEqual(student.get_score(), 95)

    def test_rejects_invalid_age(self):
        with self.assertRaises(ValueError):
            Student("001", "小明", 0, 95)

        with self.assertRaises(ValueError):
            Student("001", "小明", 101, 95)

    def test_rejects_invalid_score(self):
        with self.assertRaises(ValueError):
            Student("001", "小明", 18, -1)

        with self.assertRaises(ValueError):
            Student("001", "小明", 18, 101)

    def test_accepts_boundary_values(self):
        minimum = Student("001", "最小值", 1, 0)
        maximum = Student("002", "最大值", 100, 100)

        self.assertEqual(minimum.get_age(), 1)
        self.assertEqual(minimum.get_score(), 0)
        self.assertEqual(maximum.get_age(), 100)
        self.assertEqual(maximum.get_score(), 100)

    def test_set_score(self):
        student = Student("001", "小明", 18, 60)

        student.set_score(90)

        self.assertEqual(student.get_score(), 90)

    def test_set_score_rejects_invalid_values(self):
        student = Student("001", "小明", 18, 60)

        with self.assertRaises(ValueError):
            student.set_score(-1)

        with self.assertRaises(ValueError):
            student.set_score(101)

        self.assertEqual(student.get_score(), 60)

    def test_to_dict(self):
        student = Student("001", "小明", 18, 95)

        self.assertEqual(
            student.to_dict(),
            {"id": "001", "name": "小明", "age": 18, "score": 95},
        )

    def test_str(self):
        student = Student("001", "小明", 18, 95)

        self.assertEqual(str(student), "姓名小明,年龄18,成绩95,学号:001")


if __name__ == "__main__":
    unittest.main()
