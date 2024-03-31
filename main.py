from matriz import Matriz
from travelingSalesman import TravelingSalesman

def benchmark(tour: list, numberCities: int, distances: list[list[int]]) -> int:
    # Função para verificar se essa é realmente a melhor distance
    total_distance: int = 0

    for i in range(numberCities - 1):
        total_distance = total_distance + distances[tour[i]][tour[i + 1]]

    total_distance = total_distance + distances[tour[-1]][tour[0]]

    return total_distance

if __name__ == "__main__":
    m  = Matriz(["São Paulo","Campinas","Sorocaba","Santos","Ribeirão Preto","Bauru","São José dos Campos","São José do Rio Preto","Piracicaba","Presidente Prudente","Araraquara","Maranhão"])
    distances: list[list[int]] = m.generateRandomMatrix()
    m.toString()
    print("\nResult:\n")
    t = TravelingSalesman(distances)
    print(t.nearest_neighbor())
    print(f"Total distance calculation: {benchmark(t.nearest_neighbor(), len(t.cities),t.cities)}")