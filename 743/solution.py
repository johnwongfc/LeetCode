from collections import defaultdict
from heapq import heappop, heappush
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        heap = [(0, k)]  # latency, node
        distances = {k: 0}

        while heap:
            dist, node = heappop(heap)

            if dist > distances.get(node, float("inf")):
                continue

            for neighbor, weight in graph[node]:
                new_dist = dist + weight

                if new_dist < distances.get(neighbor, float("inf")):
                    distances[neighbor] = new_dist
                    heappush(heap, (new_dist, neighbor))

        if len(distances) < n:
            return -1
        return max(distances.values())
