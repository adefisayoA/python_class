# # still use my sql syntax to create my table
# from sqlalchemy import create_engine
# #
# engine = create_engine("mysql+pymysql://fisayo:123456@localhost/pythondevclass", echo=True)
# engine.execute(
#     f"""
#      CREATE TABLE IF NOT EXISTS `studentXX` (studentid INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
#          firstname VARCHAR(50),
#          lastname VARCHAR(50)   );""")


# using the ORM features of sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from modelss import Base, Student, Trainer
from sqlalchemy import create_engine, MetaData, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

CONNECTION_STRING = "mysql+pymysql://{user}:{password}@{host}/{db}"
engine = create_engine(
    CONNECTION_STRING.format(
        # user="root", password="password", host="127.0.0.1", db="default"
        user="fisayo", password="123456", host="127.0.0.1", db="pythondevclass"
    )
)

Base.metadata.create_all(engine) # this would create our object in the db

# metadata = MetaData()


Session = sessionmaker(bind=engine)  # create a session factory (factory for Session objects) which is bound the
# engine setup. The sessionmaker factory generates new Session objects when called

# make changes to db object. Add data details for student
session = Session()

# #  use the Student class to create a new student and session.add(...) to add the instance to our database.
# x_student = Student(first_name="Emmanuel", last_name="Adebayo")
# session.add(x_student)

x_trainer = Trainer(first_name="Ayo", last_name="Akande", location = "Oshodi")
session.add(x_trainer)

#
# session.add_all(
#     [
#         Student(first_name="Folake", last_name="James"),
#         Student(first_name="Susan", last_name="John")
#
#     ]
# )

session.commit()

#chnage first name
# x_student.first_name = 'Joe'

# student = Student()
# student.first_name = "Mary"
# student.last_name = "Bryan"
# session.add(student)


# query Student
students = session.query(Student).all()
for student in students:
    # print(student)
    # print("Student details first_name=%s, last_name=%s" % (student.first_name, student.last_name))
    print(f"{student.first_name} {student.last_name} ")
#
# session.commit()
# session.close()

# session.rollback() to rollback


# example create table for an Oracle db that requires sequence definition for PK
# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
#     name = Column(String(50))
#     fullname = Column(String(50))
#     nickname = Column(String(50))
#
#     def __repr__(self):
#         return "<User(name='%s', fullname='%s', nickname='%s')>" % (
#                                 self.name, self.fullname, self.nickname)
