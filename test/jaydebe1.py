import jaydebeapi
import random
import string
import os
import yaml

def rndString(l1, l2):
    res1=''.join(random.choice(string.ascii_uppercase) for i in range(l1))
    res2=''.join(random.choice(string.digits) for i in range(l2))
    return res1+res2

path=os.path.dirname(os.path.realpath(__file__))
with open(path + "/config.yml", "r") as ymlfile:
    cfg = yaml.load(ymlfile)

db_path = cfg["db" ]["path"]
libpath = cfg["ucanaccess"]["baselibpath"]

ucanaccess_jars = [
    os.path.join(libpath,"ucanaccess-5.0.0.jar"),
    os.path.join(libpath,"lib/commons-lang3-3.8.1.jar"),
    os.path.join(libpath,"lib/commons-logging-1.2.jar"),
    os.path.join(libpath,"lib/hsqldb-2.5.0.jar"),
    os.path.join(libpath,"lib/jackcess-3.0.1.jar") ]

classpath = ":".join(ucanaccess_jars)

cnxn = jaydebeapi.connect(
    "net.ucanaccess.jdbc.UcanaccessDriver",
    f"jdbc:ucanaccess://{db_path};newDatabaseVersion=V2010",
    ["", ""],
    classpath
    )
crsr = cnxn.cursor()
crsr.execute("SELECT title_id,title,price FROM books where price>10")
for row in crsr.fetchall():
    print(row)

id=rndString(3,2)
title=rndString(50,0)
price=rndString(0,3)
sql="insert into books (title_id,title,price) values ('"+id+"','"+title+"',"+price+")"
crsr.execute(sql)

crsr.close()
cnxn.close()
