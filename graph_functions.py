from collections import deque


def bfs_search(graph, start, end):
    """
    поиск в ширину в графе
    """
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        current, path = queue.popleft()
        if current == end:
            return path
        if current not in visited:
            visited.add(current)
            for neighbor in graph[current]:
                queue.append((neighbor, path + [neighbor]))

    return None


def find_title_by_id(pages_df, page_id):
    """
    поиска заголовка страницы по её id
    """
    row = pages_df[pages_df['page_id'] == page_id]
    if not row.empty:
        return row['page_title'].values[0]
    else:
        return None


def dijkstra_search(graph, start, end):
    """
    будем искать с помощью дейкстры
    """
    queue = [(0, start, [])]
    visited = set()

    while queue:
        cost, current, path = min(queue)
        queue.remove((cost, current, path))

        if current == end:
            return path + [current]

        if current not in visited:
            visited.add(current)
            for neighbor, weight in graph[current].items():
                queue.append((cost + weight, neighbor, path + [current]))

    return None
