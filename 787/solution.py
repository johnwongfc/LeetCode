from collections import defaultdict
from heapq import heappop, heappush
from typing import List

class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        graph = defaultdict(list)  # destination, price, stop

        for u, v, cost in flights:
            graph[u].append((v, cost))

        heap = [(0, src, 0)]  # price, node, stops
        best = {}

        while heap:
            cost, city, stops = heappop(heap)

            if city == dst:
                return cost

            if stops > k:
                continue

            if (city, stops) in best and best[(city, stops)] <= cost:
                continue
            best[(city, stops)] = cost

            for neighbor, price in graph[city]:
                # update min_price with valid neighbors
                new_price = price + cost
                heappush(heap, (new_price, neighbor, stops + 1))

        return -1
