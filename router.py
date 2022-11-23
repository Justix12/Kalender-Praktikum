from flask import Flask, render_template, make_response, request
import random
from datetime import date
import databasecontroller as dbc
import cookie as ck

app = Flask(__name__)

def init():
    """ 
    @return returns Flask app name
    """
    return app

def getDate():
    """ 
    gets current day and month
    """
    today = date.today()
    day = int(today.strftime("%d"))
    month = int(today.strftime("%m"))
    return day, month     


@app.route("/")
def start():
    """ 
    creates dictionary doorlist, requests cookies, generates backround URL,
    @return renders start.html, returns variables
    """
    
    title = "ORDIX 2022 Adventskalender"
    doorlist = []
    backroundlist = ("../static/img/snow.png", "../static/img/winter.png", "../static/img/christmaswall.png")
    backroundURL = backroundlist[random.randint(0, 2)]
    cookie = request.cookies.get("visitedDoors")

    for i in range(1, 25):

        if ck.numberinstring(i, cookie):
            door = {
                "nr": i,
                "doorClass": "door open",
                "yPos": random.randint(-10, 11),
                "xPos": random.randint(-4, 94),
                "id":0
            
            }
        else:
            door = {
                "nr": i,
                "doorClass": "door closed",
                "yPos": random.randint(-10, 11),
                "xPos": random.randint(-4, 94),
                "id":0
            }
        random.shuffle(doorlist)
        doorlist.append(door)
    for i in range(0,24):
        door = doorlist[i]
        door["id"] = i



    day, month = getDate()
    
    return render_template("start.html", title=title, tuerliste=doorlist, heute=date, d1=day, m1=month, bild=backroundURL)


@app.route("/tuer/<int:nr>")
def tuer(nr):
    """
    renders tueren.html corresponding to the door with number that was clicked
    @param nr door that was clicked
    @return schummler if nr is greater than current date
    """

    title = "ORDIX 2022 Adventskalender"

    x = dbc.getTask(nr)

    m1 = getDate()[1]
    d1 = getDate()[0]

    if nr <= d1:
        resp = make_response(render_template("tueren.html", nr=nr, x=x[0], d1=d1, m1=m1, title=title))
        resp = ck.handlecookie(resp, nr)
        return resp

    return "Schummlder"

@app.route("/loesungen/<int:nr>")
def loesung(nr):

    """
    renders loesungen.html corresponding to the door with number that was clicked
    checks for current Date - 1 
    @param nr door that was clicked
    @return schummler if nr is greater than current date - 1
    """

    title = "ORDIX 2022 Adventskalender"

    x = dbc.getAnswer(nr)

    m1 = getDate()[1]
    d1 = getDate()[0]
    

    if nr <= d1 - 1:
        return render_template("loesungen.html", nr=nr, m1=m1, d1=d1, title=title, x=x[0], )

    return "schummler"
    