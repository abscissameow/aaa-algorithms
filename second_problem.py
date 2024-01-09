import pandas as pd
from collections import defaultdict
from graph_functions import dijkstra_search, find_title_by_id


def main():
    pagelinks_df = pd.read_csv('simple_english_wiki_pagelinks.csv')
    pages_df = pd.read_csv('simple_english_wiki_pages.csv')

    graph = defaultdict(dict)
    for _, row in pagelinks_df.iterrows():
        graph[row['pl_from']][row['pl_to']] = len(str(row['pl_title']))

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

    shortest_path = dijkstra_search(graph, start_page, end_page)

    if shortest_path:
        print(f'самый короткий путь: {shortest_path}')

        total_length = sum(
            graph[shortest_path[i]][shortest_path[i+1]]
            for i in range(len(shortest_path)-1)
        )
        print(f'общая длина переходов: {total_length}')

        last_page_id = shortest_path[-2]
        last_title = find_title_by_id(pages_df, last_page_id)
        if last_title:
            print(f'статью с page_id {last_page_id} зовут: {last_title}')
        else:
            print('нет такой статьи :с')

    else:
        print('нет пути :с')


if __name__ == '__main__':
    main()
