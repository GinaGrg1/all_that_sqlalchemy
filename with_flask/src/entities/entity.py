from sqlalchemy import create_engine, String, Integer
from sqlalchemy.orm import DeclarativeBase, Session, mapped_column

engine = create_engine("postgresql+psycopg2://postgres:regina@localhost:5432/books",
                       echo=False)

class Base(DeclarativeBase):
    pass

class Exams(Base):
    __tablename__ = "exams"

    id = mapped_column(Integer, primary_key=True)
    created_by = mapped_column(String)
    title = mapped_column(String)
    description = mapped_column(String)

Base.metadata.create_all(engine)

session = Session(engine)

exams = session.query(Exams).all()

if not exams:
    mock_exams = Exams(id=1, created_by="SQLAlchemy Exam", 
                        title="Test your knowledge about SQLAlchemy", description="script")
    session.add(mock_exams)
    session.commit()


for exam in exams:
    print(f"{exam.id} -- {exam.title} -- {exam.description}")
