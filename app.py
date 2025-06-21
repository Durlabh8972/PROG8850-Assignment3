
from flask import Flask, render_template, request, redirect, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MySQL configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Dkt@123',
    'database': 'prog8850db'
}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            conn.commit()
            flash('User added successfully!', 'success')
        except mysql.connector.Error as err:
            flash(f"Database error: {err}", 'danger')
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

        return redirect('/login')
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
