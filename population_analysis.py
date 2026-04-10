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


def calculate_population_change(data):

    changes = {}
    grouped = {}
    
    for row in data:
        country = row['country']
        if country not in grouped:
            grouped[country] = []
        grouped[country].append((row['year'], row['population']))

    for country, records in grouped.items():
        records.sort(key=lambda x: x[0])
        country_changes = {}
        for i in range(1, len(records)):
            prev_year, prev_pop = records[i-1]
            curr_year, curr_pop = records[i]
            change = curr_pop - prev_pop
            country_changes[curr_year] = change
        changes[country] = country_changes

    return changes