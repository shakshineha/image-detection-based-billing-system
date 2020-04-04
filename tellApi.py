import os, sys, warnings
if not sys.warnoptions:
    warnings.simplefilter("ignore")
from flask import Flask, request, send_file
from imageai.Prediction.Custom import CustomImagePrediction

execution_path = os.getcwd()

def detect():
	prediction = CustomImagePrediction()
	prediction.setModelTypeAsResNet()
	prediction.setModelPath("model90.h5")
	prediction.setJsonPath("model_class.json")
	prediction.loadModel(num_objects=14)
	predictions, probabilities = prediction.predictImage(".jpg", result_count=1)

	for eachPrediction, eachProbability in zip(predictions, probabilities):
		item = eachPrediction
	
	return item

app = Flask(__name__)

@app.route("/")
def hello():
	return detect()


if __name__ == '__main__':
    app.run(debug=True, port=85)