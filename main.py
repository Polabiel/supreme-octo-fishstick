from generateMatrix import matriz

def nearest_neighbor(distances: list[list[int]], tour: list[int] = None, unvisited: list[list[int]] = None) -> list:
    # Inicializa tour e unvisited na primeira chamada
    if tour is None:
        tour = [0]
    if unvisited is None:
        unvisited = list(range(1, len(distances)))

    # Verifica se ainda há cidades não visitadas
    if not unvisited:
        return tour

    # Tenta encontrar a próxima cidade
    try:
        next_city = min(unvisited, key=lambda unvisited_city: distances[tour[-1]][unvisited_city])
    except ValueError as e:
        print(f"Erro ao encontrar a próxima cidade: {e}")
        return tour

    # Adiciona a próxima cidade ao tour e a remove das não visitadas
    tour.append(next_city)
    unvisited.remove(next_city)

    # Chama a função de maneira recursiva e BONITA!!!!
    return nearest_neighbor(distances, tour, unvisited)

def multiplesTravelingSalesman(TravelsSalesmans: list[list], cities: list[list[int]]) -> int:
    # Ainda não achei um jeito bonitão de fazer isso
    if(len(TravelsSalesmans) < 2):
        raise ValueError("you do not have more than 2 traveling salesmen to perform this function")    

def benchmark(tour: list, numberCities: int, distances: list[list[int]]) -> int:
    # Função para verificar se essa é realmente a melhor distance
    total_distance = 0

    for i in range(numberCities - 1):
        total_distance = total_distance + distances[tour[i]][tour[i + 1]]

    total_distance = total_distance + distances[tour[-1]][tour[0]]

    return total_distance

if __name__ == "__main__":
    m  = matriz(["São Paulo","Campinas","Sorocaba","Santos","Ribeirão Preto","Bauru","São José dos Campos","São José do Rio Preto","Piracicaba","Presidente Prudente","Araraquara","Maranhão"])
    distances = m.generateRandomMatrix()
    m.toString()
    print("\nResult:\n")
    print(nearest_neighbor(distances))
