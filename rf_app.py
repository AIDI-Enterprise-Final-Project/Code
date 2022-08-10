import numpy as np
import pickle
from rf_classify import predict_review
from flask import Flask, render_template, request


with open(r"rfmodel.pkl", "rb") as input_file:
    model = pickle.load(input_file)     # load trained model

with open('vectorizer.pkl', 'rb') as handle:
    _vectorizer = pickle.load(handle)   # load tokenizer
 
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        input_sentence = request.form["message"]  # get sentence from textarea
        print(type(input_sentence))
        print(input_sentence)
        pred = predict_review(model, input_sentence, _vectorizer) # get prediction
    
    
    return render_template('index.html', text = "Prediction result", prediction_res = pred)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port = 8080)
