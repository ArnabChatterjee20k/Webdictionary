from flask import Flask,request,render_template
from PyDictionary import *
app=Flask("1")
@app.route("/",methods=["POST","GET"])
def mean():
    return render_template("dic.html")
@app.route("/meaning",methods=["POST","GET"])
def m():
    if request.method == "POST":
        operation=request.form["operation"]
        try:
            a="Meaning of"
            search = request.form["search"]
            mean = PyDictionary.meaning(search)
            if search!="" and operation=="eng":
                return render_template("dic.html",mean=mean,search=search,a=a)
            elif operation=="other" and search!="":
                trans=PyDictionary(search)
                data={"Synonym":PyDictionary.synonym(search),
                        "Antonym":PyDictionary.antonym(search)}
                return render_template("dic.html",data=data)
            else:
                nothing="Nothing entered"
                return render_template("dic.html",nothing=nothing)
        except:
            error=["Check your connection","See the typed word"]
            return render_template("dic.html", error=error)



app.run(debug=True)