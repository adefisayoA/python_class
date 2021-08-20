from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()  # Construct a base class for declarative class definitions


class Student(Base):  # 1, inherits from the declarative base
    __tablename__ = "students"  # 2, set attribute student table name
    id = Column(Integer, primary_key=True, autoincrement=True)  # one of the columns must be a PK
    first_name = Column(String(255))
    last_name = Column(String(255))

    # last_name = Column(String(255), unique=True)

    def __str__(self):
        return f"<Student #{self.id} {self.first_name} {self.last_name}>"


class Trainer(Base):  # 1, inherits from the declarative base
    __tablename__ = "trainers"  # 2, set attribute student table name
    id = Column(Integer, primary_key=True, autoincrement=True)  # one of the columns must be a PK
    first_name = Column(String(255))
    last_name = Column(String(255))
    location = Column(String(255))

    # last_name = Column(String(255), unique=True)

    def __str__(self):
        return f"<Trainer #{self.id} {self.first_name} {self.last_name} {self.location}>"
