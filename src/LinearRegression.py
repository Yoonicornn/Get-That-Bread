from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import pandas as pd 
import numpy as np  
from app import input_to_index_bread, input_to_index_sp

def predict_price(csv_file, year, month):
    csv = pd.read_csv(csv_file)

    data = csv.iloc[:, 0].values.reshape(-1, 1)  # Assuming the first column is the feature
    target = csv.iloc[:, 1].values

    train_input, test_input, train_target, test_target = train_test_split(data, target, test_size=0.2, random_state=42)


    ss = StandardScaler()
    train_scaled = ss.fit_transform(train_input)
    test_scaled = ss.transform(test_input)

    lr = LinearRegression()
    lr.fit(train_scaled, train_target)
    index = 0
    if csv_file == "WhiteBread.csv":
        index = input_to_index_bread(year, month)
    else:
        index = input_to_index_sp(year, month)
    new = ss.transform([[index]])

    pred = lr.predict(new)
    print(pred)

if __name__ == "__main__":
    predict_price("WhiteBread.csv", 2030, 1)
    predict_price("S&P500.csv", 2030, 1)