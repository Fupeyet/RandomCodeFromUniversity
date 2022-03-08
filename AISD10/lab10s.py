import requests
from bs4 import BeautifulSoup

collections = [
    'community_5 - Vanguard',
    'bravo_ii - Alpha',
    'gods_and_monsters - Gods and Monsters',
    'bravo_i - Bravo'
]

def link_main(c):
    url_main = 'https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=tag_set_' + collections[c].split(' - ')[0] + '&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&appid=730'
    info = requests.get(url_main)
    soup = BeautifulSoup(info.content, 'html.parser')
    for link in soup.find_all('a', class_='market_listing_row_link'):
        print(link.get('href'))

for c in range(0, len(collections)):
    link_main(c)