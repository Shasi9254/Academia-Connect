from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, ai_engine
from database import engine, get_db

# Create the database tables automatically when starting the app
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Academia Connect Dashboard")

# 1. ADD STUDENT (Replaces adding a record to your C++ file)
@app.post("/add-student/")
def add_student(name: str, roll_number: str, attendance: float, midterm: float, db: Session = Depends(get_db)):
    new_student = models.StudentModel(
        name=name, roll_number=roll_number, attendance_rate=attendance, midterm_score=midterm
    )
    db.add(new_student)
    db.commit()
    return {"message": f"Student {name} added successfully!"}

# 2. VIEW ALL STUDENTS (Replaces your display() function in C++)
@app.get("/view-students/")
def view_students(db: Session = Depends(get_db)):
    return db.query(models.StudentModel).all()

# 3. AI ENDPOINT: PREDICT GPA
@app.get("/predict/{roll_number}")
def get_prediction(roll_number: str, db: Session = Depends(get_db)):
    student = db.query(models.StudentModel).filter(models.StudentModel.roll_number == roll_number).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    # Run the student's data through our Machine Learning model
    predicted_gpa = ai_engine.predict_student_gpa(student.attendance_rate, student.midterm_score)
    return {
        "name": student.name,
        "predicted_gpa": predicted_gpa
    }

# 4. AI ENDPOINT: CAMPUS CHATBOT
@app.get("/chatbot/")
def ask_bot(question: str):
    answer = ai_engine.answer_campus_query(question)
    return {"bot_answer": answer}