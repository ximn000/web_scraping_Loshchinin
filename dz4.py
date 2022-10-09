from pymongo import MongoClient
import pymongo
import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
import pandas as pd


def parsim():
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
    return result_list

df = pd.DataFrame(parsim())
vacancies = pd.read_csv(r"C:\\Дело\\Learning\\geek brains\\WebScraping\\rabota", sep=",", encoding='utf-8')
df2 = vacancies.append(df, ignore_index=True)

client = MongoClient('mongodb://localhost:27017/')
db = client.testdb
collection = db["Rabot"]

df2.reset_index(inplace=True)
data_dict = df2.to_dict("records")
db.data_dict.insert_many(data_dict)
db.data_dict.aggregate([{'$project': {'_id': 0,}},{'$group': {'_id': '$$ROOT'}},{'$replaceRoot': {'newRoot': '$_id'}}])

c = db.data_dict.find()
for c in c:
    pprint('{0}_<**>_{1}_<**>_{2}'.format(c['name'], c['salary'], c['info']))


