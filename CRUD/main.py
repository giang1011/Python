from fastapi import FastAPI, HTTPException
from CRUD.mode import Student, StudentCreate

app = FastAPI()

student_db = {}

@app.post("/students/", response_model=Student)
def create_student(student: StudentCreate):
    student_id = len(student_db) + 1
    new_student = Student(id=student_id, **student.dict())
    student_db[student_id] = new_student
    return new_student

@app.get("/student/", reponse_model=list[Student])
def get_students():
    return list(student_db.values())

@app.get("/student/{student_id}", response_model=Student)
def update_student(student_id: int, student: StudentCreate):
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    updated_student = Student(id=student_id, **student.dict())
    students_db[student_id] = updated_student
    return updated_student

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    del students_db[student_id]
    return {"message": "Student deleted successfully"}