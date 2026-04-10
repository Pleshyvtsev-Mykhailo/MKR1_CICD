import pytest
import tempfile
import os
from population_analysis import read_population_data, calculate_population_change

@pytest.fixture
def sample_data_file():
    content = "Ukraine, 2020, 41000000\nUkraine, 2021, 40000000\nJapan, 2020, 125000000\nJapan, 2021, 124000000\n"
    fd, path = tempfile.mkstemp(suffix=".txt")
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    yield path
    os.close(fd)
    os.remove(path)


def test_read_population_data(sample_data_file):
    data = read_population_data(sample_data_file)
    assert len(data) == 4
    assert data[0]['country'] == 'Ukraine'


@pytest.mark.parametrize("test_input, expected_country, expected_year, expected_change", [
    ([
        {'country': 'Ukraine', 'year': 2020, 'population': 41000000},
        {'country': 'Ukraine', 'year': 2021, 'population': 40000000}
    ], 'Ukraine', 2021, -1000000),
    ([
        {'country': 'Japan', 'year': 2020, 'population': 125000000},
        {'country': 'Japan', 'year': 2022, 'population': 123000000}
    ], 'Japan', 2022, -2000000)
])


def test_calculate_population_change(test_input, expected_country, expected_year, expected_change):
    result = calculate_population_change(test_input)
    assert expected_country in result
    assert result[expected_country][expected_year] == expected_change