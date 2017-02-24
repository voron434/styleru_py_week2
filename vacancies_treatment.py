import json

def get_vacancy_params(vacancy):
    parameters = {
            'name': vacancy['profession'],
            'requirements': vacancy['candidat'],
            'payment_from': vacancy['payment_from'],
            'currency': vacancy['currency']
        }
    return parameters

def load_data():
    print('Enter path to DataBase:')
    path = input()
    try:
        with open(path, mode='r', encoding='utf-8') as my_file:
            data = json.load(my_file)
            return data
    except FileNotFoundError:
        print('File not found, sorry...')
        raise SystemExit

if __name__ == '__main__':
    data = load_data()
    simple_vacancies = []
    for vacancy in data['objects']:
        parameters = get_vacancy_params(vacancy)
        simple_vacancies.append(parameters)
    path = 'simple_vacancies.json'
    with open(path, mode='w', encoding='utf-8') as my_file:
        json.dump(simple_vacancies, my_file)
