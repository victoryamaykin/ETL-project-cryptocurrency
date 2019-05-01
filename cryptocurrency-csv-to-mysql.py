#!/usr/bin/env python
# coding: utf-8

# In[61]:


import pandas as pd
from sqlalchemy import create_engine


# In[72]:


data_file = "../Resources/consolidated_coin_data.csv"
crypto_df = pd.read_csv(data_file)
crypto_df.head()


# In[79]:


crypto_df = crypto_df.convert_objects(convert_numeric=True)
crypto_df.dtypes


# In[80]:


crypto_df.columns = ["Currency", "Date_open", "Open_price", "High", "Low", "Close_price", "Volume", "Market_Cap"]
crypto_df= crypto_df.dropna()
crypto_df.head()


# In[81]:


rds_connection_string = "mysql+mysqlconnector://root:Datatime18!@localhost:3306/cryptocurrency_db"

engine = create_engine(f'{rds_connection_string}')


# In[82]:


engine.table_names()


# In[83]:


crypto_df.to_sql(name='data', con=engine, if_exists='append', index=False)


# In[84]:


pd.read_sql_query('select * from data', con=engine).head()


# In[ ]:




