# !/usr/bin/python
__author__ = "f0xd3v1lsw1ld@gmail.com"

# first install beautifulsoup
# use: sudo pip install beautifulsoup4
# based on:
# http://automatetheboringstuff.com/chapter11/
# https://stackoverflow.com/questions/20801034/how-to-measure-download-speed-and-progress-using-requests

import requests, bs4, os, sys, time

url = 'https://www.raspberrypi.org/magpi-issues/'


def download(url, file):

    total_length = 0

    with open(file, 'wb') as magpiFile:
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
                if chunk: # filter out keep-alive new chunks
                    try:
                        res.raise_for_status()
                    except Exception as exc:
                        print('There was a problem: %s' % (exc))
                        return False
                    download_cnt += len(chunk)
                    magpiFile.write(chunk)
                    done = int(50 * download_cnt / int(total_length))
                    sys.stdout.write("\r[%s%s] %0.2fMB:%0.2fMB   " %
                                     ('=' * done, ' ' * (50-done), float(download_cnt)/1000000,
                                     float(total_length)/1000000
                                      ))
                    sys.stdout.flush()
    sys.stdout.write("\n")

    if os.path.isfile(file):
        if not int(os.path.getsize(file)) == int(total_length):
            print('There was a unknown problem downloading: %s' % (file))
            print('Please try again')
            os.remove(file)



    return True

def main():
    res = requests.get(url)
    new_files_cnt = 0
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
                new_files_cnt += 1
                download(url, a['href'])

    if new_files_cnt == 0:
        print("No new files found")

if __name__ == "__main__":
    main();
