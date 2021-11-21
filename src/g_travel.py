from collections import deque
from typing import List
from typing import Tuple


def get_dist(city_1: Tuple[int, int], city_2: Tuple[int, int]):
    return abs(city_1[0] - city_2[0]) + abs(city_1[1] - city_2[1])


def travel():
    n = int(input())
    coords = []

    for _ in range(n):
        x, y = map(int, input().split())
        coords.append((x, y))

    capacity = int(input())
    departure, arrival = map(int, input().split())
    departure, arrival = departure - 1, arrival - 1  # python index start with 0 not at 1

    result = bfs(coords=coords, departure=departure, arrival=arrival, capacity=capacity)
    print(result)


def bfs(coords: List[Tuple[int, int]], departure: int, arrival: int, capacity: int) -> int:
    queue = deque([])
    visited = set()

    queue.append((departure, 0))  # index_of_city, road_counter
    visited.add(departure)

    while queue:
        current_city, road_counter = queue.popleft()
        if current_city == arrival:
            return road_counter

        for city in range(len(coords)):
            if get_dist(coords[city], coords[current_city]) <= capacity and city not in visited:
                queue.append((city, road_counter + 1))
                visited.add(city)

    return -1


if __name__ == '__main__':
    travel()
