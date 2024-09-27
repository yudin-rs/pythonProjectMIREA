import pandas as pd
url = "https://raw.githubusercontent.com/akmand/datasets/main/iris.csv"
dataframe = pd.read_csv(url)
display(dataframe.head(2))
display(dataframe.tail(2))
display(dataframe.shape)
display(dataframe.describe())
display(dataframe.iloc[1:4])
display(dataframe[dataframe['petal_length_cm']==1.4].head(2))