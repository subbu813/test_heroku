#install flask
# import

from flask import Flask, render_template,request

import joblib
# load the model
model = joblib.load('predict_79.pkl')




# initilaise the app (code should be written in between initializing the app and running the app)
app = Flask(__name__) 

@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/forms')
def contact():
    return render_template('forms.html')

@app.route('/predict', methods=['post'])
def predict():
    number = request.form.get('phone')
    mail = request.form.get('email')
    name = request.form.get('name')
    result = model.predict([[1,1,1,1,1,1,1,1]])
    if result[0] == 0:
     response='not diabitic'
    else:
     response='diabitic'
    
    return response
#@app.route('/dsa')
#def dsa():
    #return 'welcome to dsa page'

app.run(debug=True)

#http://127.0.0.1:5000/  # http is a protocol, 127.0.0.1 is local IP address and 5000 is port(gate). / is route
# suppose www.google.com like that is domain and it has IP address
