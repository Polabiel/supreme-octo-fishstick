import math
import random
from typing import Optional

from readFile import ReadFile
class Matriz:
    def __init__(self, namesCities: list[str] = None) -> None:
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
    
    def calculateDistance(self, x: int, y: int) -> float:
        """
        Function that calculates the distance between two points

        Parameters:
        x (int): The first point
        y (int): The second point

        Returns:
        float: The distance between the points
        """
        return abs(x - y)
    
    def capturePointsInInstancesFolder(self) -> list[list[int]]:
        """
        Function that captures the points in the instances folder
        
        Returns:
        Optional[list[list[int]]]: A list with the points
        """
        readFile = ReadFile()
        readFile.read_files("tests")
        cities: list[list[int]] = readFile.cities
        return cities
    
    def captureTravelingSalesmanInInstancesFolder(self) -> list[int]:
        """
        Function that captures the traveling salesman in the instances folder
        
        Returns:
        Optional[list[int]]: A list with the traveling salesman
        """
        readFile = ReadFile()
        readFile.read_files("tests")
        salesmen: list[int] = readFile.n_salesmen
        return salesmen
    
    def distanceEuclidean(self, point1: list[int], point2: list[int]) -> int:
        """
        Function that calculates the Euclidean distance between two points
        
        Parameters:
        point1 (list[int]): The first point
        point2 (list[int]): The second point
    
        Returns:
        float: The distance between the points"
        """
        
        return int(math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2))

    
    def generateMatrixAboutWithPoints(self) -> list[int,list[float]]:
        """
        Function that generates a matrix with the Euclidean distances between the cities

        Returns:
        list[int,list[float]]: The matrix with the distances between the cities and number of the traveling salesman
        """
        inputUser: str = input("Enter the number of cities: ")
        readFile = ReadFile()
        if(int(inputUser) < 1 or int(inputUser) > readFile.length_files("tests")):
            raise ValueError(f"Invalid number of cities, the number must be between 1 and {readFile.length_files('instances')}")
        cities: list[int] = self.capturePointsInInstancesFolder()[int(inputUser) - 1]
        n_salesman: int = self.captureTravelingSalesmanInInstancesFolder()[int(inputUser) - 1]
        num_cities: int = len(cities)

        distance_matrix: list[list[int]] = [[0] * num_cities for _ in range(num_cities)]

        for i in range(num_cities):
            for j in range(i + 1, num_cities):
                distance: float = self.distanceEuclidean(cities[i][1:], cities[j][1:])
                distance_matrix[i][j] = distance
                distance_matrix[j][i] = distance
        return [n_salesman,distance_matrix]