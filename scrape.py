#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import re
import requests

def scrape(url, county=None, community=None):
    """Scrape to soup, optionally limited to county and/or community"""
    payload = {"fylke": county, "kommune": community, "sok": "Søk etter fastlege"}
    response = requests.post(url, data=payload)

    # TODO: actually check if False in functions using scrape()
    if response.ok:
        return BeautifulSoup(response.text, "html.parser")
    else:
        return False

def filter_tags(soup, tag, pat):
    """Return dict of tag value/text from soup"""
    tags = soup.findAll(tag, attrs={'value': re.compile(pat)})
    return {tag.attrs['value']: tag.text for tag in tags}
