import pickle
import argparse
import numpy as np
import pandas as pd
from pathlib import Path

from search_engine.crawler import crawl
from search_engine.ranker import rank_pages
from search_engine.vectorizer import compute_tfidf


parser = argparse.ArgumentParser(description='Web crawler')
parser.add_argument('-d', '--domain', type=str, nargs='?',
                    const=1, default='uic.edu', help='Domain to crawl')
parser.add_argument('-s', '--seed', type=str, nargs='?',
                    const=1, default='https://cs.uic.edu', help='Seed URL to start crawling from')
parser.add_argument('-n', '--num_pages', type=int, nargs='?',
                    const=1, default=3000, help='Number of pages to crawl')
args = parser.parse_args()


def main():
    Path.mkdir(f'data/{args.domain}', exist_ok=True)
    crawl_data = crawl(domain=args.domain,
                       url=args.seed,
                       num_pages=args.num_pages)
    vectorizer, doc_tfidf = compute_tfidf(crawl_data.content)
    crawl_data['tfidf'] = list(doc_tfidf)
    
    graph = pd.Series(df.outgoing_links.values,index=df.url).to_dict()
    ranks = rank_pages(graph)
    crawl_data['rank'] = df.url.map(ranks)
    crawl_data.to_pickle(f'data/{args.domain}/crawl_data.pkl')
    with open(f'data/{args.domain}/vectorizer.pk', 'wb') as vec:
        pickle.dump(vectorizer, vec)
        

if __name__ == '__main__':
    main()
    
    
    