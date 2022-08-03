from requests import get
from bs4 import BeautifulSoup
from googlesearch import search


with open('icml2022.txt', 'r') as f:
    y = f.readlines()
# print(x[1].p.b.text.lower())
# y = x[1].find_all('li')
for i in y:
    text = i.split('|')[1]
    for j in search(text):
        if 'arxiv' in j:
            print(f'|[{text}]({j})||')
            break
        elif 'pdf' in j:
            print(f'|[{text}]({j})||')
            break
        else:
            continue

# # |[A Simple and Practical Algorithm for Private Multivariate Mean and Covariance Estimation](https://arxiv.org/abs/2006.06618)||