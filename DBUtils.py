import pymysql

host = "localhost"
user = "root"
password = ""
database = "bank"


def update(sql,param):
    con = pymysql.Connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()
    cursor.execute(sql, param)
    con.commit()
    cursor.close()
    con.close()

def select(sql, param, mode="all", size=1):
    con = pymysql.Connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()
    cursor.execute(sql, param)
    if mode == "all":
        return cursor.fetchall()
    elif mode == "one":
        return cursor.fetchone()
    elif mode == cursor.fetchmany():
        return  cursor.fetchmany(size)
    con.commit()
    cursor.close()
    con.close()
