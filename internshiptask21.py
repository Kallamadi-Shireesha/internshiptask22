import pandas as pd
import os
import hashlib
import glob


#create a table
import psycopg2
from config import config
def connect():
    connection=None
    params=config()
    print("connecting")
    connection=psycopg2.connect(**params)
    cur=connection.cursor()
    #print("postgresqlversion")
    #cur.execute('select version()')
    #cur.execute("drop table oldfile")
    #cur.execute("create table oldfile(id int, name varchar, checksum varchar);")
    
    #cur.execute("insert into oldfile values (1,'siri') ;")
    #cur.execute("alter table oldfile drop column checksum;")

    #cur.execute("select * from oldfile;")
    #print(cur.fetchall())
    #to check all tables from a database
    #cur.execute("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';")
    #tuples=cur.fetchall()
    #for i in tuples:
     #   print(str(list(i)))
    connection.commit()

    #Sdb_version=cur.fetchone()
    #print(db_version)
    cur.close()
    if connection is not None:
        connection.close()
        print("databse closed")
if __name__=="__main__":
    connect()


#get all the csv files in a list
fil=".csv"
all_fil=[i for i in glob.glob(f"*{fil}")]
l=list(all_fil)
checksums=[]
#calculate checksum
for i in l:
    hasher=hashlib.md5()
    with open(i,'rb') as open_file:
        content=open_file.read()
        hasher.update(content)
        #print(hasher.hexdigest())
'''

d={}
for i in range(1,len(l)):
    t1=open(l[0], 'r')
    t2=open(l[i], 'r')
    fileone = t1.readlines()
    filetwo = t2.readlines()
    if(fileone==filetwo):
        if l[0] in d:
            d[l[0]]=d[l[0]]+1
        else:
            d[l[0]]=1
        #print(l.index(l[0]))
       
    else:
        if l[i] in d:
            d[l[i]]=d[l[i]]+1
        else:
            d[l[i]]=1
        #print(l.index(l[i]))
print(d)
'''
