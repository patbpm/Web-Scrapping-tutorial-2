#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests 
import pandas as pd


# In[2]:


url = "https://www.programmableweb.com/category/all/apis"




# In[10]:


api_lists = {}
api_no = 0

while True:
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data,'html.parser')
    apis = soup.find_all("tr")
    for api in apis:
        api_name = api.find('a').text
        api_url = api.find('a').get('href')
        api_des_tag=api.find('td', {'class':'views-field views-field-search-api-excerpt views-field-field-api-description hidden-xs visible-md visible-sm col-md-8'})
        api_des=api_des_tag.text if api_des_tag else "N/A"
        api_cat_tag=api.find('td', {'class':'views-field views-field-field-article-primary-category'})
        api_cat=api_cat_tag.text if api_cat_tag else "N/A"
        #print('API Name:',api_name, '\nAPI URL:',api_url, '\nAPI Desc:',api_des, '\nAPI Catgory:',api_cat,'\n-----')
        
        api_no+=1
        api_lists[api_no] = [api_name, api_url, api_des, api_cat]
        
    url_tag=soup.find('a', {'title':'Go to next page'})

    if url_tag.get('href'):

        url='https://www.programmableweb.com'+url_tag.get('href')

        print(url)

    else:

        break


# In[11]:


print("Total apis" , api_no)

api_lists_df = pd.DataFrame.from_dict(api_lists, orient = 'index', columns = ['API Name','Api Url','Api Description', 'Api Category'])

api_lists_df.head()


# In[12]:


api_lists_df.to_csv('api_lists.csv')


# In[ ]:




