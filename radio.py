from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///test.db"
app.config['SECRET_KEY'] = "FDSAFASFDSAF"
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    gender = db.Column(db.String(10))


@app.route("/")
def home():
    return "Dis is home page"


@app.route("/home", methods=['POST','GET'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        gender = request.form['gender']
        new_values = User(name=name,gender=gender)
        db.session.add(new_values)
        db.session.commit()
        return "record created"
    return render_template("radio.html")



@app.route("/create")
def create():
    db.create_all()
    return "db created"

@app.route("/delete")
def delete():
    return "database deleted"

if __name__=='__main__':
    app.run(debug=True)
