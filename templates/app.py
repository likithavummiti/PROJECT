from flask import *
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/home')
def home():
    return render_template('index.html')
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    list={'likki':100,'ishu':200,'prassu':3000}
    return render_template('dashboard.html' ,dashboard=list)


if __name__=='__main__':
    app.run(debug=True)