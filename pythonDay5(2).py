#!/usr/bin/env python
# coding: utf-8

# In[1]:


import webbrowser
url = 'www.naver.com'
webbrowser.open(url)


# In[2]:


import requests


# In[5]:


r = requests.get('https://www.google.co.kr')
print(r)


# In[6]:


print(r.text)


# In[ ]:


#conda install bs4
#conda install lxml 설치


# In[8]:


from bs4 import BeautifulSoup


# In[9]:


html = """<html><body><div><span>
       <a href=http://www.naver.com>naver</a>
       <a href=https://www.google.com>google</a>
       <a href=http://www.daum.net/>daum</a>
       </span></div></body></html>"""


# In[10]:


soup = BeautifulSoup(html,'lxml')
print(soup)


# In[11]:


print(soup.prettify())


# In[12]:


print(soup.find('a'))


# In[13]:


print(soup.find('a').get_text())


# In[14]:


site_names = soup.find_all('a')
print


# In[15]:


for site_name in site_names:
    print(site_name.get_text)


# In[16]:


html2 = """
<html>
 <head>
 <title>작품과 작가 모음</title>
 </head>
 <body>
 <h1>책 정보</h1>
 <p id="book_title">토지</p>
 <p id="author">박경리</p>
 <p id="book_title">태백산맥</p>
 <p id="author">조정래</p>
 <p id="book_title">감옥으로부터의 사색</p>
 <p id="author">신영복</p>
 </body>
</html>
"""


# In[17]:


soup2 = BeautifulSoup(html2,'lxml')


# In[18]:


print(soup2.title)


# In[19]:


print(soup2.body)


# In[20]:


print(soup2.body.h1)


# In[21]:


print(soup2.find('p',{'id':'book_title'}))


# In[22]:


print(soup2.find('p',{'id':'author'}))


# In[24]:


book_titles = soup2.find_all('p',{'id':'book_title'})
authors = soup2.find_all('p',{'id':'author'})
for book_title,author in zip(book_titles,authors):
    print(book_title.get_text()+'/'+author.get_text())


# In[25]:


print(soup2.select('body h1'))


# In[26]:


print(soup2.select('body p'))


# In[27]:


print(soup2.select('p#book_title'))


# In[28]:


f = open('C://Users//BIT//anaconda3//data/example.html',encoding='utf-8')
html3 = f.read()
print(f)


# In[29]:


print(html3)


# In[30]:


soup3 = BeautifulSoup(html3,'lxml')
print(soup3.select('a.portal'))


# In[32]:


import requests
url = 'https://www.alexa.com/topsites/countries/KR'
html_website_ranking = requests.get(url).text
soup_website_ranking = BeautifulSoup(html_website_ranking,'lxml')


# In[33]:


website_ranking = soup_website_ranking.select('p a')
print(website_ranking[:6])


# In[34]:


website_ranking = website_ranking[1:]


# In[35]:


print(len(website_ranking))


# In[40]:


website_ranking_sites = [website_ranking_element.get_text() for website_ranking_element in website_ranking]  


# In[43]:


print(website_ranking_sites[:5])


# In[44]:


print('[Top SItes in South Korea]')
for k in range(len(website_ranking)):
    print("{0}:{1}".format(k+1,website_ranking_sites[k]))


# In[45]:


import pandas as pd
ranking_dict = {'Website': website_ranking_sites}
df = pd.DataFrame(ranking_dict, index=range(1, len(website_ranking)+1))


# In[46]:


print(df)


# In[48]:


#이미지 다운받기
#이미지 주소 가져오기
url ='https://www.python.org/static/img/python-logo.png'
html_image = requests.get(url)
print(html_image)


# In[55]:


import os
file_name = os.path.basename(url) #이미지 주소중 맨뒤를 가져옴,이미지 내용을 가져올수있다
print(file_name)


# In[56]:


url ='https://www.python.org/static/img/python-logo.png'
html_image = requests.get(url)
file_name = os.path.basename(url)
folder = 'download'

if not os.path.exists(folder):
    os.makedirs(folder)

iamge_path = os.path.join(folder, file_name)

imageFile = open(image_path,'wb') #있는 정보 그대로 저장해라
chunk_size = 1000000
for chunk in html_image.iter_content(chunk_size):
    imageFile.write(chunk)
    
imageFile.close()


# In[57]:


print(iamge_path)


# In[59]:


url ='https://picjumbo.com/free-stock-photos/animals/'
html_picjumbo = requests.get(url).text
soup_picjumbo = BeautifulSoup(html_picjumbo,'lxml')
image_elements =soup_picjumbo.select('picture img')
print(image_elements[:5])


# In[73]:


image_url = image_elements[0].get('data-src')
print(image_url)


# In[74]:


def get_image_url(url):
    html_image = requests.get(url).text
    soup_image = BeautifulSoup(html_picjumbo,'lxml')
    image_elements = soup_image.select('picture img')
    if image_elements != None:
        image_urls = []
        for image_element in image_elements:
            image_urls.append(image_element.get('data-src'))
        return image_urls
    else:
        return None
    


# In[89]:


def download_image(img_folder, img_url):
    if img_url != None: 
        html_imge = requests.get(img_url)
        image_file = open(os.path.join(img_folder,os.path.basename(img_url)),'wb')
        chunk_size = 1000000
        for chunk in html_image.iter_content(chunk_size):
            image_file.write(chunk)
        image_file.close()
        #print('이미지파일:{0}받기 완료'.format(os.path.basename(img_url)))
        
    else:
        print("이미지가 없습니다.")


# In[90]:


url ='https://picjumbo.com/free-stock-photos/animals/'
figure_folder = 'download'
picjumbo_image_urls = get_image_url(url)
for k in range(3):
    download_image(figure_folder, picjumbo_image_urls[k])
    
print('='*50)
print('이미지받기 완료')


# In[91]:


from tqdm.notebook import tqdm

url ='https://picjumbo.com/free-stock-photos/animals/'
figure_folder = 'download'
picjumbo_image_urls = get_image_url(url)
for k in tqdm(range(len(picjumbo_image_urls))):
    download_image(figure_folder, picjumbo_image_urls[k])
    
print('='*50)
print('이미지받기 완료')


# In[ ]:




