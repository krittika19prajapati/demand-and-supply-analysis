#!/usr/bin/env python
# coding: utf-8

# In[28]:


import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.templates.default="plotly_white"


# In[20]:


data=pd.read_csv('rides.csv')


# In[21]:


data.head()


# In[22]:


data.info()


# In[5]:


data.isnull().sum()


# In[6]:


data.dropna()


# In[12]:


demand=data["Riders Active Per Hour"]
supply=data["Drivers Active Per Hour"]
figure=px.scatter(data,x="Drivers Active Per Hour",y="Riders Active Per Hour",trendline="ols",title="Demand and Supply analysis")
figure.update_layout(xaxis_title="Drivers active per hour(supply)",yaxis_title="Riders active per hour(Demand)")
figure.show()


# In[24]:


#calculate supply ratio
data['Supply ratio']=data['Rides Completed']/data['Drivers Active Per Hour']
data.head()


# In[41]:


avg_demand = data['Riders Active Per Hour'].mean()
avg_supply = data['Drivers Active Per Hour'].mean()
pct_change_demand = (max(data['Riders Active Per Hour']) - min(data['Riders Active Per Hour'])) / avg_demand * 100
pct_change_supply = (max(data['Drivers Active Per Hour']) - min(data['Drivers Active Per Hour'])) / avg_supply * 100
elasticity = pct_change_demand / pct_change_supply

print("Elasticity of demand with respect to the number of active drivers per hour: {:.2f}".format(elasticity))


# In[26]:


#calculate demand ratio
data["Demand Ration"]=data['Rides Completed']/data['Riders Active Per Hour']
data.head()


# In[30]:


fig=go.Figure()
fig.add_trace(go.Scatter(x=data['Drivers Active Per Hour'],y=data['Supply ratio'],mode='markers'))
fig.update_layout(title='supply ratio vs driver activity',xaxis_title='Driver activity',yaxis_title='supply ratio')
fig.show()


# In[ ]:




