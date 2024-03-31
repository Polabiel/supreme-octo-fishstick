import random
class matriz:
    def __init__(self, namesCities: list[str]) -> None:
        if(len(namesCities) <= 0):
            raise ValueError("You need to enter a value in the parameter")
        self.namesCities: list[str] = namesCities

        self.distanceMatrix: list[list[int]] = None
    
    # Função que gera uma matriz das distancias de cada cidades de acordo com uma lista com as cidades que existem dentro dela 🤓☝🏻
    def generateRandomMatrix(self) -> list[list[int]]:

        numCities = len(self.namesCities)
        
        distance_matrix = [[0] * numCities for _ in range(numCities)]

        for i in range(numCities):
            for j in range(i + 1, numCities):
                distance = random.randint(1, 100)
                distance_matrix[i][j] = distance
                distance_matrix[j][i] = distance

        self.distanceMatrix = distance_matrix
        return distance_matrix
    
    def toString(self):
        print(f"List City:")
        for i in range(len(self.distanceMatrix)):
            print(self.distanceMatrix[i])

    def generateMatrixAboutLen(self, length: int) -> list[list[int]]:
        distance_matrix = [[0] * length for _ in range(length)]

        for i in range(length):
            for j in range(i + 1, length):
                distance = random.randint(1,100)
                distance_matrix[i][j] = distance
                distance_matrix[j][i] = distance

        self.distanceMatrix = distance_matrix
        return distanceMatrix