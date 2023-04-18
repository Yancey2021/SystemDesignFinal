from flask import Flask, url_for, redirect, render_template, request
from flask_bootstrap import Bootstrap
import sqlite3 as sql

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def home(): 
    return render_template("welcome.htm")

@app.route("/enterinfo")
def new_reservation():
    return render_template("reservation.htm")

@app.route("/addrec", methods = ["POST", "GET"])
def addrec(): 
    if request.method == "POST": 
        nm = request.form["nm"]
        CheckInDate = request.form["CheckInDate"]
        CheckOutDate = request.form["CheckOutDate"]
        RoomType = request.form["RoomType"]

        cmd = "INSERT INTO Reservation (name, CheckInDate, CheckOutDate, RoomType) VALUES ('{0}', '{1}', '{2}', '{3}')".format(nm, CheckInDate, CheckOutDate, RoomType)
        with sql.connect("BradfordHotel.db") as conn:
            cur = conn.cursor()
            cur.execute(cmd)
            conn.commit()
            msg = "Reservation Successfully Completed."
            return render_template("confirm.htm", msg = msg) 

@app.route("/list")
def list():
    conn = sql.connect("BradfordHotel.db")
    conn.row_factory = sql.Row 

    cmd = "SELECT * FROM Reservation"
    cur = conn.cursor()
    cur.execute(cmd)
    rows = cur.fetchall()
    conn.close()
    return render_template("reservationlist.htm", rows = rows)

if __name__ == "__main__":
    app.run(debug = True)
