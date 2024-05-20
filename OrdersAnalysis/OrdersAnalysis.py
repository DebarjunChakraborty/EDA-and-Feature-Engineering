# %%
import pandas as pd
df = pd.read_csv('orders.csv',na_values=['Not Available','unknown'])

# %%
df.head(20)

# %%
df['Ship Mode'].unique()

# %%
df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(' ','_')
df.head(5)

# %%
df['discount']=df['list_price']*df['discount_percent']*.01
df['sale_price']= df['list_price']-df['discount']
df['profit']=df['sale_price']-df['cost_price']
df

# %%
df['order_date']=pd.to_datetime(df['order_date'],format="%Y-%m-%d")

# %%
df.drop(columns=['list_price','cost_price','discount_percent'],inplace=True)

# %%
from sqlalchemy import create_engine
username = 'root'
host = 'localhost'
port = 3306
database = 'master'
database_url = f'mysql+mysqlconnector://{username}:@{host}:{port}/{database}'
engine = create_engine(database_url)
conn = engine.connect()
if conn:
    print("Connected to MySQL database using SQLAlchemy")



# %%
df.to_sql('df_orders', con=conn , index=False, if_exists = 'append')

# %%



