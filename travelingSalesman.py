class TravelingSalesman:
    def __init__(self, cities: list[list[int]], numberTravelingSalesmans: int) -> None:
        if(len(cities) <= 0 or cities is None):
            raise ValueError("you need to include your cities within the parameter")
        
        if numberTravelingSalesmans < 2:
            raise ValueError("You need to implement a value for the number of traveling salesmen")
        
        self.cities: list[list[int]] = cities
        self.numberTravelingSalesmans: int = numberTravelingSalesmans

    def divide_cities(self) -> int:
        # Dividir as cidades e arrendodar para cima caso necessario, nao sei se isso funcionará ou vai dar erro
        divCities: int = round(len(self.cities) / self.numberTravelingSalesmans)

        if divCities is None:
            return -1

        return divCities
    
    def multiples_traveling_salesman(self) -> list[list[list[int]]]:
        self.divide_cities()
        return [[]]
    
    def nearest_neighbor(self, tour: list[int] = None, unvisited: list[list[int]] = None) -> list:
        # Inicializa tour e unvisited na primeira chamada
        if tour is None:
            tour = [0]
        if unvisited is None:
            unvisited = list(range(1, len(self.cities)))

        # Verifica se ainda há cidades não visitadas
        if not unvisited:
            return tour

        # Tenta encontrar a próxima cidade
        try:
            next_city: list[int] = unvisited[0]
            min_distance: list[int] = self.cities[tour[-1]][next_city]

            for unvisited_city in unvisited[1:]:
                distance: list[int] = self.cities[tour[-1]][unvisited_city]
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
        return self.nearest_neighbor(tour, unvisited)