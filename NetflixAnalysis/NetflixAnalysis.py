# %% [markdown]
# Import Libaries and data

# %%
import numpy as np # linear algebra operations
import pandas as pd # used for data preparation
import plotly.express as px #used for data visualization


df = pd.read_csv('netflix_titles.csv')


# %% [markdown]
# Checking number of rows and columns in data

# %%
df.shape

# %% [markdown]
# Checking content available in Dataset

# %%
df.head()

# %% [markdown]
# Check columns name of dataset

# %%
df.columns

# %% [markdown]
# Count of ratings available

# %%
x = df.groupby(['rating']).size().reset_index(name='counts')
print(x)

# %% [markdown]
# Piechart based on Content rating

# %%
pieChart = px.pie(x, values='counts', names='rating', title='Distribution of content ratings on Netflix')
pieChart.show()

# %% [markdown]
# Analyzing the top 5 Directors on Netflix

# %%
df['director']=df['director'].fillna('Director not specified')
df.head()

# %%
directors_list = pd.DataFrame()
print(directors_list)

# %%
directors_list = df['director'].str.split(',', expand=True).stack()
print(directors_list)

# %%
directors_list = directors_list.to_frame()
print(directors_list)

# %%
directors_list.columns = ['Director']
print(directors_list)

# %%
directors = directors_list.groupby(['Director']).size().reset_index(name='Total Count')
print(directors)

# %%
directors = directors[directors.Director != 'Director not specified']

# %%
print(directors)

# %%
directors = directors.sort_values(by=['Total Count'], ascending = False)
print(directors)

# %%
top5Directors = directors.head()
print(top5Directors)

# %%
top5Directors = top5Directors.sort_values(by=['Total Count'])
barChart = px.bar(top5Directors, x='Total Count', y = 'Director', title = 'Top 5 Directors on Netflix')
barChart.show()

# %% [markdown]
# Analyzing the top 5 Actors on Netflix

# %%
df['cast']=df['cast'].fillna('No cast specified')
cast_df = pd.DataFrame()
cast_df = df['cast'].str.split(',',expand=True).stack()
cast_df = cast_df.to_frame()
cast_df.columns = ['Actor']
actors = cast_df.groupby(['Actor']).size().reset_index(name = 'Total Count')
actors = actors[actors.Actor != 'No cast specified']
actors = actors.sort_values(by=['Total Count'], ascending=False)
top5Actors = actors.head()
top5Actors = top5Actors.sort_values(by=['Total Count'])
barChart2 = px.bar(top5Actors, x='Total Count', y='Actor', title='Top 5 Actors on Netflix')
barChart2.show()

# %% [markdown]
# Analyzing the content produced on netflix based on years

# %%
df1 = df[['type', 'release_year']]
df1 = df1.rename(columns = {"release_year":"Release Year", "type": "Type"})
df2 = df1.groupby(['Release Year', 'Type']).size().reset_index(name='Total Count')

# %%
print(df2)

# %%
df2 = df2[df2['Release Year']>=2000]
graph = px.line(df2, x = "Release Year", y="Total Count", color = "Type", title = "Trend of Content Produced on Netfilx Every Year")
graph.show()


