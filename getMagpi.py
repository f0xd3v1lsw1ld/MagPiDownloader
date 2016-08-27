# !/usr/bin/python
__author__ = "f0xd3v1lsw1ld@gmail.com"

# first install beautifulsoup
# use: sudo pip install beautifulsoup4 

import requests, bs4, os, sys, time

url = 'https://www.raspberrypi.org/magpi-issues/'


def download(url, file):

    with open(file, 'wb') as magpiFile:
        start = time.clock()
        res = requests.get(url + file, stream=True)
        try:
            res.raise_for_status()
        except Exception as exc:
            print('There was a problem: %s' % (exc))
            return False

        total_length = res.headers.get('content-length')
        download_cnt = 0
        if total_length is None: # no content length header
            magpiFile.write(res.content)
        else:
            for chunk in res.iter_content(1024):
                download_cnt += len(chunk)
                magpiFile.write(chunk)
                done = int(50 * download_cnt / int(total_length))
                sys.stdout.write("\r[%s%s] %s bps" % ('=' * done, ' ' * (50-done), download_cnt//(time.clock() - start)))
                sys.stdout.flush()

    sys.stdout.write("\n")
    return True

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


if __name__ == "__main__":
    main();
