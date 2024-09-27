import pandas as pd

url = "https://raw.githubusercontent.com/akmand/datasets/main/iris.csv"
dataframe = pd.read_csv(url)
dataframe.head(5)
