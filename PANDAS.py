import pandas as pd 


df = pd.read_csv("RealEstate-USA1.csv",delimiter=',')
df.set_index("brokered_by")
print(df)

#print datatype
print("df-datatypes",df.dtypes)
#print data info
print("df.info" , df.info)
#print statics operations
print("statics operations",df.describe())
#printing no of rows and columns
print("no of rows and columns",df.shape)
#dispaly the first seven rows
print("first seven rows")
print(df.head(7))
#display the nine rows
print("last nine rows")
print(df.tail(9))
#access a column
city=df['city']
print("city")
#access another column
street=df['street']
print("street")
#access multiple columns
city_street=df[['city','street']]
print(city_street)
#selecting a row using.loc
second_row=df.loc[52707]
print(second_row)
print()
#selecting multiple column using.loc
row=df.loc[[103378,1205]]
print(row)
print()
#conditional selection of rows
n=df.loc[df['city']=='Adjuntas']
print(n)
#selecting a coloumn using .loc


