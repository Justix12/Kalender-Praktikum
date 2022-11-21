from flask import Response, request


def numberinstring(nr: int, string: str):
    """
    checks for numbers in string
    @param: nr int Nuber to be checked
    @param: string str string containing number
    @return boolean true if number is in string
    """


    visited = ""
    if string:
        visited = string.split(":")

    for door in visited:
        if nr == int(door):
            return True

    return False


def handlecookie(resp: Response, nr: int):
    """
    checks/creates cookies
    @param resp sets cookie
    @param nr door that was visited
    @return return cookie 
    
    """


    cookie = request.cookies.get("visitedDoors")

    if cookie == None:
        resp.set_cookie("visitedDoors", str(nr))
        return resp

    if numberinstring(nr, cookie):
        return resp

    resp.set_cookie("visitedDoors", cookie + ":" + str(nr))
    return resp
