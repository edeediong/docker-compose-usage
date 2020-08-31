from flask import Flask, render_template, request
import  mysql.connector
import json

app = Flask(__name__)


config = {
    'host': 'mysql',
    'user': 'user',
    'password': 'password1212',
    'port': '3306',
    'database': 'data',
    'auth_plugin':'mysql_native_password'
}

connection = mysql.connector.connect(**config)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']
        cur = connection.cursor()
        cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')


if __name__ == '__main__':
    app.run()