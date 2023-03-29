import urllib.request
from bs4 import BeautifulSoup

# 크롤링할 웹 페이지의 url
url = 'https://www.google.com/'

# 해당 url에 접속해서 해당 html문서를 저장한다.
# -> Beautifulsoup이 이 코드를 파싱할 수 있는 형태로 바꾸어준다.
soup = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")

# 이 html 문서에서 모든 a태그를 찾아 저장한다.
a_tags = soup.find_all('a')
result_list = []

# a_tags의 내용을 result_list에 넣는다.
for i in a_tags:
    result_list.append(i.get_text())

print(result_list)