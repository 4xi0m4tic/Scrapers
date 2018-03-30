#!/bin/sh

# Cleanup
rm ./*.csv
rm ./*.txt
touch top-crack-pages.txt

# Scrape www.crackapk.com/top-crack/
scrapy crawl top-crack
cat top-crack.csv | cut -f 2 -d "," | grep "http://www.crackapk.com/" > top-crack-pages.txt
scrapy crawl top-crack-pages
# Cleanup
rm top-crack-pages.txt

# scrapy crawl crack-apps
# scrapy crawl crack-games
