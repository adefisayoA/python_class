import pymysql

# create Database ###############################################################################
# db = pymysql.connect("127.0.0.1", "root", "password", "")

db = pymysql.connect(host="localhost", user="fisayo", password="123456", database="")  # connection
#
with db.cursor() as c:
    c.execute("CREATE SCHEMA IF NOT EXISTS pythondevclass DEFAULT CHARACTER SET utf8;")  # my sql script
db.close()
#
# db = pymysql.connect("127.0.0.1", "root", "password", "default")
# db = pymysql.connect(host = "localhost",user =  "fisayo", password = "123456", database= "pythondevclass")
# db.close()
#
# # create table ###############################################################################
db = pymysql.connect("127.0.0.1", "root", "password", "default")
#
db = pymysql.connect(host = "localhost",user =  "fisayo", password = "123456", database= "pythondevclass")
with db.cursor() as c:
    c.execute("CREATE TABLE IF NOT EXISTS exampleX (a integer, b varchar(255));")
    a = int(input("Please provide integer value for a: "))
    b = input("Please provide value for b: ")[:254]
    c.execute("INSERT INTO `exampleX` (a, b) VALUES (%s, %s);", (a, b)) #
    db.commit() # connection is not autocommit by default. So you must commit to save your changes.
db.close()

# CRUD statement  - create read update delete
# select result from table ###############################################################################
# db = pymysql.connect(host = "localhost",user =  "fisayo", password = "123456", database= "pythondevclass")
# with db.cursor() as c:
#     c.execute("select * from exampleX;")
#     result = c.fetchone()
#     # result = c.fetchall()
#     # result = c.fetchmany(2)
#
#     print(result)
#         #db.commit() # connection is not autocommit by default. So you must commit to save your changes.
# db.close()

#### update ##########################################################
# db = pymysql.connect(host="localhost", user="fisayo", password="123456", database="pythondevclass")
# with db.cursor() as c:
#     c.execute("""update examplex set b = "Brush my teeth" WHERE a = %s""", 2)
#     # result = c.fetchone()
#     # result = c.fetchall()
#     # result = c.fetchmany(2)
#     db.commit()
#     # print(result)
#     # db.commit() # connection is not autocommit by default. So you must commit to save your changes.
# db.close()


# delete #####################################################
db = pymysql.connect(host="localhost", user="fisayo", password="123456", database="pythondevclass")
with db.cursor() as c:
    c.execute("""Delete from examplex WHERE a = %s""", 2)
    # result = c.fetchone()
    # result = c.fetchall()
    # result = c.fetchmany(2)
    db.commit()
    # print(result)
    # db.commit() # connection is not autocommit by default. So you must commit to save your changes.
db.close()
