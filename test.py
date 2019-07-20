import  pandas as pd
import pickle

cv = pickle.load(open("vocab.pkl", "rb"))
from sklearn.externals import joblib
loaded_model = joblib.load('model.pkl')

xx = ['''I am well'''.lower()]
X_data = cv.transform(xx)
x = loaded_model.predict(X_data)
print(x)