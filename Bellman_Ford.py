#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import List, Dict, Tuple
import numpy as np


def bellman_ford(G: Dict[int, List[int]], a: List[List[int]], start: int = 1) -> Tuple[Dict[int, int], Dict[int, int]]:
    d = {}
    p = {}

    for u in G.keys():
        d[u] = np.inf
        p[u] = -1

    d[start] = 0

    # przejście po każdym wierzchołku i jego krawędziech incydentnych i uaktualnienie cechowania
    for _ in range(len(G.keys()) - 1):
        for u in G.keys():
            for v in G[u]:
                if d[v] > d[u] + a[u - 1][v - 1]:
                    d[v] = d[u] + a[u - 1][v - 1]
                    p[v] = u

    # sprawdzenie na wypadek cyklów ujemnych
    for u in G.keys():
        for v in G[u]:
            if d[v] > d[u] + a[u - 1][v - 1]:
                raise ValueError('Graf zawiera ujemne cykle')

    return d, p


if __name__ == '__main__':
    pass
