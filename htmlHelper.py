from bs4 import BeautifulSoup
import os

base = os.path.dirname(os.path.abspath(__file__))
t_html = '''<link rel="stylesheet" href="https://agin0634.github.io/web/style.css">'''

for dirPath, dirNames, fileNames in os.walk(base):
    for name in fileNames:
        if name.endswith(".html"):
            path = os.path.join(base, dirPath, name)
            soup = BeautifulSoup(open(path, "r", encoding='utf-8'), "html.parser")
            t_soup = BeautifulSoup(t_html, "html.parser")
            for x in soup.find_all('style'):
                x.extract()
                head = soup.find('head')
                try:
                    head.append(t_soup)
                except expression as identifier:
                    pass
            
            html = soup.contents
            html = soup.prettify("utf-8")
            with open(path, "wb") as file:
                file.write(html)