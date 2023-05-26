from flask import Flask, render_template, request
from flask import url_for
import sqlite3
app = Flask(__name__, template_folder='template')

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# from markupsafe import escape

# @app.route("/<name>")
# def hello(name):
#     return f"Hello, {escape(name)}!"

# @app.route("/student_search")
# def student_search():
#     return "Student Search"

# with app.test_request_context():
#     print(url_for("hello_world"))
#     print(url_for("hello", name="444"))
#     print(url_for("student_search"))


@app.route('/enternew')
def new_student():
    return render_template('student.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            rn = request.form['rn']
            fn = request.form['fn']
            ln = request.form['ln']
            ge = request.form['ge']
            em = request.form['em']
            ci = request.form['ci']
            
            with sqlite3.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO records (rollno,firstname,lastname,gender,email,city) VALUES (?,?,?,?,?,?)",(rn,fn,ln,ge,em,ci) )          
                con.commit()
                msg = "Record successfully added"      
        except:
            con.rollback()
            msg = "Error in insert operation"
        finally:
            con.close()
            return render_template("result.html",msg = msg)
        
@app.route('/liststudents')
def listStudents():
   con = sqlite3.connect("database.db")
   con.row_factory = sqlite3.Row
   cur = con.cursor()
   cur.execute("select * from records")
   rows = cur.fetchall();
   return render_template("studentlist.html",rows = rows)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/stud', methods=['GET', 'POST'])
def stud():
    roll = request.args.get('rn')
    fn = request.args.get('fn')
    ln = request.args.get('ln')
    ge = request.args.get('ge')
    em = request.args.get('em')
    ci = request.args.get('ci')
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from records where rollno=? OR firstname = ? OR lastname = ? OR gender = ? OR email = ? OR city = ?",(roll,fn,ln,ge,em,ci))
    rows = cur.fetchall();

    con.close()
    
    if rows:
        return render_template("khol.html", rows = rows)
    else:
        return render_template("nahi.html")


app.debug = True 
app.run()