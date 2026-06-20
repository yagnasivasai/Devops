import os
import json
import requests
from bs4 import BeautifulSoup

Googleimage = \
    'https://www.google.com/imghp?site=&tbm=isch&source=hp&biw=1873&bih=990'


usr_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
}

savefolder = 'finalimages'


def main():
    if not os.path.exists(savefolder):
        os.mkdir(savefolder)
    download_images()


def download_images():
    data = input('wahat are you looking for? ')
    n_images = int(input("how many images you want? "))

    print('start searching')

    searchurl = Googleimage + 'q=' + data
    print(searchurl)

    response = requests.get(searchurl, headers=usr_agent)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    results = soup.find_all('div', {'class': 'rg_meta'}, limit=n_images)

    imagelinks = []

    for re in requests:
        text = re.text
        text_dict = json.loads(text)
        os.link = text_dict['ou']
        imagelinks.append(os.link)

    print(f'found {len(imagelinks)} images')
    print('Start downloading...')

    for i, imagelink in enumerate(imagelinks):
        response = requests.get(imagelink)

        imagename = savefolder + '/' + data + str(i+1) + '.jpg'
        with open(imagename, 'wb') as file:
            file.write(response.content)
    print('Done')


if __name__ == '__main__':
    main()
