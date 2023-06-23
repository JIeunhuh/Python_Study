import requests
from bs4 import BeautifulSoup
import pandas as pd
## 카카오 웹툰 크롤링해서 장르에 따른 조회수,좋아요로 인기분석?해서 시각화
## url
url = 'https://webtoon.kakao.com/'
response = requests.get(url)
print(response.text)

# 제목, 작가, 장르, 조회수, 좋아요 가져옴
#soup = BeautifulSoup(response.text,'html.parser')
