import random
from typing import Optional
class Matriz:
    def __init__(self, namesCities: list[str]) -> None:
        if(len(namesCities) < 2):
            raise ValueError("You need to enter a value in the parameter")
        self.namesCities: list[str] = namesCities    
    
    # Função que gera uma matriz das distancias de cada cidades de acordo com uma lista com as cidades que existem dentro dela 🤓☝🏻
    def generateRandomMatrix(self) -> list[list[int]]:
        numCities: int = len(self.namesCities)
        distance_matrix: list[list[int]] = [[0] * numCities for _ in range(numCities)]

        for i in range(numCities):
            for j in range(i + 1, numCities):
                distance: int = random.randint(1, 100)
                distance_matrix[i][j] = distance
                distance_matrix[j][i] = distance

        self.distance_matrix = distance_matrix
        return distance_matrix
    
    def toString(self) -> list[str]:
        print_str: list[str] = []
        for i in range(len(self.distance_matrix)):
            print_str.append(' '.join(map(str, self.distance_matrix[i])))
            
        return print_str

    def generateMatrixAboutLen(self, length: int) -> list[list[int]]:
        distance_matrix: list[list[int]] = [[0] * length for _ in range(length)]

        for i in range(length):
            for j in range(i + 1, length):
                distance: int = random.randint(1,100)
                distance_matrix[i][j] = distance
                distance_matrix[j][i] = distance

        self.distance_matrix: list[list[int]] = distance_matrix
        return distance_matrix