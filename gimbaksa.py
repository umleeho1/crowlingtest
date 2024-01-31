import requests
from bs4 import BeautifulSoup


#김박사넷 오픈랩페이지
base_url = "https://phdkim.net/professor/open-lab"
#유효성검사
res = requests.get(base_url)
res.raise_for_status()

#각연구소페이지 받을객체
professor_urls = []


# 페이지 번호에 따라 URL을 업데이트하고 크롤링
for page in range(1, 30):  # 페이지범위설정 페이지당 20개의 공고
    url = f"{base_url}?page={page}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    # 현재 페이지의 'item' 클래스를 가진 모든 요소 찾기
    items = soup.find_all(class_="item")

    # 각 아이템에서 'href' 추출 및 필터링
    for item in items:
        a_tag = item.find('a')
        if a_tag and 'href' in a_tag.attrs:
            href = a_tag['href']
            if href.startswith("/professor/") and href.endswith("/info/"):
                professor_urls.append(href)

print(f"Total URLs collected: {len(professor_urls)}")

# 필터링된 URL에 대해 추가 크롤링
counter = 0
for professor_url in professor_urls:
    counter += 1
    full_url = "https://phdkim.net" + professor_url
    response = requests.get(full_url)
    professor_soup = BeautifulSoup(response.text, "lxml")

    # 'open-lab-content-area' 클래스를 가진 요소 찾기 및 내용 출력
    content_area = professor_soup.find(class_="open-lab-content-area")
    if content_area:
        print(f"Crawling {counter}/{len(professor_urls)}: {full_url}")
        print(content_area.get_text(strip=True))
    else:
        print(f"Crawling {counter}/{len(professor_urls)}: Content not found in {full_url}")
