# Web Crawler
> Crawls a domain and stores crawl data for quick query searches


## Install (Optional)

The package can be installed using pip as below

`pip install -e .`

## Dependencies

This project requires the following libraries
- numpy
- pandas
- sklearn
- nltk
- beautiful_soup
- beautifulsoup4
- urllib

> If you installed the package, there is no need to separately install the packages

## Usage

### Crawling Webpages

Before we can start searching, the domain we wish to query has to be crawled and stored. To do that, `crawl.py` is executed.

To know how to use `crawl.py`, execute `crawl.py -h`

```bash
usage: crawl.py [-h] [-d [DOMAIN]] [-s [SEED]] [-n [NUM_PAGES]]

Web crawler

optional arguments:
  -h, --help            show this help message and exit
  -d [DOMAIN], --domain [DOMAIN]
                        Domain to crawl
  -s [SEED], --seed [SEED]
                        Seed URL to start crawling from
  -n [NUM_PAGES], --num_pages [NUM_PAGES]
                        Number of pages to crawl
```

Here's an example...

```bash
crawl.py -d uic.edu -s https://cs.uic.edu -n 3000
```
This will crawl `3000` webpages from the domain `uic.edu` starting from `https://cs.uic.edu`

### Searching crawled domains

Now that we have some webpages crawled and stored for a domain (say, `uic.edu`), we can query that domain to return search results using `search.py`

To know how to use `search.py`, execute `search.py -h`

```bash
usage: search.py [-h] [-d [DOMAIN]] [-q QUERY] [-n [NUM_RESULTS]]

Search web pages

optional arguments:
  -h, --help            show this help message and exit
  -d [DOMAIN], --domain [DOMAIN]
                        Domain to search in
  -q QUERY, --query QUERY
                        Query to search a given domain
  -n [NUM_RESULTS], --num_results [NUM_RESULTS]
                        Number of results to show
```

Here's an example...

```bash
search.py -d uic.edu -q library -n 10
```
This will return `10` relevant results to query term `q` from the domain `uic.edu`

```bash
https://library.uic.edu/using-the-library
https://library.uic.edu/help/search?t%5B0%5D=18
https://library.uic.edu/help/search?t%5B0%5D=21
https://library.uic.edu/help/search?l%5B0%5D=391
https://library.uic.edu/help/search?t[]=18&t[]=20&t[]=21&t[]=26&t[]=29&;
https://library.uic.edu/help/search?t[]=17&t[]=24&t[]=208&l[]=390&l[]=388&l[]=389&l[]=391&l[]=386
https://library.uic.edu/help/search?t[]=19&t[]=48&t[]=21&l[]=386
https://library.uic.edu/help/search?t[]=18&t[]=23&l[]=386
https://library.uic.edu/help/search?q=&t%5B%5D=18
https://library.uic.edu/help/search?q=&t%5B%5D=21
```

## More Details

For more details about this package, please visit https://vignesh-nswamy.github.io/search_engine/
