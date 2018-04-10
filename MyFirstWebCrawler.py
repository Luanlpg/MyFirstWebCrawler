from bs4 import BeautifulSoup
import requests

def extract_title(content):
    soup = BeautifulSoup(content, 'lxml')
    tag = soup.find('title', text = True)

    if not tag:
        return None

    return tag.string.strip()

def extract_links(content):
    soup = BeautifulSoup(content, 'lxml')
    links = set()

    for tag in soup.find.all('a', href = True):
        if tag('href').startswith('http'):
            links.add(tag['href'])

    return links

def crawl(start_url):
    seen_urls = set([start_url])
    available_urls = set([start_url])

    while available_urls:
        url = available_urls.pop()

        try:
            content = requests.get(url, timeout=3)
        except Exception:
            continue

        title = extract_title(content)

        if title:
            print(title)
            print(url)
            print()

        for link in extract_links(content):
            if link not in seen_urls:
                seen_urls.add(link)
                available_urls.add(link)


try:
    crawl('https://www.facebook.com/maikon.weberdecarvalho')
except KeyboardInterrupt:
    print()
    print('FIM!')


