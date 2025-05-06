import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression, Ridge  
from sklearn.metrics import mean_absolute_error
from sklearn.pipeline import make_pipeline

df = pd.read_csv('Housing.csv')
X = df.drop(columns=['price'])
y = df['price']

# print(X.value_counts())