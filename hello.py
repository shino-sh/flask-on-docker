from flask import Flask, redirect, render_template, request
import pymysql

app = Flask(__name__)

db = pymysql.connect(host='db',
                     user='root',
                     password='root',
                     db='flask',
                     charset='utf8',
                     cursorclass=pymysql.cursors.DictCursor)

@app.route('/')
def index():
    with db.cursor() as cursor:
        sql = "SELECT * FROM users"
        cursor.execute(sql)
        users = cursor.fetchall()

    return render_template('index.html', title='flask on docker', users=users)

@app.route('/', methods=['POST'])
def create():
    _id = request.form['id']
    name = request.form['name']

    with db.cursor() as cursor:
        sql = "INSERT INTO users (id, name) VALUES (%s, %s)"
        cursor.execute(sql, (_id, name))
        db.commit()

    return redirect('/', code=302)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
