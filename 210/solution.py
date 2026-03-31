from collections import deque, defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        order_courses = []

        for dest, src in prerequisites:
            graph[src].append(dest)
            in_degree[dest] += 1

        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        count = 0
        while queue:
            course = queue.popleft()
            count += 1
            order_courses.append(course)

            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return order_courses if numCourses == count else []
