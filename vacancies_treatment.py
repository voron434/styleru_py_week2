from filework_helpers import dump_data
from filework_helpers import load_data

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
    vacancies_data = load_data(input_path)
    if not vacancies_data:
        print('File not found, sorry...')
        raise SystemExit
    simple_vacancies = []
    for vacancy in vacancies_data['objects']:
        parameters = get_vacancy_params(vacancy)
        simple_vacancies.append(parameters)
    output_path = 'simple_vacancies.json'
    dump_data(simple_vacancies, 'simple_vacancies.json')
