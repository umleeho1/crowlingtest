#참고사이트 https://www.youtube.com/watch?v=yQ20jZwDjTE

#뷰티플숲사용
import requests
from bs4 import BeautifulSoup


#유효성검사
res = requests.get(base_url)
res.raise_for_status()

#f12 마우스왼쪽 검사클릭 각요소확인

#각 요소의 클래스네임 확인


#파싱
soup = BeautifulSoup(res.text, lxml)
#print(soup.a) 객체에서 처음발견되는 요소
#print(soup.a.attrs) # a elemant의 속성 정보
#print(soup.a["href"])  # a element 의 href