import requests
from bs4 import BeautifulSoup
import pandas as pd

reviews = []


def trade_spider():
    url = "https://www.cetpainfotech.com/reviews"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, features="html.parser")
    for re in soup.find_all('div', {'class': "rvDes"}):
        reviews.append(re.text)
        print(re.text)


trade_spider()
print(reviews)
print(len(reviews))
dataset = pd.DataFrame({'Reviews': reviews})
dataset.to_csv('Cetpa review.csv', index=False)
# , encoding='utf-8'