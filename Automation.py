import datetime
import time 
import random
import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-2G4QGG6\SQLEXPRESS;'
                        'Database=Call_Center;'
                        'Trusted_Connection=yes;')   # A local connection

cursor = conn.cursor()



while 1==1:
    date = datetime.date.today()
    location = random.randint(111,201)
    company =  random.randint(11,30)
    issue =   random.randint(111,130)
    csr = random.randint(111,210)
    rtime = random.randint(1,300)
    ctime = random.randint(1,600)
    status = random.randint(1,100)
    if status < 75:
        status = 1
    elif status < 85:
        status = 2
    elif status < 90:
        status = 3
    else:
        status = 4
    if status == 1:
        rating = random.randint(5,10)
    elif status == 2:
        rating = random.randint(3,8)
    elif status == 3:
        rating = random.randint(1,3)
    elif status == 4:
        rating = random.randint(1,5)

    print(date)
    
    cursor.execute('insert into calls values(getdate(),'
                   + str(location) + ','
                   + str(company) + ','
                   + str(issue) + ','
                   + str(csr) + ','
                   + str(rtime) + ','
                   + str(ctime) + ',' 
                   + str(status) + ','
                   + str(rating) + ')'
                   )
    cursor.commit() 
    time.sleep(1)