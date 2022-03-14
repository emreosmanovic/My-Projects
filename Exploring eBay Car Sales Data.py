#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
autos = pd.read_csv("autos.csv",encoding = "Latin-1")


# In[2]:


autos


# In[3]:


autos.info()


# In[4]:


autos.head()


# In[5]:


autos.columns


# In[6]:


autos.rename({"yearOfRegistration":"registration_year",
"monthOfRegistration":"registration_month",
"notRepairedDamage":"unrepaired_damage",
"dateCreated": "ad_created",
"dateCrawled":"date_crawled",
"offerType":"offer_type",
"vehicleType":"vehicle_type",
              "powerPS":"power_ps",
              "nrOfPictures":"nr_of_pictures",
              "fuelType":"fuel_type",
              "postalCode":"postal_code",
              "lastSeen":"last_seen",
              "abtest":"ab_test"
}, axis = 1, inplace = True)


# In[7]:


autos.columns


# In[8]:


autos.head()


# In[9]:


autos.describe(include = "all")


# In[10]:


autos["vehicle_type"].value_counts().sum() 

From the table above, there are a number of things worth noting:

the 'nr_of_pictures' column can be dropped as none of the rows have any pictures.

There are some rows of data in the 'registration_year' column that can be removed as the table contains a min and max value of 1000 and 9999 which is highly impropable for the vehicle registrations.

The max in 'power_p_s' column is significantly more than the value at 75% which suggest some inaccurate data in this column.

The minimum in the 'registration_month' column is 0 which is not possible, so this also suggests inaccurate rows of data.

The seller and offer_type columns contain values where almost all the values are the same, so they can be safely removed from the DataFrame.

# In[11]:


autos[["price","odometer"]]
#these are not numeric we have to convert to numeric 


# In[12]:


def convert_price(x):
    if pd.isnull(x) == True:
        return None
    else:
        string = x.split(' ')[0]
        string = string.replace('$','')
        string = string.replace(',','')
        return int(string)
    
price = autos['price'].apply(convert_price)
autos['price'] = price
autos['price'].head()


# In[13]:


def convert_odometer(y):
    if pd.isnull(y) == True:
        return None
    else:
        string = y.split(" ")[0]
        string = string.replace(",","")
        string = string.replace("km","")
        return int(string)
odometer = autos["odometer"].apply(convert_odometer)
autos["odometer"] = odometer
autos["odometer"].head()


# In[14]:


autos.rename({"odometer": "odometer_km"}, axis=1, inplace=True)
autos["odometer_km"].head()


# In[15]:


autos["odometer_km"].value_counts()


# In[16]:


print(autos["price"].describe())
autos["price"].value_counts().head()


# In[17]:


autos["price"].value_counts().sort_index(ascending=False).head()


# In[19]:


autos["price"].value_counts().sort_index(ascending=True).head()


# In[22]:


autos = autos[autos["price"].between(1,351000)]
autos["price"].describe()


# In[23]:


autos[['date_crawled','ad_created','last_seen']][0:5]


# In[24]:


(autos["date_crawled"]
        .str[:10]
        .value_counts(normalize=True, dropna=False)
        .sort_values()
        )


# In[25]:


(autos["last_seen"]
        .str[:10]
        .value_counts(normalize=True, dropna=False)
        .sort_index()
        )


# In[27]:


print(autos["ad_created"].str[:10].unique().shape)
(autos["ad_created"]
        .str[:10]
        .value_counts(normalize=True, dropna=False)
        .sort_index()
        )
(autos["ad_created"]
        .str[:10]
        .value_counts(normalize=True, dropna=False)
        .sort_index()
        )


# In[28]:


autos["brand"].value_counts(normalize=True)


# In[29]:


brand_counts = autos["brand"].value_counts(normalize=True)
common_brands = brand_counts[brand_counts > .05].index
print(common_brands)


# In[ ]:




