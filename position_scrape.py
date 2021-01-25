from bs4 import BeautifulSoup
import requests

def scrape(url, path=''):
    r = requests.get(url + path)
    html_doc = r.text

    soup = BeautifulSoup(html_doc,'lxml')

    result=[]

    for item in soup.find_all('div', class_='co01-current-openings__item'):
        office = item.find('div', class_='co01-current-openings__office-name')
        office_name = office.text.strip()
        for department in item.find_all('div', class_='co01-current-openings__department'):
            department_name = department.find('div', class_='co01-current-openings__department-name').text.strip()
            for position in department.find_all('a'):
                final = {}
                final['office'] = office_name
                final['department'] = department_name
                final['position'] = position.text
                if position['href'][0:4] == 'http':
                    final['url'] = position['href']
                else:
                    final['url'] = url + position['href']
                result.append(final)

    return result

