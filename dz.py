# Создайте класс студента.
# Используя дескрипторы проверяйте ФИО на первую заглавную букву
# и наличие только букв.

import re

class NameDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not re.match(r'^[А-ЯЁ][а-яё]*$', value):
            raise ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class Student:
    first_name = NameDescriptor()
    last_name = NameDescriptor()
    patronymic = NameDescriptor()

    def __init__(self, first_name, last_name, patronymic):
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic

if __name__ == "__main__":
    first_name = input("Введите имя студента: ")
    last_name = input("Введите фамилию студента: ")
    patronymic = input("Введите отчество студента: ")

    student = Student(first_name, last_name, patronymic)

    print("Имя: ", student.first_name)
    print("Фамилия: ", student.last_name)
    print("Отчество: ", student.patronymic)