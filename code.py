import requests
from bs4 import BeautifulSoup
import os


#This program only works on one website which is hided due to copyright
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
all_url = 'xxxxxxxxxxxxxxxxxxxxxxx' #hided
maid_html = requests.get(all_url,  headers=headers)
Soup=BeautifulSoup(maid_html.text,'lxml')
all_a=Soup.find('div',class_='w1200 oh').find_all('a')
num=0
count=1
l=input("下载数")
for a in all_a:
    href=a['href']
    if len(a['href'])>20:
     num=num+1
     if count > int(l) :
        break
     else: count+=1
     html=requests.get(href,headers=headers)
     html_Soup=BeautifulSoup(html.text,'lxml')
     exist=os.path.exists(os.path.join(os.path.abspath('.'), a.text))
     if exist:
         count-=1
         continue
     else:
         os.mkdir(os.path.join(os.path.abspath('.'), a.text))
     os.chdir(os.path.join(os.path.abspath('.'), a.text))
     for page in range(1,100):
        page_url = href[:-5] + '_' + str(page) + '.html'
        print(page_url)
        img_html = requests.get(page_url,headers=headers)
        img_Soup = BeautifulSoup(img_html.text, 'lxml')
        img_url = img_Soup.find('div', class_='articleV4Body').find('img')['src']
        page=img_Soup.find('div',class_='page-tag oh').find_all('a')[1].get_text()
        if str(page)=='查看原图':
             break
        name = page
        img = requests.get(img_url, headers=headers)
        f = open(name + '.jpg', 'ab')
        f.write(img.content)
        f.close()
     print('download complete')
