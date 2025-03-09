import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Diwali Sales Data.csv', encoding='latin1')
print('Shape of the data:\n',df.shape)
print('\nFirst 5 rows:\n',df.head())
print('\nDataset information:\n',df.info())

# Data Cleaning
# Drop unrelated/blank columns
df.drop(['Status', 'unnamed1'], axis=1, inplace=True)
print('\nChecking null values:\n',df.isnull().sum())

# Drop rows with null values
print('\nShape of the data before dropping null values:',df.shape)
df.dropna(inplace=True)
print('\nShape of the data after dropping null values:',df.shape)

# Change data type of columns
df['Amount'] = df['Amount'].astype('int')
print('\nData type of Amount column:',df['Amount'].dtype)

# Rename columns
print('\nColumns before renaming:\n',df.columns)
df.rename(columns={'Marital_Status' : 'Marrige_Status'})

# describe() method returns description of the data in the DataFrame (like cont, mean, std, etc)
print('\nDesctiption of the data:\n', df.describe())

# Use describe() for specific columns
print(df[['Age', 'Orders', 'Amount']].describe()) 

# Exploratory Data Analysis
# Gender
ax = sns.countplot(x = 'Gender', data = df)
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
print(sales_gen)
sns.barplot(x='Gender', y='Amount', data=sales_gen)
plt.show()
# From the above graphs we can see that most of the buyers are females and even the purchasing power of females are greater than men.

# Age
age = sns.countplot(data=df, x='Age Group', hue='Gender')
for bars in age.containers:
    age.bar_label(bars)
plt.show()

# Total amount vs Age Group
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x='Age Group', y='Amount', data=sales_age)
plt.show()
# From above graphs we can see most of the buyers are of age group between 26-35yrs female

# State
# Total number of orders from top 10 states
sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15, 5)})
sns.barplot(data=sales_state, x='State', y='Orders')
plt.show()

# Total amount/sales from top 10 states
sales_states = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15, 5)})
sns.barplot(data=sales_states, x='State', y='Amount')
plt.show()

# Marital Status
ax = sns.countplot(data=df, x='Marital_Status')

for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

# Marital Status vs Amount
sales_marital = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data=sales_marital, x='Marital_Status', y='Amount', hue='Gender')
plt.show()

# Occupation
sns.set(rc={'figure.figsize':(20, 5)})
ax = sns.countplot(data=df, x='Occupation')

for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

# Occupation vs Amount
sales_occ = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data=sales_occ, x='Occupation', y='Amount')
plt.show()

# Product Category
sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data=df, x='Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

# Product Categeory vs Amount
sales_prod = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data=sales_prod, x='Product_Category', y='Amount')
plt.show()

# Top Selling Products on Product_ID
sales_prod_id = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data=sales_prod_id, x='Product_ID', y='Orders')
plt.show()

# Top 10 most sold products 
fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')
plt.show()