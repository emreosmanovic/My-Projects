#!/usr/bin/env python
# coding: utf-8

# # Project: Finding Heavy Traffic Indicators on I-94
# 

# The goal of our analysis is to determine a few indicators of heavy traffic on I-94. These indicators are weather type, time of the day, time of the week, etc.

# In[1]:


import pandas as pd
traffic = pd.read_csv("Metro_Interstate_Traffic_Volume.csv")
traffic.info()
traffic.head()


# In[2]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

plt.hist(traffic["traffic_volume"])
plt.show()
traffic["traffic_volume"].describe()


# In[3]:


traffic["date_time"] = pd.to_datetime(traffic["date_time"])
day = traffic.copy()[(traffic["date_time"].dt.hour < 19) & (traffic["date_time"].dt.hour >= 7)]
night = traffic.copy()[(traffic["date_time"].dt.hour >= 19) | (traffic["date_time"].dt.hour < 7)]
print(day.shape)
print(night.shape)


# In[4]:


plt.figure(figsize=(11,3.5))

plt.subplot(1, 2, 1)
plt.hist(day["traffic_volume"])
plt.title("Traffic Volume Between 7am-7pm")
plt.xlabel("Volume")
plt.ylabel("Frequency")
plt.xlim(-100, 7500)
plt.ylim(0, 8000)

plt.subplot(1, 2, 2)
plt.hist(night["traffic_volume"])
plt.title("Traffic Volume Between 7pm-7am")
plt.xlabel("Volume")
plt.ylabel("Frequency")
plt.xlim(-100, 7500)
plt.ylim(0, 8000)

plt.show()


# In[5]:


day["traffic_volume"].describe()


# In[6]:


night["traffic_volume"].describe()


# In[7]:


day['month'] = day['date_time'].dt.month
by_month = day.groupby('month').mean()
by_month['traffic_volume']
plt.plot(by_month['traffic_volume'])
plt.show()


# In[8]:


day['dayofweek'] = day['date_time'].dt.dayofweek
by_dayofweek = day.groupby('dayofweek').mean()
by_dayofweek['traffic_volume']  # 0 is Monday, 6 is Sunday
plt.plot(by_dayofweek['traffic_volume'])
plt.show()


# In[9]:


day['dayofweek'] = day['date_time'].dt.dayofweek
by_dayofweek = day.groupby('dayofweek').mean()
by_dayofweek['traffic_volume']  # 0 is Monday, 6 is Sunday
plt.plot(by_dayofweek['traffic_volume'])
plt.show()


# In[10]:


day["hour"] = day["date_time"].dt.hour

business_days = day.copy()[day["dayofweek"] <= 4]
weekend = day.copy()[day["dayofweek"] >= 5]

by_hour_business = business_days.groupby("hour").mean()
by_hour_weekend = weekend.groupby("hour").mean()

plt.figure(figsize=(11,3.5))

plt.subplot(1,2,1)
by_hour_business["traffic_volume"].plot.line()
plt.xlim(6,20)
plt.ylim(1500,6500)
plt.title('Traffic Volume By Hour: Monday–Friday')

plt.subplot(1,2,2)
by_hour_weekend["traffic_volume"].plot.line()
plt.xlim(6,20)
plt.ylim(1500,6500)
plt.title('Traffic Volume By Hour: Weekend')
plt.show()


# In[11]:


day.corr()["traffic_volume"]


# In[12]:


day.plot.scatter('traffic_volume', 'temp')
plt.ylim(230, 320) # two wrong 0K temperatures mess up the y-axis
plt.show()


# In[13]:


by_weather_main = day.groupby("weather_main").mean()
by_weather_main["traffic_volume"].plot.barh()
plt.show()


# In[16]:


by_weather_desc = day.groupby("weather_description").mean()
by_weather_desc["traffic_volume"].plot.barh()
plt.show()


# In[ ]:




