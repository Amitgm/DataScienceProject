from flask import Flask, request, jsonify,render_template,url_for

import numpy as np
import pandas as pd
import os

from src.datascience.pipeline.prediction_pipeline import PredictionPipeline

app = Flask(__name__)

# HOME PAGE
@app.route('/', methods=['GET'])
def home():

    return render_template('index.html')

# TO TRAIN THE MODEL
@app.route('/train', methods=['GET'])
def train():

    os.system("python main.py")

    return jsonify({"message": "Model trained successfully"})

@app.route('/predict', methods=['POST',"GET"])
def index():

    if request.method == 'POST':

        try:

            fixed_acidity =float(request.form['fixed_acidity'])
            volatile_acidity =float(request.form['volatile_acidity'])
            citric_acid =float(request.form['citric_acid'])
            residual_sugar =float(request.form['residual_sugar'])
            chlorides =float(request.form['chlorides'])
            free_sulfur_dioxide =float(request.form['free_sulfur_dioxide'])
            total_sulfur_dioxide =float(request.form['total_sulfur_dioxide'])
            density =float(request.form['density'])
            pH =float(request.form['pH'])
            sulphates =float(request.form['sulphates'])
            alcohol =float(request.form['alcohol'])

            # the data is 1 row with many columns so reshape it

            data = [fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol]

            # reshaping the 2d array data 
            data = np.array(data).reshape(1, 11)

            obj = PredictionPipeline()

            predict = obj.predict(data)


            return render_template('results.html', prediction = str(predict))


        except Exception as e:

            raise "Something is wrong"
        
    else:

        return render_template('index.html')
    

if __name__ == '__main__':

    app.run(host="0.0.0.0", port = 8080)








