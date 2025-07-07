import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split

def load_raw_data():
    return pd.read_csv("data/raw/train.csv")

def add_features(df):
    return df

# this is to preprocess the data for xgboost and the like, since trees handle data a little bit differently
def preprocess_for_tree(df):
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