import pandas as pd
import numpy as np
import os

def load_raw_data():
    return pd.read_excel("data/raw/credit_data.xls", engine='xlrd', header=1)

# this is to preprocess the data for xgboost and the like, since trees handle data a little bit differently
def general_preprocess(df):
    # this will be empty since the data is already numeric
    return df

# this is to further preprocess the data for standard methods, since I will need to one-hot encode some categories, since they have relatively arbitrary ratings
def encode_features(df):
    # for now i will also leave this blank
    return df

if __name__ == "__main__":
    print('working')
    df = load_raw_data()
    print(df.head())