#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import List, Dict
import numpy as np


def dijkstra_whole(G: Dict[int, List[int]], a: List[List[int]], start: int = 1) -> Dict[int, int]:
    d = {}
    p = {}

    for u in G.keys():
        d[u] = np.inf
        p[u] = 0

    Q = list(G.keys())
    Q.remove(start)
    d[start] = 0
    u_prior = start

    while Q:
        # zmiana cechowania
        for u in [node for node in Q if node in G[u_prior]]:
            if d[u_prior] + a[u_prior - 1][u - 1] < d[u]:
                d[u] = d[u_prior] + a[u_prior - 1][u - 1]
                p[u] = u_prior

        # szukanie wierzchołka o najmniejszym koszcie
        mini = min([v for i, v in d.items() if i in Q])
        for i, v in d.items():
            if v == mini and i in Q:
                u_prior = i
                break

        # usunięci wierzchołka o najmniejszym koszcie
        Q.remove(u_prior)

    return d


if __name__ == '__main__':
    pass
