
import pandas as pd

def drop_outliers_IQR(df):

   q1=df.quantile(0.25)

   q3=df.quantile(0.75)

   IQR=q3-q1

   df = df[~((df<(q1-1.5*IQR))|(df>(q3+1.5*IQR))).any(axis=1)]

   return df



#load the data into a dataframe

df = pd.read_csv('heart.csv')
df = drop_outliers_IQR(df)
print (df.shape)
