from flask import Flask, render_template, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'

@app.route('/')
def home():
    return render_template('home.html', agora=datetime.now())

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)