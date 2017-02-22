from helpers import load_data
from helpers import get_vacancy_params
import json

if __name__ == '__main__':
    data = load_data()
    simple_vacancies = []
    for vacancy in data['objects']:
        parameters = get_vacancy_params(vacancy)
        simple_vacancies.append(parameters)
    path = 'simple_vacancies.json'
    with open(path, mode='w', encoding='utf-8') as my_file:
        json.dump(simple_vacancies, my_file)
