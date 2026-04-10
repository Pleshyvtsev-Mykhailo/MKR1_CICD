import os

def read_population_data(file_path):
    
    data = []
    if not os.path.exists(file_path):
        return data
        
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 3:
                country, year, population = parts
                data.append({
                    'country': country.strip(),
                    'year': int(year.strip()),
                    'population': int(population.strip())
                })
    return data