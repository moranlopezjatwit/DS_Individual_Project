import pandas as pd
import seaborn as sb
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

data7=pd.read_csv("/kaggle/input/online-shopping-dataset/file.csv")

data7=data7.dropna()

data7.Month.info()

data7.duplicated().value_counts()

data8=data7[:]

data7.CustomerID.nunique()

data7.drop(['Transaction_ID','Product_SKU','Transaction_Date','Date'],axis=1,inplace=True)

data7=data7.drop_duplicates()

data7['Total Prices']=data7.Avg_Price+data7.Delivery_Charges

val1=data7['Total Prices']

val1=data7[['CustomerID','Total Prices']]

val1=val1.sort_values(by='Total Prices',ascending=False)
sb.barplot(x=val1.CustomerID.head(40),y=val1['Total Prices'].head(40),palette='hot')
plt.xticks(rotation=90)
plt.title("Maximum Price Customer Id")

val2=data7.CustomerID.value_counts().sort_values(ascending=False).head(30)
sb.barplot(x=val2.index,y=val2,palette='rainbow')

plt.xticks(rotation=90)
plt.ylabel('No. of Purchases')
plt.title('Top 30 Popular Customer ID with Purchase Count')



