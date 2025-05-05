import pandas as pd
df = pd.read_csv('/Users/vishwanthgollapally/Desktop/python-practice/pandas_practise/currency.csv')
print(df.head())
print(df.info())
print(df.describe())

# filter rows
data = {'name':['vishwanth','barck','chirak','marak'],
        'age':[27,26,56,66]}
df=pd.DataFrame(data)
elders=df[df['age'] >50]

print(elders)


#add a new column 
data ={'mobile':['samsung','apple','oneplus'],
       'quanity':[10,20,30],
       'price':[1000,2000,2500]}
df= pd.DataFrame(data)

df['total value'] = df['quanity']*df['price']
print(df)

#grouping and aggregation 
data = {'product': ['A', 'B', 'A', 'B', 'C'],
        'quantity': [10, 5, 7, 3, 8]}
df= pd.DataFrame(data)
grouped=df.groupby('product').sum()
print(grouped)


# handling missing values with mean 
bata = {'name':['vishwanth','barck','chirak','marak'],
        'age':[27,None,56,None]}
df= pd.DataFrame(bata)
mean_age= df['age'].mean()
df['age']=df['age'].fillna(mean_age)
print(df)



