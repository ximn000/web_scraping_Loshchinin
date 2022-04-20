import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
import pandas as pd

URL_TEMPLATE = "https://www.rabota.ru/vacancy"
r = requests.get(URL_TEMPLATE)

soup = bs(r.text, "html.parser")
vacancies_names = soup.find_all('h3', class_='vacancy-preview-card__title')
vacancies_info = soup.find_all(class_='vacancy-preview-card__short-description')
salary = soup.find_all('div', class_='vacancy-preview-card__salary')

result_list = {'name': [], 'Link': [], 'salary': [], 'info': []}
for name in vacancies_names:
    result_list['name'].append(str(name)[148:-22])
for lnk in salary:
    result_list['Link'].append('https://www.rabota.ru/' + lnk.a['href'])
    result_list['salary'].append(str(lnk)[122:-10])
for info in vacancies_info:
    result_list['info'].append(str(info)[76:])

df = pd.DataFrame(result_list)
df.to_csv("C:\\Дело\\Learning\\geek brains\\WebScraping\\rabota.csv", sep=",", encoding='utf-8')


