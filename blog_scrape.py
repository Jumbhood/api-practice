from bs4 import BeautifulSoup
import requests

def scrape(url, path=''):
    r = requests.get(url + path)
    html_doc = r.text

    soup = BeautifulSoup(html_doc,'lxml')

    result=[]

    for item in soup.find_all('div', class_='post-item'):
        outer = item.find('div', class_='post-outer')
        header = outer.find('div', class_='post-header')
        title = header.find('a')

        final = {}
        final['title'] = title.text
        if title['href'][0:4] == 'http':
            final['url'] = title['href']
        else:
            final['url'] = url + title['href']
        body = outer.find('div', class_='post-body')
        final['body'] = body.text
        result.append(final)

    return result