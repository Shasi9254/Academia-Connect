from sqlalchemy import Column, Integer, String, Float
from database import Base

class StudentModel(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    roll_number = Column(String, unique=True)
    attendance_rate = Column(Float)  # Used by AI to predict grades
    midterm_score = Column(Float)     # Used by AI to predict grades
          # Used by AI to predict grades