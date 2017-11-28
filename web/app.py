from flask import Flask
from flask import render_template
from flask import request
from classes.Preprocessor import Preprocessor
from classes.Predictor import Predictor
from sklearn.externals import joblib
import json

def bootloader():
	global model, preprocessor, predictor
	predictor = Predictor()
	preprocessor = Preprocessor()

app = Flask(__name__, static_folder='./public')

@app.route("/")
def index():
    return render_template("index.html", features_names=preprocessor.feature_names, discrete_feature_domains = preprocessor.discrete_feature_domains)

@app.route("/predict", methods=['POST'])
def predict():
	data = request.get_json(silent=True)
	encoded = preprocessor.encodeData(data)
	result = predictor.predict(encoded)
	return(result[0])

@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)

if __name__ == "__main__":
	bootloader()
	app.run()