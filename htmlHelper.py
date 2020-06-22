from bs4 import BeautifulSoup
import os
import shutil

base = os.path.dirname(os.path.abspath(__file__))
t_html = '''
<link rel="stylesheet" href="https://agin0634.github.io/web/style.css">
<link rel="stylesheet" type="text/css" href="https://agin0634.github.io/web/google-code-prettify/prettify.css">
<script type="text/javascript" src="https://agin0634.github.io/web/google-code-prettify/prettify.js"></script>
'''
index = ""
# modify html contents
for dirPath, dirNames, fileNames in os.walk(base):
    for name in fileNames:
        if name.endswith(".html"):
            path = os.path.join(base, dirPath, name)
            if not index and name != "index.html":
                index = path
            soup = BeautifulSoup(open(path, "r", encoding='utf-8'), "html.parser")
            t_soup = BeautifulSoup(t_html, "html.parser")
            for x in soup.find_all('style'):
                x.extract()

                head = soup.find('head')
                head.append(t_soup)

                body = soup.find('body')
                body['onload'] = "PR.prettyPrint()"

                for y in soup.find_all('pre'):
                    y['class']='prettyprint'

            html = soup.contents
            html = soup.prettify("utf-8")
            with open(path, "wb") as file:
                file.write(html)

# create index.html
src = index
dst = os.path.join(base,"homepage.html")
shutil.copy(src, dst)