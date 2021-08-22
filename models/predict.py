import base64
from io import BytesIO
from tensorflow.keras.models import load_model
from PIL import Image
from flask import jsonify
from utils.util import base64_to_pil

import numpy as np
import os


def model_path(MODEL_PATH):
    return load_model(f"{os.getcwd()}/{MODEL_PATH}")


def get_labels(LABELS_PATH):
	with open(LABELS_PATH, 'r') as label:
		labels = list(map(lambda x:x.strip(), label.readlines()))
		label.close()
	return labels


def model_predict(img_base64, model):
    img = base64_to_pil(img_base64)
    img = img.convert('RGB')
    img = img.resize((150, 150))
    img = np.array(img)
    img = img.astype(np.float32) / 255
    img = np.expand_dims(img, axis=0)
    pred = model.predict(img)
    return pred


def get_model_predict(preds, class_names):
    pred_proba = f"{(np.max(preds))*100:.2f}%"
    pred_class = class_names[np.argmax(preds)]
    return jsonify(result=pred_class, probability=pred_proba)


def image_predict(img, model):
    img = Image.open(img).convert('RGB')
    img = img.resize((150, 150))
    img = np.array(img)
    img = img.astype(np.float32) / 255
    img = np.expand_dims(img, axis=0)
    pred = model.predict(img)
    return pred


def byte_array_predict(img, model):
    img = Image.open(BytesIO(base64.b64decode(img)))
    img = img.resize((150, 150))
    img = np.array(img)
    img = img.astype(np.float32) / 255
    img = np.expand_dims(img, axis=0)
    pred = model.predict(img)
    return pred


def get_predict(preds, class_names):
    pred_proba = f"{(np.max(preds))*100:.2f}%"
    pred_class = class_names[np.argmax(preds)]
    out = {
        'probability': pred_proba,
        'class_result': pred_class
    }
    return jsonify(out)
