import random
import time
from matriz import Matriz
from colorama import Fore, Style

class TravelingSalesman:
    
    def __init__(self, cities: list[list[int]] = None, numberTravelingSalesmans: int = None) -> None:
        """
        Constructor of the TravelingSalesman class

        It performs parameter checks to prevent errors within the class.

        Parameter:
        cities: list[list[int]] -> a list of lists of integers that represent the coordinates of the cities to be visited.
        numberTravelingSalesmans: int -> an integer that represents the number of traveling salesmen that will visit the cities.

        Return:
        It will only create an object according to this class.
        """
        
        if cities is None and numberTravelingSalesmans is None:
            mt = Matriz()
            newValues: list[int,list[float]] = mt.generateMatrixAboutWithPoints()

            self.number_traveling_salesmans = newValues[0]
            self.cities = newValues[1]
            return
        
        self.cities: list[list[int]] = cities
        self.number_traveling_salesmans: int = numberTravelingSalesmans

    def divide_cities(self) -> list[list[int]]:
        """
        This function will divide the cities according to the number of traveling salesmen.
        
        Return:
        It will return the number of cities that each salesman will visit.
        """
        
        return len(self.cities) // self.number_traveling_salesmans
    
    
    
    def multiples_traveling_salesman(self) -> list[list[int]]:
        """
        This function will divide the cities according to the number of traveling salesmen.
        
        Return:
        It will return the result of the division of cities according to the number of traveling salesmen and the result of the heuristics.
        """
        
        cities: list[list[int]] = self.cities.copy()
        number_traveling_salesmans: int = self.number_traveling_salesmans
        cities_divided: list[list[int]] = []
        
        for i in range(number_traveling_salesmans):
            cities_divided.append(cities[i * self.divide_cities(): (i + 1) * self.divide_cities()])
        
        return cities_divided 
        
    def heuristic_nearest_neighbor(self, cities: list[list[int]] = None,tour: list[int] = None, unvisited: list[list[int]] = None) -> list:
        """
        This function will find the nearest neighbor of a city and add it to the tour.
        
        Parameters:
        tour: list[int] -> a list of integers that represents the cities that the traveling salesman will visit.
        unvisited: list[list[int]] -> a list of lists of integers that represents the cities that the traveling salesman will visit.
        
        Return:
        It will return the tour of the traveling salesman.
        """
        
        # Inicializa tour e unvisited na primeira chamada
        if tour is None:
            tour = [0]
        if unvisited is None:
            unvisited = list(range(1, len(cities)))

        # Verifica se ainda há cidades não visitadas
        if not unvisited:
            tour.append(0)
            return tour

        # Tenta encontrar a próxima cidade
        try:
            next_city: list[int] = unvisited[0]
            min_distance: list[int] = cities[tour[-1]][next_city]

            for unvisited_city in unvisited[1:]:
                distance: list[int] = cities[tour[-1]][unvisited_city]
                if distance < min_distance:
                    next_city = unvisited_city
                    min_distance = distance
        except ValueError as e:
            print(f"Error finding next city: {e}")
            return tour

        # Adiciona a próxima cidade ao tour e a remove das não visitadas
        tour.append(next_city)
        unvisited.remove(next_city)

        # Chama a função de maneira recursiva e BONITA!!!!
        return self.heuristic_nearest_neighbor(cities, tour, unvisited)

    def heuristic_longest_neighbor(self, cities: list[list[int]] = None,tour: list[int] = None, unvisited: list[list[int]] = None) -> list:
        """
        This function will find the longest neighbor of a city and add it to the tour.
        
        Parameters:
        tour: list[int] -> a list of integers that represents the cities that the traveling salesman will visit.
        unvisited: list[list[int]] -> a list of lists of integers that represents the cities that the traveling salesman will visit.
        
        Return:
        It will return the tour of the traveling salesman.
        """
        
        # Inicializa tour e unvisited na primeira chamada
        if tour is None:
            tour = [0]
        if unvisited is None:
            unvisited = list(range(1, len(cities)))

        # Verifica se ainda há cidades não visitadas
        if not unvisited:
            tour.append(0)
            return tour

        # Tenta encontrar a próxima cidade
        try:
            next_city: list[int] = unvisited[0]
            max_distance: list[int] = cities[tour[-1]][next_city]

            for unvisited_city in unvisited[1:]:
                distance: list[int] = cities[tour[-1]][unvisited_city]
                if distance > max_distance:
                    next_city = unvisited_city
                    max_distance = distance
        except ValueError as e:
            print(f"Error finding next city: {e}")
            return tour

        # Adiciona a próxima cidade ao tour e a remove das não visitadas
        tour.append(next_city)
        unvisited.remove(next_city)

        # Chama a função de maneira recursiva e BONITA!!!!
        return self.heuristic_longest_neighbor(cities, tour, unvisited)

    def calculate_total_distance(self, tour: list[int]) -> int:
        """
        This function will calculate the total distance traveled by the traveling salesman.
        
        Parameters:
        tour: list[int] -> a list of integers that represents the cities that the traveling salesman will visit.
        
        Return:
        It will return the total distance traveled by the traveling salesman.
        """
        
        total_distance: int = 0
        cities: list[list[int]] = self.cities
        
        for i in range(len(tour) - 1):
            total_distance += cities[tour[i]][tour[i + 1]]
        
        total_distance += cities[tour[-1]][tour[0]]
        
        return total_distance

    def choose_heuristic(self) -> str:
        """
        This function will choose a heuristic to solve the traveling salesman problem.
        
        Return:
        It will return a string that represents the chosen heuristic.
        """

        heuristics: list[str] = ["heuristic_nearest_neighbor", "heuristic_longest_neighbor"]
        chosen_heuristic: str = random.choice(heuristics)
        return chosen_heuristic

    def execute_heuristic(self) -> list[int, list[int]]:
        """
        This function will serve to execute the chosen heuristic for all multiple salesmen in such a way that each salesman has his own heuristic and returns its result within a list.
        
        return: 
        Returns the sum of the distances traveled by all traveling salesmen and the matrix of cities.
        """
        
        chosen_heuristic: str = self.choose_heuristic()
        results: list[list[int]] = []
        cities_divided: list[list[int]] = self.multiples_traveling_salesman()
        total_distance: int = 0
        benchmark: dict = {}
        
        print(Fore.BLUE + f"Heuristic chosen: {chosen_heuristic}" + Style.RESET_ALL)
        
        for i, cities in enumerate(cities_divided):
            start_time: float = time.time()
            result: None = getattr(self, chosen_heuristic)(cities)
            end_time: float = time.time()
            execution_time: float = end_time - start_time
            results.append(result)
            total_distance += self.calculate_total_distance(result)
            benchmark[f"Salesman {i+1}"] = {"Execution Time": execution_time, "Total Distance": total_distance}
        
        print(Fore.GREEN + "Results:" + Style.RESET_ALL)
        for i, result in enumerate(results):
            print(Fore.GREEN + f"Salesman {i+1} tour: {result}" + Style.RESET_ALL)
        
        print(Fore.YELLOW + "Benchmark:" + Style.RESET_ALL)
        for salesman, data in benchmark.items():
            print(Fore.CYAN + f"{salesman}:" + Style.RESET_ALL)
            for key, value in data.items():
                print(f"  {key}: {value}")
        
        return results if len(results) > 1 else results[:][0]