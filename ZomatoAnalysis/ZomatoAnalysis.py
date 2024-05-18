# %% [markdown]
# Zomato Dataset Exploratory Data Analysis

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

# %%
df=pd.read_csv('zomato.csv',encoding='latin-1')
df.head()

# %%
df.columns

# %%
df.info()

# %%
df.describe()

# %% [markdown]
# In Data Analysis What All Things We Do
# 
# 1. Missing Values
# 2. Explore About the Numerical Variables
# 3. Explore About categorical Variables
# 4. Finding Relationship between features

# %%
df.shape

# %%
df.isnull().sum()

# %%
df.isnull().sum()

# %%
[features for features in df.columns if df[features].isnull().sum()>0]

# %%
sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis')

# %%
df_country=pd.read_excel('Country-Code.xlsx')
df_country.head()

# %%
df.columns

# %%
final_df=pd.merge(df,df_country,on='Country Code', how='left')

# %%
final_df.head(2)

# %% [markdown]
# Check Data Types

# %%
final_df.dtypes

# %%
final_df.columns

# %%
country_names=final_df.Country.value_counts().index

# %%
country_val=final_df.Country.value_counts().values

# %% [markdown]
# Top 3 countries that uses zomato

# %%
plt.pie(country_val[:3],labels=country_names[:3],autopct='%1.2f%%')

# %% [markdown]
# Observation: 
# 1. Zomato maximum records or transaction are from India
# 2. After that USA and then United Kingdoms

# %%
final_df.columns

# %%
ratings=final_df.groupby(['Aggregate rating','Rating color','Rating text']).size().reset_index().rename(columns={0:'Rating Count'})

# %%
ratings

# %% [markdown]
# Observation
# 1. When Rating is between 4.5 to 4.9---> Excellent
# 2. When Rating are between 4.0 to 3.4--->very good
# 3. when Rating is between 3.5 to 3.9----> good
# 4. when Rating is between 3.0 to 3.4----> average
# 5. when Rating is between 2.5 to 2.9----> average
# 6. when Rating is between 2.0 to 2.4----> Poor

# %%
ratings.head()

# %%
import matplotlib
matplotlib.rcParams['figure.figsize'] = (12, 6)
sns.barplot(x="Aggregate rating",y="Rating Count",data=ratings)

# %%
sns.barplot(x="Aggregate rating",y="Rating Count",hue='Rating color',data=ratings,palette=['blue','red','orange','yellow','green','green'])

# %% [markdown]
# Observation:
# 1. Not Rated count is very high
# 2. Maximum number of rating are between 2.5 to 3.4

# %%
## Count plot
sns.countplot(x="Rating color",data=ratings,palette=['blue','red','orange','yellow','green','green'])

# %%
ratings

# %% [markdown]
# Countries name that has given 0 rating

# %%
final_df[final_df['Rating color']=='White'].groupby('Country').size().reset_index()

# %%
final_df.groupby(['Aggregate rating','Country']).size().reset_index().head(5)

# %% [markdown]
# Observations 
# Maximum number of 0 ratings are from Indian customers

# %%
##find out which currency is used by which country?
final_df.columns

# %%
final_df[['Country','Currency']].groupby(['Country','Currency']).size().reset_index()

# %% [markdown]
# Countries do have online deliveries option

# %%
final_df[final_df['Has Online delivery'] =="Yes"].Country.value_counts()

# %%
final_df[['Has Online delivery','Country']].groupby(['Has Online delivery','Country']).size().reset_index()

# %% [markdown]
# Observations: 
# 1. Online Deliveries are available in India and UAE    

# %%
final_df.columns

# %% [markdown]
# Top 5 cities distribution

# %%
final_df.City.value_counts().index

# %%
city_values=final_df.City.value_counts().values
city_labels=final_df.City.value_counts().index

# %%
plt.pie(city_values[:5],labels=city_labels[:5],autopct='%1.2f%%')

# %% [markdown]
# The Top 10 cuisines

# %%
final_df['Cuisines'].value_counts().reset_index().head(10)


