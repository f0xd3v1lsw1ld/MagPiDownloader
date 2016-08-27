# !/usr/bin/python
__author__ = "f0xd3v1lsw1ld@gmail.com"

# first install beautifulsoup
# use: sudo pip install beautifulsoup4 

import requests, bs4, os

url = 'https://www.raspberrypi.org/magpi-issues/'


def download(url, file):
    res = requests.get(url + file)
    try:
        res.raise_for_status()
    except Exception as exc:
        print('There was a problem: %s' % (exc))
        return False

    magpiFile = open(file, 'wb')
    for chunk in res.iter_content(100000):
        magpiFile.write(chunk)
    magpiFile.close()


def main():
    res = requests.get(url)

    try:
        res.raise_for_status()
    except Exception as exc:
        print('There was a problem: %s' % (exc))
        exit()

    magpiSoup = bs4.BeautifulSoup(res.text,"lxml")

    for a in magpiSoup.find_all('a', href=True):
        if a['href'][-3:] == 'pdf':
            if not os.path.isfile(a['href']):
                print("Found new file: %s" % a['href'])
                download(url, a['href'])
                exit()


if __name__ == "__main__":
    main();
