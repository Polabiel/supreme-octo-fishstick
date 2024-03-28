def nearest_neighbor(tour: list, ) -> list:
    unvisited = list(range(1, n_cities))
    tour = [0]
    
    while unvisited:

        next_city = min(unvisited, key = lambda unvisited_city : distances[tour[-1]][unvisited_city])
        
        tour.append(next_city)
        unvisited.remove(next_city)
        
    return tour

def multiplesTravelingSalesman(TravelsSalesmans: list[list], cities: list[list[int]]) -> int:
    if(len(TravelsSalesmans) < 2):
        raise Exception("you do not have more than 2 traveling salesmen to perform this function")    

def benchmark(tour: list, numberCities: int) -> int:
    total_distance = 0

    for i in range(numberCities - 1):
        total_distance = total_distance + distances[tour[i]][tour[i + 1]]

    total_distance = total_distance + distances[tour[-1]][tour[0]]

    return total_distance

if __name__ == "__main__":
    print(multiplesTravelingSalesman([]))