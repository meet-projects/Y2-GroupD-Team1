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



#Code goes above here

if __name__ == '__main__':
    app.run(debug=True)