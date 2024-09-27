import pandas as pd
from sklearn import preprocessing
url = "https://raw.githubusercontent.com/akmand/datasets/master/iris.csv"
dataframe = pd.read_csv(url)
scaler_minmax = preprocessing.MinMaxScaler()
scaler_z = preprocessing.StandardScaler()
dataframe[['sepal_length_cm']] = scaler_minmax.fit_transform(dataframe[['sepal_length_cm']])
dataframe[['sepal_width_cm']] = scaler_z.fit_transform(dataframe[['sepal_width_cm']])
dataframe.head(10)