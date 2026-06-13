import numpy as np
from sklearn.linear_model import LinearRegression

# 🧠 FEATURE 1: SMART GPA PREDICTOR (Machine Learning)
# We feed the computer basic historical data: [Attendance %, Midterm Grade] -> Final GPA
X_train = np.array([[95, 85], [80, 70], [60, 50], [90, 90], [75, 60]])
y_train = np.array([3.8, 3.2, 2.1, 4.0, 2.8])

# Train a basic mathematical model (Linear Regression)
model = LinearRegression()
model.fit(X_train, y_train)

def predict_student_gpa(attendance: float, midterm: float) -> float:
    """Predicts a final GPA score between 0.0 and 4.0 based on current standing."""
    prediction = model.predict([[attendance, midterm]])[0]
    return round(float(np.clip(prediction, 0.0, 4.0)), 2)


# 💬 FEATURE 2: CAMPUS CHATBOT
def answer_campus_query(question: str) -> str:
    """A rule-based AI responder that answers basic campus questions."""
    question = question.lower()
    if "attendance" in question:
        return "Campus Rule: You must maintain a minimum of 75% attendance to sit for final exams."
    elif "library" in question:
        return "The campus library is open daily from 8:00 AM to 10:00 PM."
    elif "grading" in question:
        return "Academia Connect uses a standard 4.0 GPA scale."
    else:
        return "I'm sorry, I don't have that specific rule in my syllabus database yet. Please contact administration."