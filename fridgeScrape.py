from lxml import html
import requests

cl_url = f"https://columbus.craigslist.org/search/zip?query=fridge"
page = requests.get(cl_url)
with requests.session() as s:
    sites = s.get('https://www.craigslist.org/about/sites')
    tree = html.fromstring(sites.content)
    hrefs = tree.xpath('//a[contains(@href, "craig")]/@href')

    fridge_tag = '//p[@class="result-info"]/a/text()'
    for site in hrefs:
        cl_url = f"{site}search/zip?query=fridge"
        print(cl_url)
        print("###########")
        page = s.get(cl_url)
        tree = html.fromstring(page.content)
        results = tree.xpath(fridge_tag)
        for r in results:
            print(r)
            print("----------")


