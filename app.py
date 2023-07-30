from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

#Code goes below here
config = {
  'apiKey': "AIzaSyCDeIwgP6BcZLCnqIOA-41jRm4U6SkCPBo",
  'authDomain': "esha-le-esha.firebaseapp.com",
  'projectId': "esha-le-esha",
  'storageBucket': "esha-le-esha.appspot.com",
  'messagingSenderId': "537908405410",
  'appId': "1:537908405410:web:e6cda3c540ba6fd62b23fb",
  'measurementId': "G-DK1D72K916",
  "databaseURL":'https://esha-le-esha-default-rtdb.europe-west1.firebasedatabase.app/'
};


firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        username=request.form['username']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email,password)
            user={"email":email,"password":password,"username":username}
            UID = login_session['user']['localId']
            db.child("Users").child(UID).set(user)
            return redirect(url_for('youhelp'))
        except:
            return redirect(url_for('signup'))
    return render_template("signup.html")

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['Email']
        password = request.form['Password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('youhelp'))
        except:
            return redirect(url_for('youhelp'))
    return render_template("signin.html")




@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        Title = request.form['Title']
        story=request.form['story']
        UID = login_session['user']['localId']
        try:
            post1 = {"Title":Title,
                     "story":story,
                     "UID":UID,}

            db.child("stories").push(post1)
            return redirect(url_for('display'))
        except Exception as e:
            print(e)
    return render_template("post.html")




@app.route('/display',methods=['GET', 'POST'])
def display():
    
    Stories=db.child("stories").get().val()
    return render_template("display.html", Stories=Stories)



# @app.route('/change',methods=['GET', 'POST'])
# def change():
#     if request.method == 'POST':
#         username=request.form['username']
#         bio=request.form['bio']
#         pfp = request.form['pfp']


#         try:
#             UID = login_session['user']['localId']
#             changed_user={"username":username,"bio":bio,"pfp":pfp}
#             db.child("Users").child(UID).update(changed_user)
#             return redirect(url_for('profile'))  
#         except:
#             return redirect(url_for('change'))
#     return render_template("change.html")




@app.route('/statistics')
def statistics():
    return render_template("statistics.html")

@app.route('/youhelp')
def youhelp():
    return render_template("youhelp.html")

@app.route('/signout')
def signout():
    login_session['user'] = None
    auth.current_user = None
    return redirect(url_for('signin'))







#Code goes above here

if __name__ == '__main__':
    app.run(debug=True)