from flask import Flask, render_template, request, redirect, url_for
from database import conn, cursor


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/submit', methods = ['POST'])

def submit():

    name = request.form['name']
    email = request.form['email']
    rating = request.form['rating']
    message = request.form['message']
    

    query = "INSERT INTO feedback (name, email, rating, message) VALUES(%s, %s, %s, %s)"

    cursor.execute(query, (name, email, rating, message))

    conn.commit()
    

    return render_template('success.html')



@app.route('/view')
def view():

    cursor.execute("SELECT * FROM feedback ORDER BY id DESC")

    feedback = cursor.fetchall()

    return render_template('view.html', feedback=feedback)


if __name__ == '__main__':
    app.run(debug=True)