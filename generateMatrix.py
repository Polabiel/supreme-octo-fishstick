import random

def generate_distance_matrix(namesCities: string) -> list[list[int]]:
    num_cities = len(namesCities)
    distance_matrix = [[0] * num_cities for _ in range(num_cities)]

    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            distance = random.randint(1, 100)
            distance_matrix[i][j] = distance
            distance_matrix[j][i] = distance

    return distance_matrix