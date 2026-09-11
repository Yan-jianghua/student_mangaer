import json
from pathlib import Path


DATA_FILE = Path(__file__).with_name("students.json")


def _is_valid_student(student):
    """判断一条学生数据是否具有系统所需的完整结构。"""
    if not isinstance(student, dict):
        return False

    if set(student) != {"id", "name", "age", "score"}:
        return False

    return (
        isinstance(student["id"], str)
        and isinstance(student["name"], str)
        and isinstance(student["age"], int)
        and not isinstance(student["age"], bool)
        and 1 <= student["age"] <= 100
        and isinstance(student["score"], (int, float))
        and not isinstance(student["score"], bool)
        and 0 <= student["score"] <= 100
    )


def save_student(students, data_file=DATA_FILE):
    """把学生列表保存到 JSON 文件。"""
    with data_file.open("w", encoding="utf-8") as file:
        json.dump(students, file, ensure_ascii=False, indent=4)


def load_student(data_file=DATA_FILE):
    """从 JSON 文件读取学生列表；文件不存在或损坏时返回空列表。"""
    if not data_file.exists():
        return []

    try:
        with data_file.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except (OSError, json.JSONDecodeError):
        print("数据异常，将采用空列表，如有数据丢失请联系工作人员")
        return []

    if isinstance(data, list) and all(_is_valid_student(item) for item in data):
        return data

    print("数据格式异常，将采用空列表，如有数据丢失请联系工作人员")
    return []
