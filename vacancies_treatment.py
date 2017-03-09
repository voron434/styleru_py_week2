import json
import os

def get_vacancy_params(vacancy):
    parameters = {
            'name': vacancy['profession'],
            'requirements': vacancy['candidat'],
            'payment_from': vacancy['payment_from'],
            'currency': vacancy['currency']
        }
    return parameters

if __name__ == '__main__':
    input_path = input('Enter path to DataBase:')
    if not os.path.exists(input_path):
        print('File not found, sorry...')
        raise SystemExit
    with open(input_path, mode='r', encoding='utf-8') as my_file:
        data = json.load(my_file)
    simple_vacancies = []
    for vacancy in data['objects']:
        parameters = get_vacancy_params(vacancy)
        simple_vacancies.append(parameters)
    output_path = 'simple_vacancies.json'
    with open(output_path, mode='w', encoding='utf-8') as my_new_file:
        json.dump(simple_vacancies, my_new_file)
