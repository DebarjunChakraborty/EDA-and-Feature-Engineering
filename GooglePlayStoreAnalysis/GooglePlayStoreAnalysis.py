# %%
import pandas as pd

# %%
data=pd.read_csv('googleplaystore.csv')

# %% [markdown]
# Display Top 5 Rows of The Dataset

# %%
data.head()

# %% [markdown]
# Check Last 3 Rows of The Dataset

# %%
data.tail(3)

# %% [markdown]
# Find Shape of Our Dataset

# %%
data.shape

# %%
print("Number of Rows",data.shape[0])
print("Number of Columns",data.shape[1])

# %% [markdown]
# Get Information About Our Dataset

# %%
data.info()

# %% [markdown]
# Overall Statistics About The Dataframe

# %%
data.describe(include='all')

# %% [markdown]
# Total Number of App Titles Contain Astrology

# %%
data.columns

# %%
len(data[data['App'].str.contains('Astrology',case=False)])

# %% [markdown]
# Average App Rating

# %%
data.columns

# %%
data['Rating'].mean()

# %% [markdown]
# Total Number of Unique Category

# %%
data.columns

# %%
data['Category'].nunique()

# %% [markdown]
# Which Category Gets The Highest Average Rating?

# %%
data.columns

# %%
data.groupby('Category')['Rating'].mean().sort_values(ascending=False)

# %% [markdown]
# Total Number of Apps having 5 Star Rating

# %%
data.columns

# %%
len(data[data['Rating']==5.0])

# %% [markdown]
# Average Value of Reviews

# %%
data.columns

# %%
data[data['Reviews']=='3.0M']

# %%
data['Reviews']=data['Reviews'].replace('3.0M',3.0)

# %%
data['Reviews']=data['Reviews'].astype('float')

# %%
data['Reviews'].dtype

# %%
data['Reviews'].mean()

# %% [markdown]
# Total Number of Free and Paid Apps

# %%
data.head(1)

# %%
data['Type'].value_counts()

# %% [markdown]
# Which App Has Maximum Reviews?

# %%
data.columns

# %%
data[data['Reviews'].max()==data['Reviews']]['App']

# %% [markdown]
# Top 5 Apps Having Highest Reviews

# %%
index=data['Reviews'].sort_values(ascending=False).head().index

# %%
data.iloc[index]['App']

# %% [markdown]
# Average Rating of Free and Paid Apps

# %%
data.head(1)

# %%
data.groupby('Type')['Rating'].mean()

# %% [markdown]
# Top 5 Apps Having Maximum Installs

# %%
data.head(1)

# %%
data['Installs_1']=data['Installs'].str.replace(',','')

# %%
data.head(1)

# %%
data['Installs_1']=data['Installs_1'].str.replace('+','')

# %%
data.head(1)

# %%
data[data['Installs_1']=='Free']

# %%
data['Installs_1']=data['Installs_1'].str.replace('Free','0')

# %%
data['Installs_1']=data['Installs_1'].astype('int')

# %%
data['Installs_1'].dtype

# %%
index=data['Installs_1'].sort_values(ascending=False).head().index

# %%
data.iloc[index]['App']


