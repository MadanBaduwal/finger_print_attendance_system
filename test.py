import sqlite3



connection = sqlite3.connect('management1.db')
TABLE_NAME = "student_exam_attendance_table"

USER_ID = "user_id"
FLAG = "flag"

connection.execute(" CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + USER_ID +
                    " INTEGER, " + FLAG +"INTEGER);")



userid = "1"

flag = "5"


connection.execute("INSERT INTO " + TABLE_NAME + "(" + USER_ID+","+FLAG+") VALUES ("
                       +userid+","+flag+");")
connection.commit()
