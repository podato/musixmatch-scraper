# **Musixmatch scraper**
A script that scrapes lyrics of the popular music lyrics site [Musixmatch](https://www.musixmatch.com/), written entirely in python.

![GitHub](https://img.shields.io/github/license/podato/musixmatch-scraper?style=for-the-badge)
![GitHub Repo stars](https://img.shields.io/github/stars/podato/musixmatch-scraper?style=for-the-badge)

## Features:
* Shell arguments
* Clean-ish code :)

## Usage:
Before using the script you must install the requirements:

```
pip3 install -r requirements.txt
```
Upon installing the requirements you can just run the script normally
```
python3 main.py
```
alternatively you could input custom arguments via shell
```
python3 main.py [musixmatch url] [output filename]
```

## TODO
* Download all songs from artists
* improved error handling
* automatic language changing for lyrics
* proxy support

## Disclaimer
This is likely abuse of musixmatch's API and i am not liable for any problems this tool may cause for musixmatch.

Because as they all say;
> It's for educational purposes only
