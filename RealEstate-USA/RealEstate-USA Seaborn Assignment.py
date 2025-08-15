import seaborn as sns
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("RealEstate-USA1.csv",delimiter=',')
df.set_index("brokered_by")
df = df.reset_index(drop=True)
print(df)

#print datatype
print("df-datatypes",df.dtypes)
#print data info
print("df.info" , df.info)
#print statics operations
print("statics operations",df.describe())
#printing no of rows and columns
print("no of rows and columns",df.shape)

sns.set_theme(style="darkgrid")
sns.lineplot(x='city',y='price',data=df)
plt.show()