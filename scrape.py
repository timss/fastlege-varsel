#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import re
import requests

def filter_tags(soup, tag, pat):
    """Return dict of tag value/text from soup"""
    tags = soup.find_all(tag, attrs={'value': re.compile(pat)})
    return {tag.attrs['value']: tag.text for tag in tags}

def parse_table(soup):
    """Return list of dicts matching table from soup"""
    table = soup.find('table', attrs={'class': 'RTVtbl'})
    thead = ['name', 'sex', 'office', 'accessibility', 'address',
            'post', 'grouped', 'shared', 'citizens', 'available']

    # list of dict {'available': 0', 'post': '4324 Sandnes', ...}
    result = []

    for row in table.find('tbody').find_all('tr'):
        cols = [ele.text.strip() for ele in row.find_all('td')]
        prac = dict(zip(thead, cols))
        result.append(prac)

    return result

def scrape(url, county=None, community=None):
    """Scrape to soup, optionally limited to county and/or community"""
    payload = {"fylke": county, "kommune": community, "sok": "Søk etter fastlege"}
    response = requests.post(url, data=payload)

    # TODO: actually check if False in functions using scrape()
    if response.ok:
        return BeautifulSoup(response.text, "html.parser")
    else:
        return False
