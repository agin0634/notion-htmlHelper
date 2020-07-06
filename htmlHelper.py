from bs4 import BeautifulSoup
import os
import shutil
import string

base = os.path.dirname(os.path.abspath(__file__))
'''
t_html = 
<link rel="stylesheet" href="https://agin0634.github.io/web/style.css">
<link rel="stylesheet" type="text/css" href="https://agin0634.github.io/web/google-code-prettify/prettify.css">
<script type="text/javascript" src="https://agin0634.github.io/web/google-code-prettify/prettify.js"></script>

'''
index = ""
# modify html contents
for dirPath, dirNames, fileNames in os.walk(base):
    for name in fileNames:
        if name == "template.html":
            t_path = os.path.join(base, dirPath, name)

    for name in fileNames:
        if name.endswith(".html"):
            path = os.path.join(base, dirPath, name)
            soup = BeautifulSoup(open(path, "r", encoding='utf-8'), "html.parser")
            tmp_soup = BeautifulSoup(open(t_path, "r", encoding="utf-8"), "html.parser")
            
            div = tmp_soup.find('div', class_= "text-center")
            try:
                div.insert_before(soup.body)
            except:
                print("Fail")

            # rename file name and copy new file
            FN, tmp = "", ""
            for s in name:
                if s != " ":
                    tmp += s.lower()
                else:
                    if len(tmp) <= 25:
                        FN += tmp
                    tmp = "-"
            
            dst = os.path.join(base,FN+".html")

            html = tmp_soup.prettify("utf-8")

            with open(dst, "wb") as file:
                file.write(html)
