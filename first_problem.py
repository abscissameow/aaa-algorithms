import pandas as pd
from collections import defaultdict
from graph_functions import bfs_search, find_title_by_id


def main():
    pagelinks_df = pd.read_csv('simple_english_wiki_pagelinks.csv')
    pages_df = pd.read_csv('simple_english_wiki_pages.csv')

    graph = defaultdict(set)
    for _, row in pagelinks_df.iterrows():
        graph[row['pl_from']].add(row['pl_to'])

    start_title = 'Analytics'
    end_title = 'Algorithm'

    start_page = (
        pages_df[pages_df['page_title'] == start_title]
        ['page_id'].values[0]
    )
    end_page = (
        pages_df[pages_df['page_title'] == end_title]
        ['page_id'].values[0]
    )

    shortest_path = bfs_search(graph, start_page, end_page)

    if shortest_path:
        print(f'кратчайший путь от "Analytics" к "Algorithm": {shortest_path}')
        last_page_id = shortest_path[-2]
        last_title = find_title_by_id(pages_df, last_page_id)
        if last_title:
            print(f'статью с page_id {last_page_id} зовут: {last_title}')
        else:
            print('нет такой статьи :с')
        print(f'число переходов: {len(shortest_path) - 1}')

    else:
        print('нет пути :с')


if __name__ == '__main__':
    main()
