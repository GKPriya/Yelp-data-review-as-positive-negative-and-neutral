
# coding: utf-8

# In[1]:


import pandas as pd
import json
#json to csv


# In[2]:


data = pd.read_json("business.json",lines=True)
df_business= pd.DataFrame(data)


# In[3]:


df_business.to_json(orient= 'index')


# In[4]:


pd.read_json(_, orient='index')


# In[5]:


import pickle
PIK = "pickle.dat"


with open(PIK, "wb") as f:
    pickle.dump(df_business, f)


# In[6]:


f.close()


# In[7]:


pickle_in = open("pickle.dat","rb")
df_business = pickle.load(pickle_in)
pickle_in.close()


# In[8]:


print(df_business)


# In[9]:


import pandas as pd
import json

with open('review.json',encoding='utf8') as json_file:      
    data_r = json_file.readlines()
    
    data_r = list(map(json.loads, data_r)) 

df_review= pd.DataFrame(data_r)


# In[10]:


import pickle
O_rev = "pickle1.dat"


with open(O_rev, "wb") as f:
    pickle.dump(df_review, f)
f.close()


# In[11]:


pickle_in = open("pickle1.dat","rb")
df_review = pickle.load(pickle_in)
pickle_in.close()


# In[12]:


print(df_review)

