import matplotlib.pyplot as plt
from datetime import datetime

class Person:
    def __init__(self, firstname, middlename, lastname, birthday, address, phone):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.birthday = birthday
        self.address = address
        self.phone = phone

    def get_age(self):
        birth_date = datetime.strptime(self.birthday, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        return age

    def full_name(self):
        return f"{self.firstname} {self.middlename} {self.lastname}"

class Student(Person):
    def __init__(self, regno, gpa, firstname, middlename, lastname, birthday, address, phone):
        super().__init__(firstname, middlename, lastname, birthday, address, phone)
        self.regno = regno
        self.gpa = gpa

    def display(self):
        print(f"\nMa so sinh vien: {self.regno}")
        print(f"Ho ten: {self.full_name()}")
        print(f"Tuoi: {self.get_age()}")
        print(f"Diem GPA: {self.gpa}")
        print(f"Dia chi: {self.address}")
        print(f"So dien thoai: {self.phone}")

students = []

def them_sinh_vien():
    regno = input("Nhap ma so sinh vien: ")
    firstname = input("Nhap ho: ")
    middlename = input("Nhap ten dem: ")
    lastname = input("Nhap ten: ")
    birthday = input("Nhap ngay sinh (yyyy-mm-dd): ")
    address = input("Nhap dia chi: ")
    phone = input("Nhap so dien thoai: ")
    gpa = float(input("Nhap GPA: "))
    sv = Student(regno, gpa, firstname, middlename, lastname, birthday, address, phone)
    students.append(sv)
    print("Da them sinh vien thanh cong.")

def hien_thi_danh_sach():
    if not students:
        print("Danh sach sinh vien trong.")
    else:
        for sv in students:
            sv.display()

def loc_sinh_vien_lon_hon_22():
    print("\nSinh vien co tuoi lon hon 22:")
    found = False
    for sv in students:
        if sv.get_age() > 22:
            sv.display()
            found = True
    if not found:
        print("Khong co sinh vien nao lon hon 22 tuoi.")

def loc_sinh_vien_gpa_80_100_va_nho_hon_22():
    print("\nSinh vien co GPA tu 80-100 va nho hon 22 tuoi:")
    found = False
    for sv in students:
        if 80 <= sv.gpa <= 100 and sv.get_age() < 22:
            sv.display()
            found = True
    if not found:
        print("Khong co sinh vien nao thoa dieu kien.")

def luu_vao_file():
    with open("sinhvien.txt", "w", encoding="utf-8") as f:
        for sv in students:
            f.write(f"{sv.regno},{sv.full_name()},{sv.get_age()},{sv.gpa},{sv.address},{sv.phone}\n")
    print("Da luu danh sach vao file 'sinhvien.txt'.")

def ve_bieu_do_gpa():
    if not students:
        print("Danh sach sinh vien trong, khong the ve bieu do.")
        return

    names = [sv.full_name() for sv in students]
    gpas = [sv.gpa for sv in students]

    plt.figure(figsize=(10, 6))
    bars = plt.bar(names, gpas)

    for bar, gpa in zip(bars, gpas):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{gpa:.1f}',
                 ha='center', va='bottom', fontsize=8)

    plt.xlabel("Ten sinh vien")
    plt.ylabel("Diem GPA")
    plt.title("Bieu do GPA cua sinh vien")
    plt.xticks(rotation=30, ha='right', fontsize=8)
    plt.tight_layout()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()



while True:
    print("\n===== MENU =====")
    print("1. Them sinh vien")
    print("2. Hien thi danh sach sinh vien")
    print("3. Loc sinh vien lon hon 22 tuoi")
    print("4. Loc sinh vien co GPA 80-100 va nho hon 22 tuoi")
    print("5. Luu vao file van ban")
    print("6. Ve bieu do GPA")
    print("0. Thoat")

    choice = input("Chon chuc nang: ")

    if choice == "1":
        them_sinh_vien()
    elif choice == "2":
        hien_thi_danh_sach()
    elif choice == "3":
        loc_sinh_vien_lon_hon_22()
    elif choice == "4":
        loc_sinh_vien_gpa_80_100_va_nho_hon_22()
    elif choice == "5":
        luu_vao_file()
    elif choice == "6":
        ve_bieu_do_gpa()
    elif choice == "0":
        print("Da thoat chuong trinh.")
        break
    else:
        print("Lua chon khong hop le.")
