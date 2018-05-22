from flask import Flask, render_template
import pymysql

app = Flask(__name__)

@app.route('/')
def hello():
    db = pymysql.connect(
            host='db',
            user='root',
            password='root',
            db='flask',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
        )

    cur = db.cursor()
    sql = "select * from users"
    cur.execute(sql)
    users = cur.fetchall()

    cur.close()
    db.close()

    return render_template('index.html', title='flask on docker', users=users)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
