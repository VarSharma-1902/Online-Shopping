import mysql.connector

conn = mysql.connector.connect(host = "127.0.0.1", user = "root", password = "sql8varsha")
cursor = conn.cursor() 
cursor.execute("USE market")

def sql_cust_db(name, dob, gVar, address, pin, phone, email, pswd): 
    sql  =  "INSERT  INTO  customer  VALUES  (%s,STR_TO_DATE(%s,'%d-%m-%Y'),%s,%s,%s,%s,%s,%s)"
    values = (name, dob, gVar, address, pin, phone, email, pswd) 
    cursor.execute(sql, values)
    conn.commit()

def sql_check_record_exist(email, pswd):
    cursor.execute("select exists (select * from customer where email = %s  and pswd = %s);", (email, pswd))
    result = cursor.fetchall() 
    return result

def  extract_vegetables(): 
    cursor.execute("SELECT * FROM vegetables;") 
    result = cursor.fetchall()
    return result

def  extract_fruits(): 
    cursor.execute("SELECT * FROM fruits;") 
    result = cursor.fetchall()
    return result

def  extract_bodycare(): 
    cursor.execute("SELECT * FROM bodycare;") 
    result = cursor.fetchall()
    return result

def   extract_haircare(): 
    cursor.execute("SELECT * FROM haircare;") 
    result = cursor.fetchall()
    return result

def  extract_snacks(): 
    cursor.execute("SELECT * FROM snacks;") 
    result = cursor.fetchall()
    return result

def extract_stationery(): 
    cursor.execute("SELECT * FROM stationery;") 
    result = cursor.fetchall()
    return result
