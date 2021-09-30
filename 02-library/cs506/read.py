import pandas as pd

def read_csv(csv_file_path):
    data = pd.read(csv_file_path)
    matrix = []
    for x in range(len(data)):
        for y in range(len(data[0])):
            matrix[x][y] = data[x][y]
    return matrix
