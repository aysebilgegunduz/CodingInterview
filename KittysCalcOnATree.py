# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict, deque
from itertools import combinations
import math
def create_graph(indexes, n):
    graph = defaultdict(list)
    for k, v in indexes:
        graph[k].append(v)
        graph[v].append(k)
    return graph
def bfs2(graph, start, goal):
    """
    finds a shortest path in undirected `graph` between `start` and `goal`.
    If no path is found, returns `None`
    """
    if start == goal:
        return [start]
    visited = {start}
    queue = deque([(start, [])])

    while queue:
        current, path = queue.popleft()
        visited.add(current)
        for neighbor in graph[current]:
            if neighbor == goal:
                return path + [current, neighbor]
            if neighbor in visited:
                continue
            queue.append((neighbor, path + [current]))
            visited.add(neighbor)
    return None

def find_distance(graph, start, goal):
    #find the distance with dfs
    if start == goal:
        return 0
    visited = {start}
    queue = deque([(start, [])])

    while queue:
        current, path = queue.popleft()
        visited.add(current)
        for neighbor in graph[current]:
            if neighbor == goal:
                return len(path + [current, neighbor])-1
            if neighbor in visited:
                continue
            queue.append((neighbor, path + [current]))
            visited.add(neighbor)

def calculate(m_list):
    result = 0
    path = 0
    n_list = list(combinations(m_list,2))
    for a, b in n_list:
            path = find_distance(graph, a, b)
            result += (a * b * path)
    return int(result% (math.pow(10,9) +7))


if __name__ == '__main__':

    n, q = map(int, input().split())
    indexes = []

    for _ in range(n-1):
        indexes.append(list(map(int, input().rstrip().split())))
    graph = create_graph(indexes, n)

    for _ in range(q):
        k = int(input())
        if k > 1:
            m_list = list(map(int, input().rstrip().split()))
            print(calculate(m_list))
        else:
            item = int(input())
            print(0)

        #find_distance(graph, )

