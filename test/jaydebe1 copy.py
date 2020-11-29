import jaydebeapi

db_path = "/home/zombu/c/transfer/Books2010.accdb"

ucanaccess_jars = [
    "/home/zombu/prj/ucanaccess/ucanaccess-5.0.0.jar",
    "/home/zombu/prj/ucanaccess/lib/commons-lang3-3.8.1.jar",
    "/home/zombu/prj/ucanaccess/lib/commons-logging-1.2.jar",
    "/home/zombu/prj/ucanaccess/lib/hsqldb-2.5.0.jar",
    "/home/zombu/prj/ucanaccess/lib/jackcess-3.0.1.jar",
]
classpath = ":".join(ucanaccess_jars)
cnxn = jaydebeapi.connect(
    "net.ucanaccess.jdbc.UcanaccessDriver",
    f"jdbc:ucanaccess://{db_path};newDatabaseVersion=V2010",
    ["", ""],
    classpath
    )
crsr = cnxn.cursor()
try:
    crsr.execute("DROP TABLE table1")
    cnxn.commit()
except jaydebeapi.DatabaseError as de:
    if "user lacks privilege or object not found: TABLE1" in str(de):
        pass
    else:
        raise
crsr.execute("CREATE TABLE table1 (id COUNTER PRIMARY KEY, fname TEXT(50))")
cnxn.commit()
crsr.execute("INSERT INTO table1 (fname) VALUES ('Gord')")
cnxn.commit()
crsr.execute("SELECT * FROM table1")
for row in crsr.fetchall():
    print(row)
crsr.close()
cnxn.close()