import json
import matplotlib.pyplot as plt
from datetime import datetime

class Student:
    def __init__(self, student_id, name, birthday, gpa):
        self.student_id = student_id
        self.name = name
        self.birthday = birthday  
        self.gpa = float(gpa)

    def get_age(self):
        birth_date = datetime.strptime(self.birthday, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        return age

    def display(self):
        print(f"ID: {self.student_id}, Name: {self.name}, Birthday: {self.birthday}, "
              f"Age: {self.get_age()}, GPA: {self.gpa}")

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "birthday": self.birthday,
            "gpa": self.gpa
        }


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self):
        try:
            student_id = input("Nhap ID: ")
            name = input("Nhap ten: ")
            birthday = input("Nhap ngay sinh (YYYY-MM-DD): ")
            gpa = float(input("Nhap GPA: "))
            self.students.append(Student(student_id, name, birthday, gpa))
            print(" Add sinh vient hanh cong!")
        except ValueError:
            print(" Error: GPA phai la so!")

    def display_all(self):
        if not self.students:
            print(" Ko co sinh vien nao!")
            return
        print("\n Danh sanh sinh vien:")
        for s in self.students:
            s.display()

    def display_gpa_high(self):
        high_students = [s for s in self.students if s.gpa >= 8]
        if not high_students:
            print(" Ko co sinh vien nao GPA >= 8!")
            return
        print("\n Sinh viên giỏi (GPA >= 8):")
        for s in high_students:
            s.display()

    def save_to_file(self):
        try:
            with open("students.json", "w", encoding="utf-8") as f:
                json.dump([s.to_dict() for s in self.students], f, ensure_ascii=False, indent=4)
            print(" Luu giu lieu thanh cong vao students.json")
        except Exception as e:
            print(" Loi khi luu file:", e)

    def find_by_id(self):
        student_id = input("Nhap Id sinh vien can tim: ")
        for s in self.students:
            if s.student_id == student_id:
                print(" Thong tin sinh vien:")
                s.display()
                return
        print(" Khong tim thay sinh vien!")

    def plot_gpa_chart(self):
        if not self.students:
            print(" Ko co du lieu bieu do!")
            return
        names = [s.name for s in self.students]
        gpas = [s.gpa for s in self.students]
        plt.bar(names, gpas, color='blue')
        plt.xlabel("Sinh viên")
        plt.ylabel("GPA")
        plt.title("Bieu do GPA cua sinh vien")
        plt.show()



def main():
    manager = StudentManager()

    while True:
        print("\n===== MENU =====")
        print("1. Thêm sinh viên")
        print("2. Hiển thị tất cả sinh viên")
        print("3. Hiển thị sinh viên giỏi GPA >= 8")
        print("4. Lưu ra file")
        print("5. Xem thông tin sinh viên theo ID")
        print("6. Vẽ biểu đồ GPA")
        print("7. Thoát chương trình")

        choice = input("Nhập lựa chọn: ")

        try:
            if choice == "1":
                manager.add_student()
            elif choice == "2":
                manager.display_all()
            elif choice == "3":
                manager.display_gpa_high()
            elif choice == "4":
                manager.save_to_file()
            elif choice == "5":
                manager.find_by_id()
            elif choice == "6":
                manager.plot_gpa_chart()
            elif choice == "7":
                print(" Thoát chương trình!")
                break
            else:
                print(" Lựa chọn không hợp lệ!")
        except Exception as e:
            print(" Lỗi không mong muốn:", e)


if __name__ == "__main__":
    main()
