from datetime import datetime, date

class Student:
    def __init__(self, student_id, firstname, middlename, lastname, birthday):
        self.student_id = student_id
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.birthday = birthday

    def get_age(self):
        try:
            birth_date = datetime.strptime(self.birthday, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("")

        today = date.today()
        age = today.year - birth_date.year

        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        return age

    def displayinfo(self):
        full_name = f"{self.firstname} {self.middlename} {self.lastname}"
        age = self.get_age()
        print("\n--- Thong tin sinh vien ---")
        print(f"ID: {self.student_id}")
        print(f"Full name: {full_name}")
        print(f"age: {age}")

students = []

student_id = input("ID HS: ")
firstname = input("firstname: ")
middlename = input("middlename: ")
lastname = input("lastname: ")
birthday = input("birthday (yyyy-mm-dd): ")

student = Student(student_id, firstname, middlename, lastname, birthday)
students.append(student)
print("Add thanh cong!")

student.displayinfo()
