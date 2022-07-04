import requests
from bs4 import BeautifulSoup
from webtoon import extract_info
import csv

file = open('webtoon.csv', mode='w', newline='')  # newline은 띄어쓰기 없이 입력한다는 뜻
writer = csv.writer(file)
writer.writerow(["title", "author", "rating"])

final_result = []

# 우리가 정보를 얻고 싶어하는 URL
WEBTOON_URL = f"https://comic.naver.com/webtoon/weekdayList?week=fri"

# get 요청을 통해 해당 페이지 정보를 저장
webtoon_html = requests.get(WEBTOON_URL)

# bs4 라이브러리를 통해 불러온 html을 우리가 원하는 형태로 파싱
webtoon_soup = BeautifulSoup(webtoon_html.text, "html.parser")

webtoon_list_box = webtoon_soup.find("ul", {"class": "img_list"})
webtoon_list = webtoon_list_box.find_all("li")

final_result += extract_info(webtoon_list)

for result in final_result:
    row = []
    row.append(result['title'])
    row.append(result['author'])
    row.append(result['rating'])
    writer.writerow(row)


print(final_result)
