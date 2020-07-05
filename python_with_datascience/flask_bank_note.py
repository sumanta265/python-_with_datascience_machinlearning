# -*- coding: utf-8 -*-
"""
Created on Thu May 21 20:56:23 2020

@author: SUMANTA KR MAJI
"""

from flask import Flask, request
import numpy as np
import pickle
import pandas as pd



app=Flask(__name__)



pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Welcome All"

@app.route('/hi')
def jio():
    return "Welcome sumanta"




@app.route('/predict',methods=["Get"])
def predict_note_authentication():

    variance=request.args.get("variance")
    skewness=request.args.get("skewness")
    curtosis=request.args.get("curtosis")
    entropy=request.args.get("entropy")
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    
    return "Hello The answer is"+str(prediction)


if __name__=='__main__':
    app.run()



