import requests
from bs4 import BeautifulSoup

# 세 자리 숫자 범위 설정 (예: 801에서 801까지)
start, end = 801, 801

for i in range(start, end + 1):
    # 페이지 주소 구조에 맞춰 URL 생성
    url = f"https://www.all-con.co.kr/view/contest/510{i}?page=1&sortname=cl_order&sortorder=asc&t=1&ct=&sc=&tg="
    
    # 해당 URL로부터 HTML 페이지를 가져옴
    response = requests.get(url)
    
    # 요청이 성공했는지 확인
    if response.status_code == 200:
        # BeautifulSoup 객체 생성
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 'board_body' 클래스가 있는 요소들을 모두 찾음
        board_body = soup.find_all(class_='board_body')
        
        # 각 요소에 대하여 내용을 추출
        for index, content in enumerate(board_body, start=1):
            # 텍스트 추출 및 출력
            print(f'Page 510{i} - Content {index}:', content.get_text(strip=True))
    else:
        print(f'Failed to retrieve page 510{i}')
