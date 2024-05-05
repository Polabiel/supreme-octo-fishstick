from travelingSalesman import TravelingSalesman

if __name__ == "__main__":
    print("\nResult:\n")
    t = TravelingSalesman()
    heuristicResult: list[list[int]] = t.execute_heuristic()