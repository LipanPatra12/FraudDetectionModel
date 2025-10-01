import pickle
from flask import Flask,request,render_template

import pandas as pd
import numpy as np


pickled_model=pickle.load(open('rfmodel.pkl', 'rb'))


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict",methods=['POST'])
def predict():
    data=[float(value) for value in request.form.values()]
    res =pickled_model.predict([data])
    if res[0]==1:
        return "⚠️ Fraud detected!"
    else:
        return "✅ No fraud detected."
   

if __name__=='__main__':
    app.run(host="0.0.0.0",port=7000)

