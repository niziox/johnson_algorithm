#!/usr/bin/python
# -*- coding: utf-8 -*-
from Bellman_Ford import bellman_ford
from dijkstra_whole import dijkstra_whole

from typing import List, Dict, Optional
import numpy as np


def johnson(G: Dict[int, List[int]], a: List[List[int]]) -> Optional[Dict[int, Dict[int, int]]]:
    # dodaję nowy węzeł i łączę go ze wszystkimi wirzchołkami krawędzią o wadze 0
    for row in a:
        row.append(np.inf)
    a.append([0 for _ in range(len(a) + 1)])

    new_vertex = list(G)[-1] + 1
    G[new_vertex] = list(G.keys())

    # bellman_ford z wierzchołkiem startowym ustawionym na nowo dodany węzeł
    try:
        bellman_ford_distnaces = bellman_ford(G, a, new_vertex)[0]
    except ValueError as msg:
        print(msg)
        return None

    # usunięcie wcześniej dodanego wierzchołka
    del G[new_vertex]
    del a[-1]
    for row in a:
        row.pop()

    # usunięcie wag ujemnych
    for u in G.keys():
        for v in G[u]:
            if a[u - 1][v - 1] != 0 or a[u - 1][v - 1] != np.inf:
                a[u - 1][v - 1] += bellman_ford_distnaces[u] - bellman_ford_distnaces[v]

    # dijkstra ze wszystkimi wierzołkami startowymi
    dijkstra_distances = {}
    for u in G.keys():
        dijkstra_distances[u] = dijkstra_whole(G, a, start=u)

    # przywrócenie ujemnych wag
    for u in G.keys():
        for v in G.keys():
            dijkstra_distances[u][v] += bellman_ford_distnaces[v] - bellman_ford_distnaces[u]

    return dijkstra_distances


if __name__ == '__main__':

    # print('Graf nieskierowany')
    # d1 = {1: [2, 4, 10], 2: [1, 3, 4, 9, 10], 3: [2, 4, 5, 9], 4: [1, 2, 3, 5], 5: [3, 4, 6, 7, 9], 6: [5, 7, 8],
    #      7: [5, 6, 8, 9], 8: [6, 7, 9, 10], 9: [2, 3, 5, 7, 8, 10], 10: [1, 2, 8, 9]}
    #
    # m1 = [[0, 4, np.inf, 6, np.inf, np.inf, np.inf, np.inf, np.inf, 9],
    #      [4, 0, 1, 5, np.inf, np.inf, np.inf, np.inf, 9, 11],
    #      [np.inf, 1, 0, 2, 9, np.inf, np.inf, np.inf, 8, np.inf],
    #      [6, 5, 2, 0, 10, np.inf, np.inf, np.inf, np.inf, np.inf],
    #      [np.inf, np.inf, 9, 10, 0, 6, 5, np.inf, 7, np.inf],
    #      [np.inf, np.inf, np.inf, np.inf, 6, 0, 1, 5, np.inf, np.inf],
    #      [np.inf, np.inf, np.inf, np.inf, 5, 1, 0, 3, 8, np.inf],
    #      [np.inf, np.inf, np.inf, np.inf, np.inf, 5, 3, 0, 9, 15],
    #      [np.inf, 9, 8, np.inf, 7, np.inf, 8, 9, 0, 8],
    #      [9, 11, np.inf, np.inf, np.inf, np.inf, np.inf, 15, 8, 0]]
    #
    # print(johnson(d1, m1))

    # print('\nGraf skierowany:')
    # d2 = {1: [2], 2: [3, 4], 3: [1], 4: [3, 5, 6], 5: [2, 7, 10], 6: [3, 10],
    #       7: [8, 9], 8: [10], 9: [6, 8], 10: [7, 9]}
    #
    # m2 = [[0, 4, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf],
    #      [np.inf, 0, -11, 9, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf],
    #      [8, np.inf, 0, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf],
    #      [np.inf, np.inf, 7, 0, 2, 6, np.inf, np.inf, np.inf, np.inf],
    #      [np.inf, 8, np.inf, np.inf, 0, np.inf, -7, np.inf, np.inf, 4],
    #      [np.inf, np.inf, -1, np.inf, np.inf, 0, np.inf, np.inf, np.inf, 5],
    #      [np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 0, 9, 13, np.inf],
    #      [np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 0, np.inf, 6],
    #      [np.inf, np.inf, np.inf, np.inf, np.inf, 2, np.inf, 10, 0, np.inf],
    #      [np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 3, np.inf, 1, 0]]
    #
    # print(johnson(d2, m2))

    print('\nGraf skierowany z cyklami ujemnymi:')
    d3 = {1: [2], 2: [3, 4], 3: [1], 4: [3, 5, 6], 5: [2, 7, 10], 6: [3, 10],
          7: [8, 9], 8: [10], 9: [6, 8], 10: [7, 9]}

    m3 = [[0, 4, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf],
         [np.inf, 0, 11, -9, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf],
         [8, np.inf, 0, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf],
         [np.inf, np.inf, 7, 0, 2, -6, np.inf, np.inf, np.inf, np.inf],
         [np.inf, 8, np.inf, np.inf, 0, np.inf, 7, np.inf, np.inf, 4],
         [np.inf, np.inf, -1, np.inf, np.inf, 0, np.inf, np.inf, np.inf, -5],
         [np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 0, 9, 13, np.inf],
         [np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 0, np.inf, 6],
         [np.inf, np.inf, np.inf, np.inf, np.inf, 2, np.inf, 10, 0, np.inf],
         [np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, -3, np.inf, 1, 0]]

    print(johnson(d3, m3))