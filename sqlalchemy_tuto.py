from operator import or_
from sqlalchemy import create_engine, String, Column, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import or_

engine = create_engine('mysql+pymysql://root:@localhost/db_ak',echo=False)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Student(Base):
    __tablename__='Student'
    name=Column(String(50))
    email=Column(String(50))
    id=Column(Integer, primary_key=True)

# Base.metadata.create_all(engine)
# to create database

# student1 = Student(name='Akash Patel',id=1,email='akashpatel@gmail.com')
# student2 = Student(name='Palak Patel',id=2,email='palakpatel@gmail.com')

#following lines will add entry in table
# session.add_all([student1,student2])
# session.commit()

# Query from db table
# students = session.query(Student).all()
# for val in students:
#     print(val.name)

# students = session.query(Student).order_by(Student.name.desc())
# for val in students:
#     print(val.name)

# student = session.query(Student).filter(Student.name=="Akash Patel")
# print(student)
# for val in student:
#     print(val.name)

# student = session.query(Student).filter(or_(Student.name=="Akash Patel",Student.name=="Palak Patel"))
# for val in student:
#     print(val.email)

# count = session.query(Student).filter(or_(Student.name=="Akash Patel",Student.name=="Palak Patel")).count()
# print(count)

#Update data

# student = session.query(Student).filter(Student.name=="Akash Patel").first()
# student.name = "Kashyap Patel"
# student.email = "kashyap@patel.com"
# session.commit()

#Delete daya

# student = session.query(Student).filter(Student.name=="Kashyap Patel").first()
# session.delete(student)
# session.commit()
