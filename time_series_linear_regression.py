import pandas as pd
import numpy as np

#importo el dataset

df = pd.read_csv("D:/KAGGLE/book_sales.csv", 
                 index_col='Date',
                 parse_dates=['Date']).drop('Paperback',axis=1)

print(df.head)
