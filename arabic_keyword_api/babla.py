#!/usr/bin/env python3

from urllib.request import urlopen,Request
from bs4            import BeautifulSoup

import sys


def scrape(word):

    response = Request(f"https://en.bab.la/dictionary/arabic-english/{word}", headers={'User-Agent': 'Mozilla/5.0'})

    #webpage  = response
    soup     = BeautifulSoup(urlopen(response).read().decode('utf-8'), "lxml")

    translations = []

    try:
        content_container = soup.findAll("div", attrs={"class": "quick-results container"})[0]
        for ul in content_container.findAll("ul", attrs={"class": "sense-group-results"}):
            for a in ul.findAll("a"):
                if a.text == '\nvolume_up\n':
                    continue
                else:
                    translations.append(a.text)
                    
    except IndexError:
        print("Index Error ,,,")

    if not translations:
        sys.exit(1)

    # for t in translations:
    #     print(t)

    return {word:",".join(translations)}

