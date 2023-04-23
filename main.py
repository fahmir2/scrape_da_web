import requests
from bs4 import BeautifulSoup
import pprint


res = requests.get('https://news.ycombinator.com/')
bs = BeautifulSoup

soup = bs(res.text, 'html.parser')

links = soup.select('.titleline>a')
subtext = soup.select('.subtext')

def sort_stories_by_vote(hnlist):
    #return sorted(hnlist, key=lambda k: k['Votes'])
    curated_news = sorted(hnlist, key=lambda k: k['votes'], reverse=True)
    pprint.pprint(curated_news)

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')

        if len(vote):
            points = int(vote[0].getText().replace(' points', ' '))
            if points >= 100:
                hn.append({'Title': title, 'Link': href, 'votes': points})
    return sort_stories_by_vote(hn)

#print(create_custom_hn(links, votes))
create_custom_hn(links, subtext)