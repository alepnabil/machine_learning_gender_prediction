from os import name
import re
from flask import Flask,render_template,request
import joblib
from joblib import load
import numpy as np
import pandas as pd


app = Flask(__name__)
model=joblib.load('model1')

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/",methods=['POST'])
def predict():
    if request.method=='POST':
        long_hair=request.form['hair_long']
        if(long_hair=='Yes'):
            long_hair=1
        else:
            long_hair=0

        forehead_width=request.form['forehead_width']
        forehead_height=request.form['forehead_height']

        nose_wide=request.form['nose_wide']
        if(nose_wide=='Yes'):
            nose_wide=1
        else:
            nose_wide=0

        nose_long=request.form['nose_long']
        if(nose_long=='Yes'):
            nose_long=1
        else:
            nose_long=0
            
        lips_thin=request.form['lips_thin']
        if (lips_thin=='Yes'):
            lips_thin=1
        else:
            lips_thin=0
        
        nose_lip_distance=request.form['nose_lip_distance']
        if(nose_lip_distance=='Yes'):
            nose_lip_distance=1
        else:
            nose_lip_distance=0

        prediction=model.predict([[long_hair,forehead_width,forehead_height,nose_wide,nose_long,lips_thin,nose_lip_distance]])
            
        if(prediction==1):
             return render_template('index.html', prediction_text='You are a man.')
        else:
              return render_template('index.html', prediction_text='You are a woman.')
    else:
        return render_template("index.html")
    



if __name__=='__main__':
    app.run(debug=True)
