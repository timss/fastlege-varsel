#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
from scrape import scrape, filter_tags

def get_counties(url):
    """Returns a dict {id: name}"""
    soup = scrape(url)
    pat = '^\d{2}$'
    return filter_tags(soup, 'option', pat)

def get_communities(url, counties):
    """Returns a dict {id: name}"""
    communities = {}

    # could also be done with incomprehensible dict comprehension
    for county in counties:
        soup = scrape(url, county)
        pat = "{}\d+".format(county)
        options = filter_tags(soup, 'option', pat)
        communities.update(options)

    return communities

def save(url):
    """Save county/community id/name for later use"""
    counties = get_counties(url)
    communities = get_communities(url, counties)

    # create directory if not exists, no warning thrown
    os.makedirs("data", exist_ok=True)

    with open('data/counties.json', 'w+') as f:
        f.write(json.dumps(counties, indent=4, sort_keys=True, ensure_ascii=False))

    with open('data/communities.json', 'w+') as f:
        f.write(json.dumps(communities, indent=4, sort_keys=True, ensure_ascii=False))

def load(category):
    """Load county/community id/name from saved file"""
    with open('data/{}.json'.format(category), 'r+') as f:
        return json.loads(f.read())

def main():
    url = "https://tjenester.nav.no/minfastlege/innbygger/fastlegesokikkepalogget.do"
    save(url)

if __name__ == '__main__':
    main()
