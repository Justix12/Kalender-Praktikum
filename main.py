from flask import Flask
from flask import  render_template
import random


app = Flask(__name__)



@app.route("/")
def start():

        title = "Ordix 2022 Adventskalender"
        tuerliste  = []

        for i in range(24):

                if i%2:
                        thisdict= {
                        "nr": i + 1,
                        "farbe": "blue"

                        }
                else:
                        thisdict= {
                        "nr": i + 1,
                        "farbe": "green"
                        }
                tuerliste.append(thisdict)




        botr = random.randint(0,800)
        topr = random.randint(0,800)
        righr = random.randint(0,800)
        lefr = random.randint(0,800)


        return render_template("start.html", title=title, tuerliste=tuerliste, botr=botr)


        


@app.route("/tuer/<int:nr>")
def tuer(nr):


        aufg1 = "aw1"
        aufg2 = "aw2"
        aufg3 = "aw3"
        aufg4 = "aw4"
        aufg5 = "aw5"
        aufg6 = "aw6"
        aufg7 = "aw7"
        aufg8 = "aw8"
        aufg9 = "aw9"
        aufg10 = "aw10"
        aufg11 = "aw11" 
        aufg12 = "aw12"
        aufg13 = "aw13"
        aufg14 = "aw14"
        aufg15 = "aw15"
        aufg16 = "aw16"
        aufg17 = "aw17"
        aufg18 = "aw18"
        aufg19 = "aw19"
        aufg20 = "aw20"
        aufg21 = "aw21"
        aufg22 = "aw22"
        aufg23 = "aw23"
        aufg24 = "aw24"

        aufg = [aufg1,aufg2,aufg3,aufg4,aufg5,aufg6,aufg7,aufg8,aufg9,aufg10,aufg11,aufg12,
                aufg13,aufg14,aufg15,aufg16,aufg17,aufg18,aufg19,aufg20,aufg21,aufg22,aufg23,aufg24]

        

        return render_template("tueren.html", nr=nr, aufg=aufg)
        




if __name__ =="__main__":
    app.run(debug=True)
