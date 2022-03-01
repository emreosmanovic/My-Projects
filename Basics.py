#!/usr/bin/env python
# coding: utf-8

# # Profitable App Profiles for App Store and Google Play Markets

# This project aims to show which app's in stores is profitable.

# In[1]:


from csv import reader

# for apps in Apple Store 
open_file = open("AppleStore.csv")
read_file = reader(open_file)
list_file = list(read_file)

apple_header = list_file[0]
apple = list_file[1:]

#for apps in Google Play
open_file = open("googleplaystore.csv")
read_file = reader(open_file)
list_file = list(read_file)

google_header = list_file[0]
google = list_file[1:]

print(google_header)
print(apple_header)


# In[2]:


def explore_data(dataset, start, end, rows_and_column = False):
    dataset_slice = dataset[start:end]
    for row in dataset_slice:
        print(row)
        print('\n')
    if rows_and_column:
        print("Number of rows:", len(dataset))
        print("Number of columns:", len(dataset[0]))


# In[3]:


print("Google Section")
print(google_header)
explore_data(google, 0, 3, True)
print('\n')
print("Apple's Section")
print(apple_header)
explore_data(apple,0,3,True)


# In[4]:


# This must be deleted because of the error.
del google[10472]


# In[5]:


google_unique = {}

for row in google:
    name = row[0]
    n_reviews = float(row[3])
    
    if name in google_unique and google_unique[name] < n_reviews:
        google_unique[name] = n_reviews
    elif name not in google_unique:
        google_unique[name] = n_reviews


# In[6]:


print("Total apps in Android List:",len(google))
print("Actual total apps in Android:",len(google_unique))


# In[7]:


# burayı anlaman önemli tekrardan incelemen gerekir
# az önce bir sözlük içeresinden kaç tane uygulama olup olmadığını bakmıştık
# halbüki, listenin içeresinden uygulamaları çıkarmadık :) 
android_clean = []
already_added  = []

for row in google:
    name = row[0]
    n_reviews = float(row[3])
    
    if (google_unique[name] == n_reviews) and (name not in already_added):
        android_clean.append(row)
        already_added.append(name)
    


# In[8]:


explore_data(android_clean, 0, 3, True)


# In[9]:


#it is just for testing
def string(x):
    for row in x:
        if ord(row) > 127:
            return False
        else:
            return True


# In[10]:


print(string("Instagram"))
print(string("爱奇艺PPS -《欢乐颂2》电视剧热播"))
print(string('Instachat 😜'))


# In[11]:


def is_english(string):
    non_ascii = 0
    for i in string:
        if ord(i) > 127:
            non_ascii += 1
    if non_ascii > 3:
        return False
    else:
        return True
print(is_english('Docs To Go™ Free Office Suite'))
print(is_english('Instachat 😜'))
        


# In[12]:


android_english = []
apple_english = []

for row in android_clean:
    name = row[0]
    if is_english(name) == True:
        android_english.append(row)
for row in apple:
    name = row[1]
    if is_english(name) == True:
        apple_english.append(row)

        


# In[13]:


print(len(android_english))
print(len(apple_english))


# In[14]:


android_final = []
ios_final = []

for row in android_english:
    price = row[7]
    if price == "0":
        android_final.append(row)
for row in apple_english:
    price = row[4]
    if price == "0.0":
        ios_final.append(row)
                


# In[15]:


print("Total Number of Apps in Android:",len(android_final))
print("Total Number of Apps in IOS:",len(ios_final))


# # NOTE
# Buraya tekrardan bakmam gerekir.
# 
# To minimize risks and overhead, our validation strategy for an app idea is comprised of three steps:
# 
#     1) Build a minimal Android version of the app, and add it to Google Play.
#     2) If the app has a good response from users, we then develop it further.
#     3) If the app is profitable after six months, we also build an iOS version of the app and add it to the App Store

# In[26]:


def freq_table(dataset,index):
    table = {}
    total = 0
    
    for row in dataset:
        total += 1
        value = row[index]
        if value in table:
            table[value] += 1
        else:
            table[value] = 1
            
    table_percentage = {}
    for key in table:
        percentage = (table[key] / total) * 100
        table_percentage[key] = percentage
        
    return table_percentage

freq_table(ios_final,1)
    

