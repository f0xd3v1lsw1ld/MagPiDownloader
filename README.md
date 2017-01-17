# MagPiDownloader
simple script to sync local folder with the MagPi server to get all MagPi editions

The script sync all MagPi editions (and other pdf documents) from ['https://www.raspberrypi.org/magpi-issues/'](https://www.raspberrypi.org/magpi-issues/) with a local directory.

Example output:
```sh
# download new file
./getMagpi.py
> Found new file: Essentials_Bash_v1.pdf
> [==================================================] 2.35MB:2.35MB  
# there is no new file
./getMagpi.py
> No new files found
```


## Installation

 1. install beautifulsoup
    ```sh
    $ sudo pip install beautifulsoup4
    ```
 2. create folder to store the MagPi editions
    ```sh
    $ mkdir --parents ~/Dokumente/books/MagPi
    ```
 3. go in the new directory and clone the repository
   ```sh
   $ cd ~/Dokumente/books/MagPi
   $ git clone https://github.com/f0xd3v1lsw
   ```

## Usage

go in the MagPi directory and run the script
   ```sh
   $ cd ~/Dokumente/books/MagPi
   $ ./getMagpi.py
   ```
by default other languages then english are blacklisted
you can enable these with cli argument, avaible languages are ["French", "Hebrew", "Italian", "Spanish"]
   ```sh
   $ ./getMagpi.py French
   ```

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## Credits

based on:
 - http://automatetheboringstuff.com/chapter11/
 - https://stackoverflow.com/questions/20801034/how-to-measure-download-speed-and-progress-using-requests

## License

MIT License

Copyright (c) 2016 f0xd3v1lsw1ld

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
