from  urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://www.sta1.com/shops?gndr=F&shopType=S'
hdr= {'User-Agent': 'Mozilla/5.0'}
req = Request(url,headers=hdr)
page = urlopen(req)
soup = BeautifulSoup(page, 'html.parser')


name_list = []
for i in soup.find_all('h2'):
    dummy_txt = i.get_text().split()
    name_list.append(' '.join(dummy_txt))
len(name_list)
#>>>60
rank_list = []
for i in soup.find_all('i','rank'):
    dummy_txt = i.get_text().split()
    rank_list.append(' '.join(dummy_txt))
len(rank_list)
#>>>60    
    
p_list = []
for i in soup.find_all('p')[3:]:
    dummy_txt = i.get_text().split()
    p_list.append(' '.join(dummy_txt)) 

p_list.pop()
#'쇼핑몰 검색결과가 없습니다.'   제거

len(p_list)
#>>>180

#마이샵 제거
search = "마이샵"
for i in p_list:
    if search in i: 
        #print('>> remove: ' + i)
        p_list.remove(i)
p_list

len(p_list)
#>>>120
#p_list 나누기
genre_list=p_list[1::2]    #extended slicing   장르빼기
genre_list
len(genre_list)
#>>>60
target_list = p_list[::2]
target_list
len(target_list)
#>>>60


data = {'rank' : rank_list, 'name': name_list, 'target': target_list,'genre':genre_list}

df = pd.DataFrame(data)
