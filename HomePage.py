from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
from model.MedicineModel import predict_using_model
import pandas as pd




from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict")
def predictionPage():
    return render_template("predict.html")

@app.route("/get")
def predictionResponse():
    userText = request.args.get('msg')
    new_data = pd.DataFrame({'Description': [str(userText)]})
    new_data:str = str(predict_using_model(new_data)[0])
    pos = new_data.find("\'S")
    if(pos == -1):
        pos = int(len(new_data) - 3)
    return new_data[:pos+2]

if __name__ == "__main__":
    app.run(debug=True)