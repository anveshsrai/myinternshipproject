#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pandas


# In[11]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

url='https://www.worldometers.info/world-population/population-by-country/'
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')

rows =soup.find('table',{'id':'example2'}).find('tbody').find_all('tr')

countries_list =[]
for row in rows:
    dic={}
    
    dic['Country'] = row.find_all('td')[1].text
    dic['Population 2020'] = row.find_all('td')[2].text.replace(',','')
    
    countries_list.append(dic)
df = pd.DataFrame(countries_list)
df.to_csv('countries_data.csv',index=False)


# In[ ]:




