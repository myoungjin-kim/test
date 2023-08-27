
# Create your tests here.
import sqlite3
conn = sqlite3.connect('../db.sqlite3')#파일 경로를 잘 지정하자 ....
# 커서 획득
c = conn.cursor()
# c.execute("SELECT * FROM auth_user")
print(c.execute("SELECT * FROM get").fetchall())



