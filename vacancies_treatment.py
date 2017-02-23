import json
from helpers import load_data

def get_vacancy_params(vacancy):
    parameters = {
            'name': vacancy['profession'],
            'requirements': vacancy['candidat'],
            'payment_from': vacancy['payment_from'],
            'currency': vacancy['currency']
        }
    return parameters

if __name__ == '__main__':
    data = load_data()
    simple_vacancies = []
    for vacancy in data['objects']:
        parameters = get_vacancy_params(vacancy)
        simple_vacancies.append(parameters)
    path = 'simple_vacancies.json'
    with open(path, mode='w', encoding='utf-8') as my_file:
        json.dump(simple_vacancies, my_file)
