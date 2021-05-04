import pickle
import argparse
import pandas as pd

from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import vstack


parser = argparse.ArgumentParser(description='Search web pages')
parser.add_argument('-d', '--domain', type=str, nargs='?',
                    const=1, default='uic.edu', help='Domain to search in')
parser.add_argument('-q', '--query', type=str, help='Query to search a given domain')
parser.add_argument('-n', '--num_results', type=int, nargs='?',
                    const=1, default=10, help='Number of results to show')
args = parser.parse_args()


def retrieve_results(query, domain='uic.edu'):
    crawl_data = pd.read_pickle(f'data/{domain}/crawl_data.pkl')
    vectorizer = pickle.load(open(f'data/{domain}/vectorizer.pk', 'rb'))
    q_vector = vectorizer.transform([query])
    sim_vectors = cosine_similarity(vstack(crawl_data.tfidf), q_vector)

    urls, ranks = crawl_data['url'], crawl_data['rank']

    results = [(urls[i], sim_vectors[i][0], ranks[i]) for i in range(len(crawl_data))]
    print(results)
    results.sort(key=lambda x: x[1], reverse=True)

    return results


def main():
    results = retrieve_results(args.query, args.domain)
    sorted_top_results = results[:args.num_results]
    sorted_top_results.sort(key=lambda x: x[2], reverse=True)
    for url, sim, rank in sorted_top_results:
        print(url)


if __name__ == '__main__':
    main()
