from flask import Flask, request, render_template
from models import Predict
from app import WebUI
from src import MODEL_FILE, LABEL_FILE, APP_NAME, IS_DEBUG

app = Flask(__name__)

ui = WebUI(app, debug=IS_DEBUG(), app_name=APP_NAME)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    pred = Predict(MODEL_FILE, LABEL_FILE)
    return pred.get_predicted_images(request.json)


@app.route('/predict/base64', methods=['POST'])
def predict_bytearray():
    pred = Predict(MODEL_FILE, LABEL_FILE)
    return pred.get_predicted_images(request.json['base64-img'], mode='byte')


@app.route('/predict/curl', methods=['POST'])
def predict_curl():
    pred = Predict(MODEL_FILE, LABEL_FILE)
    return pred.get_predicted_images(request.json['base64-img'], mode='img')


@app.route('/predict/image', methods=['POST'])
def predict_image():
    pred = Predict(MODEL_FILE, LABEL_FILE)
    return pred.get_predicted_images(request.json['base64-img'], mode='img')


@app.route('/info', methods=['GET', 'POST'])
def information():
    pred = Predict(MODEL_FILE, LABEL_FILE)
    print("Pre-trained model yang dipakai disini adalah Xception")
    print(f"Dengan 7 Class: {pred.get_label()}")

