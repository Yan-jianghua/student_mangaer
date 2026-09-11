import json
from pathlib import Path


DATA_FILE = Path(__file__).with_name("students.json")


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

    if isinstance(data, list):
        return data

    print("列表读取失败，将采用空列表，如有数据丢失请联系工作人员")
    return []
