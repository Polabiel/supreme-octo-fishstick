from ast import Match
import os
import re

class ReadFile:
    def __init__(self) -> None:
        """
        Constructor of the ReadFile class
        
        It will initialize the lists that will store the cities and the number of salesmen.
        
        Return:
        It will only create an object according to this class.
        """
        self.cities: list[list[int]] = []
        self.n_salesmen: list[int] = []
        
    def length_files(self, folder_path: str) -> int:
        """
        This function will return the number of files in the folder.
        
        Parameter:
        folder_path: str -> a string that represents the path to the folder where the files are located.
        
        Return:
        It will return the number of files in the folder.
        """
        files: list[str] = os.listdir(folder_path)
        return len(files)

    def read_files(self, folder_path: str) -> list[int,int,list[int]]:
        """
        This function will read the files in the folder and extract the number of cities, the number of salesmen, and the cities to be visited.
        
        Parameter:
        folder_path: str -> a string that represents the path to the folder where the files are located.
        
        Return:
        It will return a list with the number of cities, the number of salesmen, and the cities to be visited.
        """
        files: list[str] = os.listdir(folder_path)
        data: list = []
        for file in files:
            # Extract number of cities and salesmen from the file name
            match: Match[str] | None = re.search(r'n(\d+)-m(\d+)', file)
            if match:
                num_cities = int(match.group(1))
                num_salesmen = int(match.group(2))

                # Read the file content
                with open(f"{folder_path}/{file}", "r") as f:
                    cities: list = []
                    for line in f:
                        index, x, y = map(int, line.split())
                        cities.append([index, x, y])
                    
                    # Organize the cities according to their indices
                    cities = sorted(cities, key=lambda city: city[0])
                    
                    data.append([num_salesmen, cities])

        for i in range(len(data)):
            self.n_salesmen.append(data[i][0])
            self.cities.append(data[i][1])

        return data