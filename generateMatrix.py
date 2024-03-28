import random

def generate_distance_matrix(namesCities: string) -> list[list[int]]:
    numCities = len(namesCities)
    distance_matrix = [[0] * numCities for _ in range(numCities)]

    for i in range(numCities):
        for j in range(i + 1, numCities):
            distance = random.randint(1, 100)
            distance_matrix[i][j] = distance
            distance_matrix[j][i] = distance

    return distance_matrix