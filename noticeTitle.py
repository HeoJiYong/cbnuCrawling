'''
공지사항 제목 가져오는 파일
'''

import requests
from bs4 import BeautifulSoup
import urls

print("Crawling Module Loading...")
def GetNotice():
    res = requests.get(urls.noticeUrl)
    soup = BeautifulSoup(res.content,'html.parser')
    size = len(soup.find_all('b'))  #Find_all 한후의 string 의 size
    print(type(size))
    sel = soup.select('b')
    print(type(sel))
    ## print(sel)
    ## print(len(sel))
    result_msg=""
    for a in range(size):
        result_msg = result_msg+soup.find_all('b')[a].text +"\n"
        #print(soup.find_all('b')[a].text)
    return result_msg

def PrintNotice():
    res = requests.get(urls.noticeUrl)
    soup = BeautifulSoup(res.content,'html.parser')
    size = len(soup.find_all('b'))  #태그 크기
    print(type(size))
    sel = soup.select('b')
    print(type(sel))
    ## print(sel)
    ## print(len(sel))
    for a in range(size):
        print(soup.find_all('b')[a].text)

if __name__=="__main__":
    print("Crawling Module main is executed..")
    PrintNotice()
    #PrintNotice()
    msg = GetNotice()
'''
url = ['http://www.hair2000.co.kr/product.html?category=1-16',
       'http://www.hair2000.co.kr/product.html?category=1-322',
       'http://www.hair2000.co.kr/product.html?category=1-17',
       'http://www.hair2000.co.kr/product.html?category=1-18',
       'http://www.hair2000.co.kr/product.html?category=8-202']

for i in range(1,5):

    res = requests.get(url[i])

    soup = BeautifulSoup(res.content,'html.parser')
    size = len(soup.find_all('span'))  #태그 크기
    print(type(size))
    sel = soup.select('a')
## print(sel)
## print(len(sel))
    for a in range(size):
        print(soup.find_all('span')[a].text)

    print(size)
    titles = soup.find('title').text
    print(titles)
'''


'''
url1 = 'http://www.hair2000.co.kr/product.html?category=1-16'
url2 = 'http://www.hair2000.co.kr/product.html?category=1-322'
url3 = 'http://www.hair2000.co.kr/product.html?category=1-17'
url4 = 'http://www.hair2000.co.kr/product.html?category=1-18'
url5 = 'http://www.hair2000.co.kr/product.html?category=8-202'
'''
