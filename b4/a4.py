class Student:
    def __init__(self, name, age, scores):
        self.name = name
        self.age = age
        self.scores = scores

    def avg_score(self):
        return sum(self.scores) / len(self.scores)

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Average Score: {self.avg_score():.2f}")


students = []

n = int(input("Nhap so luong sinh vien: "))

for i in range(n):
    print(f"\n--- Sinh Vien {i + 1} ---")
    name = input("Nhap ten: ")
    age = int(input("Nhap tuoi: "))
    scores = input("Nhap diem (cach nhau boi dau cach): ").split()
    score_list = list(map(float, scores))
    student = Student(name, age, score_list)
    students.append(student)

max_avg = max(students, key=lambda s: s.avg_score())
print("\n--- Sinh Vien Co Diem Trung Binh Cao Nhat ---")
max_avg.display()

print("\n--- Danh Sach Sinh Vien Co Diem TB > 8: ---")
found = False
for s in students:
    if s.avg_score() > 8:
        s.display()
        found = True

if not found:
    print("Khong co sinh vien nao co diem TB > 8.")
