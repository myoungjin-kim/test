from django.test import TestCase

# Create your tests here.
import sqlite3
print(sqlite3.version)
print(sqlite3.sqlite_version)
conn = sqlite3.connect('../db.sqlite3')#파일 경로를 잘 지정하자 ....
# 커서 획득
c = conn.cursor()
# c.execute("SELECT * FROM auth_user")
c.execute("INSERT into getclothes values('긴팔','반바지','실내','자동차')")
c.execute("SELECT * FROM auth_user")
print(len(c.fetchall()))#테이블안에 있느 row 개수

