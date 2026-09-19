class Student:
    def __init__(
        self,
        student_id: str,
        name: str,
        age: int,
        score: float,
    ) -> None:
        """
        :param student_id: 学号
        :param name: 姓名
        :param age: 年龄
        :param score: 成绩
        """
        self.student_id = student_id
        self.name = name
        if 0 < age <= 100:
            self.__age = age
        else:
            raise ValueError("年龄应在1~100区间")
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError("成绩应在0~100区间")

    def __str__(self) -> str:
        """
        输出学生姓名，学号，年龄，成绩的信息
        :return:学生的信息
        """
        return f"姓名{self.name},年龄{self.__age},成绩{self.__score},学号:{str(self.student_id)}"

    def get_age(self) -> int:
        """
        获取学生年龄信息
        :return: 年龄
        """
        return self.__age

    def get_score(self) -> float:
        """
        获取学生成绩信息
        :return: 成绩
        """
        return self.__score

    def set_score(self, score: float) -> None:
        """
        修改学生成绩信息
        :param score:
        :return: 成绩
        """
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError("成绩应在0~100之间")

    def to_dict(self) -> dict:
        """
        将学生类的信息转化为字典格式
        :return:
        """
        return {
            "id": self.student_id,
            "name": self.name,
            "age": self.__age,
            "score": self.__score,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Student":
        return cls(
            student_id=data["id"],
            name=data["name"],
            age=data["age"],
            score=data["score"],
        )
