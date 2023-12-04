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

val5=data7.Avg_Price
sb.boxplot(val5,palette='hls')
plt.title('Average Price Anaysis')
plt.xlabel('Average Price')
plt.xticks([0],['Central Tendency'])
plt.ylabel('Prices')

sb.lineplot(y=new.Total_Spend,x=new.index,color='g')
plt.xticks(new.index,mon,rotation=60)
plt.title("Total Spend With Month")

sb.lineplot(y=new.Online_Spend,x=new.index,color='pink')
plt.xticks(new.index,mon,rotation=60)
plt.title("Total Online Spend With Month")

delivery=data7[['Delivery_Charges','Month']].groupby('Month').sum()
sb.barplot(data=delivery,x=delivery.index,y='Delivery_Charges',palette='coolwarm')
plt.xticks(delivery.index,mon,rotation=60)
plt.title("Total Delivery Charges per Month")

import matplotlib.pyplot as plt


new1 = data7.groupby('Product_Category').size()


fig, ax = plt.subplots()


new1.sort_values().plot(kind='barh', color='skyblue', edgecolor='black', ax=ax)


for index, value in enumerate(new1.sort_values()):
    ax.text(value, index, f'{value/sum(new1)*100:.2f}%', va='center')

# Set labels and title
ax.set_xlabel('Frequency')
ax.set_ylabel('Product Category')
plt.title("Product Category Frequency Analysis")

# Show the plot
plt.show()




