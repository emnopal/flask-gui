from flask import Flask, request, render_template
from gevent.pywsgi import WSGIServer
from models.predict import get_model_predict, model_predict, \
                           model_path, byte_array_predict,\
                           get_predict, image_predict, get_labels

app = Flask(__name__)

LABEL_PATH = "models/labels.txt"
class_names_long = get_labels(LABEL_PATH)

MODEL_PATH = 'models/model.h5'
model = model_path(MODEL_PATH)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        preds = model_predict(request.json, model)
        final = get_model_predict(preds, class_names_long)
        return final
    return


@app.route('/predict/base64', methods=['GET', 'POST'])
def predict_bytearray():
    if request.method == 'POST':
        img = request.json['base64-img']
        preds = byte_array_predict(img, model)
        final = get_predict(preds, class_names_long)
        return final
    return


@app.route('/predict/curl', methods=['GET', 'POST'])
def predict_curl():
    if request.method == 'POST':
        img = request.files['img']
        preds = image_predict(img, model)
        final = get_predict(preds, class_names_long)
        return final
    return


@app.route('/predict/image', methods=['GET', 'POST'])
def predict_image():
    if request.method == 'POST':
        img = request.json['img']
        preds = image_predict(img, model)
        final = get_predict(preds, class_names_long)
        return final
    return


@app.route('/info', methods=['GET', 'POST'])
def information():
    print("Pre-trained model yang dipakai disini adalah Xception")
    print(f"Dengan 7 Class: {class_names_long}")


if __name__ == '__main__':
    print("Ke http://127.0.0.1:5000 untuk membuka program")
    print("CTRL + C untuk menutup server")
    http_server = WSGIServer(('0.0.0.0', 5000), app)
    http_server.serve_forever()
