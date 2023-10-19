from html2image import Html2Image
from bs4 import BeautifulSoup
import requests
import re
from datetime import datetime as dt
import requests
from urllib.parse import urljoin

def main():
    url = "https://ru.wikipedia.org/wiki/%D0%90%D0%BB%D0%BC%D0%B0-%D0%90%D1%82%D0%B0"
    url = '3.html'
    size = (1920, 1080)
    out_dir = "output"
    make_screen(url, size, out_dir)


def make_screen(url, size, out_dir):
    page, css_files = clean_html(url)

    if css_files:
        style = requests.get(css_files[0])
        css_style = BeautifulSoup(style.text,"html.parser")
        hti = Html2Image(browser="chrome",size=size, output_path=out_dir)
        hti.screenshot(html_str=page, css_str=str(css_style), save_as=f'{dt.now()}.png')
    else:
        hti = Html2Image(browser="chrome",size=size, output_path=out_dir)
        hti.screenshot(html_str=page, css_str="body{background:white;}",save_as=f'{dt.now()}.png')

def clean_html(url):
    if url.startswith("http"): 
        page = requests.get(url)
        soup = BeautifulSoup(page.text,"html.parser")
    else:
        soup = BeautifulSoup(open(url),"html.parser")

    css_files = []
    for css in soup.find_all("link"):
        if css.attrs.get("href"):
            # if the link tag has the 'href' attribute
            css_url = urljoin(url, css.attrs.get("href"))
            css_files.append(css_url)

    html_content = str(soup)

    allTd = soup.findAll('td')
    for td in allTd:
        into_td = td.findAll(['p','div', 'h', 'ul', 'li', 'a', 'span', 'label', 'i', 'link', 'q'])
        if into_td:
            for intd in into_td:
                s = intd.string
                s = s.replace(" ", "")
                intd.string = ('\xa0')*int(len(s)*2.5)
        else:
            s = td.string
            s = s.replace(" ", "")
            td.string = ('\xa0')*int(len(s)*2.5)
    
    allTh = soup.findAll('th')
    for th in allTh:
        into_th = th.findAll(['p','div', 'h', 'ul', 'li', 'a', 'span', 'label', 'i', 'link', 'q'])
        if into_th:
            for inth in into_th:
                s = inth.string
                s = s.replace(" ", "")
                inth.string = ('\xa0')*int(len(s)*2.5)
        else:
            s = th.string
            s = s.replace(" ", "")
            th.string = ('\xa0')*int(len(s)*2.5)

    html_content = str(soup)

    return html_content,css_files


if __name__ == "__main__":
    main()