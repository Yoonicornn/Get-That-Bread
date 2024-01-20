from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import pandas as pd 
import numpy as np  

SandP500 = pd.read_csv("S&P500.csv")

data = SandP500.iloc[:, 0].values.reshape(-1, 1)  # Assuming the first column is the feature
target = SandP500.iloc[:, 1].values

train_input, test_input, train_target, test_target = train_test_split(data, target, test_size=0.2, random_state=42)


ss = StandardScaler()
train_scaled = ss.fit_transform(train_input)
test_scaled = ss.transform(test_input)

lr = LinearRegression()
lr.fit(train_scaled, train_target)

new = ss.transform([[100]])

pred = lr.predict(new)
print(pred)