import mysql.connector
import markdown


def taskReader(counter):
    """
    reads .txt file
    @return all lines in a .txt file and joins the lines with a newline 
    """

    lines = []

    with open('./doorContent/%s.txt' % counter, encoding='utf8') as f:
        for line in f:
            lines.append(line.strip())
        return markdown.markdown(str('\n'.join(lines)))

def answerReader(counter):
    """
    reads .txt file
    @return alls lines in a .txt file and joins the lines with a newline 
    """

    lines = []

    with open('./doorAnswers/%sa.txt' % counter, encoding='utf8') as f:
        for line in f:
            lines.append(line.strip())
        return markdown.markdown(str('\n'.join(lines)))

def connectToDB(init = False):
    """
    Connects to Database
    @return cursor and db connection
    """


    host="127.0.0.1"
    user="root"
    password="8naYsFQd"
    database="adventskalender"

    if init:
        db = mysql.connector.connect(
            host= host,
            user= user,
            password= password
        )
        db.cursor().execute("CREATE DATABASE if not exists " + database)

    db = mysql.connector.connect(
        host= host,
        user= user,
        password= password,
        database= database
    )
    return db, db.cursor(buffered=True)



def addDataToDB():
        """
        Inserts Data into table

        """

        mydb, cur = connectToDB()

        for i in range(1, 25):
            statement = ("INSERT INTO  tuer (id, content, answer) VALUES (%s, %s, %s)")
            valu1 = (i, taskReader(i), answerReader(i))
            cur.execute(statement, valu1)

        mydb.commit()

        print("hinzugefügt, war vorher nix")


def deleteDataFromDB():
    """
    Deletes Data from table tuer
    """

    mydb, cur = connectToDB()
    cur.execute(" DELETE FROM tuer;")
    mydb.commit()



def init(dbupdate: bool):
    """
    initialises the database and creates databases/tables if not existant
    @param dbupdate updates Databse if true

    """
    _, cur = connectToDB(init = True)


    #cur.execute("DROP TABLE if exists tuer")
    cur.execute("CREATE TABLE if not exists tuer (id INT, content TEXT(65535), answer TEXT(65535) )")
    cur.execute("SELECT * FROM adventskalender.tuer;")
    if cur.rowcount == 0:

        addDataToDB()

    elif dbupdate:
        
        deleteDataFromDB()
        print("DB Gelöscht")
        addDataToDB()

    else:
        cur.execute("SHOW TABLES")

        cur.execute("SELECT * FROM adventskalender.tuer;")

        print(cur.rowcount, "drinne")
        for x in cur:
            print(x)
        print("ist was drinne")

        # cur.close(


def getTask(nr):
    """
    gets task from databas
    @param nr looks for id in table tuer
    @return fetches all in database 
    """

    mydb, cur = connectToDB()

    cur.execute("SHOW TABLES")

    tasNr = (f"SELECT content FROM tuer WHERE id = {nr};")
    cur.execute(tasNr)
    return cur.fetchall()[0]

def getAnswer(nr):
    """
    gets Answer from database
    @param nr looks for answer in table tuer
    @return fetches all in database 
    """

    mydb, cur = connectToDB()

    cur.execute("SHOW TABLES")

    ansNr = (f"SELECT answer FROM tuer WHERE id = {nr};")
    cur.execute(ansNr)
    return cur.fetchall()[0]

