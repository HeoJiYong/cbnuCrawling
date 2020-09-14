'''
공지사항 제목과 Url을 가져오는 모듈


자식태그 선택법 (공백 중요)
soup.select('p > span')
soup.select('p  span')
soup.select('p.name > span.price')
soup.select('h1.name > span.store')
soup.select('a[속성명]')
soup.select('a[href = https://www.naver.com]')
soup.find('p').parent.get_text()    //찾은p의 부모 태그의 텍스트 가져오기


부모태그 선택하기
선택한 태그의 속성값 가져오기 (a태그의 href 값)

'''

from bs4 import BeautifulSoup
import requests
import urls
print("url module loading..")

def GetUrl():
    res = requests.get(urls.noticeUrl)
    soup = BeautifulSoup(res.content,'html.parser')
    size = len(soup.find_all('b'))
    tag_list = soup.find_all('b')
    #print(tag_list)
    #for i in range(size):
    #    print(tag_list[i])
    url_result = ""
    for a in range(size):
        url_result = url_result + urls.mainUrl + soup.find_all('b')[a].parent.parent.get('href') + "\n"
    return url_result

def PrintUrl():
    res = requests.get(urls.noticeUrl)
    soup = BeautifulSoup(res.content,'html.parser')
    size = len(soup.find_all('b'))
    tag_list = soup.find_all('b')
#url 출력부분
    for a in range(size):
        print(soup.find_all('b')[a])
        print(soup.find_all('b')[a].parent)
        print(soup.find_all('b')[a].parent.parent)
        print(soup.find_all('b')[a].parent.parent.get('href'))
        url_result = urls.mainUrl + soup.find_all('b')[a].parent.parent.get('href')
        print(url_result)
        print()

if __name__ == "__main__":
    print("url_module main is executed")
    PrintUrl()
    #result = GetUrl()
    #print(result)
