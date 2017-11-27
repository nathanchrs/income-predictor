from sklearn.externals import joblib

class Predictor:
	def __init__(self):	
		 self.model = joblib.load('./model/mlp_model.pkl')
	def predict(self, data):
		prediction = self.model.predict(data)
		return prediction