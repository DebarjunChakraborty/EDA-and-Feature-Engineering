# %% [markdown]
# Heart Disease Analysis

# %% [markdown]
# Context
# 
# Heart disease remains one of the leading causes of mortality worldwide. Exploring the factors associated with heart disease can provide valuable insights into its prevention, diagnosis, and treatment. In this project, we conduct an exploratory data analysis (EDA) on a dataset containing various attributes related to heart health. Our objective is to uncover patterns, relationships, and potential risk factors associated with heart disease.
# 
# This data set dates from 1988 and consists of four databases: Cleveland, Hungary, Switzerland, and Long Beach V. It contains 76 attributes, including the predicted attribute, but all published experiments refer to using a subset of 14 of them. The "target" field refers to the presence of heart disease in the patient. It is integer valued 0 = no disease and 1 = disease.

# %% [markdown]
# Content
# 
# Attribute Information:
# 
# 1. age
# 2. sex
# 3. chest pain type (4 values)
# 4. resting blood pressure
# 5. serum cholestoral in mg/dl
# 6. fasting blood sugar > 120 mg/dl
# 7. resting electrocardiographic results (values 0,1,2)
# 8. maximum heart rate achieved
# 9. exercise induced angina
# 10. oldpeak = ST depression induced by exercise relative to rest
# 11. the slope of the peak exercise ST segment
# 12. number of major vessels (0-3) colored by flourosopy
# 13. thal: 0 = normal; 1 = fixed defect; 2 = reversable defect
# 
# The names and social security numbers of the patients were recently removed from the database, replaced with 
# dummy values.
# 

# %% [markdown]
# Import The Libraries And Dataset 

# %%
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

# %%
data = pd.read_csv('heart.csv')

# %% [markdown]
# Display Top 5 Rows of The Dataset

# %%
data.head()

# %% [markdown]
# Check The Last 5 Rows of The Dataset

# %%
data.tail()

# %% [markdown]
# Find Shape of Our Datase

# %%
data.shape

# %%
print("Rows: ", data.shape[0])
print("Columns: ", data.shape[1])

# %% [markdown]
# Get Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement

# %%
data.info()

# %% [markdown]
# Check Null Values In The Dataset

# %%
data.isnull().sum()

# %% [markdown]
# Check For Duplicate Data and Drop Them

# %%
dataDupli = data.duplicated().any()
print(dataDupli)

# %%
data = data.drop_duplicates()

# %%
data.shape

# %% [markdown]
# Overall Statistics About The Dataset

# %%
data.describe()

# %% [markdown]
# Draw Correlation Matrix

# %%
data.corr()

# %%
plt.figure(figsize=(18,7))
sns.heatmap(data.corr(),annot=True)

# %% [markdown]
# How Many People Have Heart Disease, And How Many Don't Have Heart Disease In This Dataset?

# %%
data.columns

# %%
# Count the occurrences of each value in the 'target' column
target_counts = data['target'].value_counts()

# Display the count
print("Number of people without heart disease:", target_counts[0])
print("Number of people with heart disease:", target_counts[1])

# %%
sns.countplot(data=data, x='target')

# %% [markdown]
# Find Count of  Male & Female in this Dataset

# %%
data['sex'].value_counts()


# %%
sns.countplot(data=data, x='sex')

# %% [markdown]
# Check Age Distribution In The Dataset

# %%
sns.histplot(data['age'], bins=20, kde=True, color='skyblue')

# %% [markdown]
# Check Chest Pain Type

# %%
sns.countplot(data=data, x='cp')

# %% [markdown]
# The Chest Pain Distribution As Per Target Variable

# %%
sns.countplot(data=data, x='cp', hue='target')

# %% [markdown]
# Fasting Blood Sugar Distribution According To Target Variable

# %%
sns.countplot(data=data, x='fbs', hue='target')
plt.title('Fasting Blood Sugar Distribution by Target Variable')
plt.xlabel('Fasting Blood Sugar (0: Normal, 1: High)')
plt.ylabel('Count')
plt.legend(title='Target', labels=['No Heart Disease', 'Heart Disease'])
plt.show()

# %% [markdown]
#  Resting Blood Pressure Distribution

# %%
sns.histplot(data['trestbps'], bins=20, kde=True, color='skyblue')
plt.title('Resting Blood Pressure Distribution')
plt.xlabel('Resting Blood Pressure (mm Hg)')
plt.ylabel('Frequency')
plt.show()

# %% [markdown]
# Compare Resting Blood Pressure As Per Sex Column

# %%
sns.violinplot(data=data, x='sex', y='trestbps', palette='muted')
plt.title('Resting Blood Pressure Distribution by Sex')
plt.xlabel('Sex (0: Female, 1: Male)')
plt.ylabel('Resting Blood Pressure (mm Hg)')
plt.show()

# %% [markdown]
# Distribution of Serum cholesterol

# %%
sns.histplot(data['chol'], kde=True, color='skyblue')
plt.title('Distribution of Serum Cholesterol Levels')
plt.xlabel('Serum Cholesterol (mg/dL)')
plt.ylabel('Frequency')
plt.show()

# %% [markdown]
# Plot Continuous Variables

# %%
sns.histplot(data['chol'], kde=True, color='skyblue')
plt.title('Distribution of Serum Cholesterol Levels')
plt.xlabel('Serum Cholesterol (mg/dL)')
plt.ylabel('Frequency')
plt.show()

sns.boxplot(data=data, y='trestbps', color='skyblue')
plt.title('Distribution of Resting Blood Pressure')
plt.ylabel('Resting Blood Pressure (mm Hg)')
plt.show()

sns.scatterplot(data=data, x='trestbps', y='chol', color='skyblue')
plt.title('Scatter Plot of Resting Blood Pressure vs. Serum Cholesterol')
plt.xlabel('Resting Blood Pressure (mm Hg)')
plt.ylabel('Serum Cholesterol (mg/dL)')
plt.show()

sns.lineplot(data=data, x='age', y='thalach', color='skyblue')
plt.title('Line Plot of Age vs. Maximum Heart Rate Achieved')
plt.xlabel('Age')
plt.ylabel('Maximum Heart Rate Achieved')
plt.show()


