from getpass import getpass
import requests
from filework_helpers import dump_data

def get_api_key():
    api_key = getpass('Enter your api key:')
    header = {'X-Api-App-Id': api_key}
    try:
        parameters = {'count': 1, 'catalogue_id': 48}
        reqest = requests.get('https://api.superjob.ru/2.0/vacancies', headers=header, params=parameters)
        code_of_error = reqest.json()["subscription_id"]
        return api_key
    except KeyError:
        return None

def send_reqest(api_key, count=100):
    header = {'X-Api-App-Id': api_key}
    parametrs = {'keyword': 'программист',
                 'town': '4', #id Москвы 
                 'count': count,
                 'catalogue_id': 48, #каталог "Разработка, программирование"
                 'no_agreement': 1}
    reqest = requests.get('https://api.superjob.ru/2.0/vacancies', headers=header, params=parametrs)
    return reqest.json()

if __name__ == '__main__':
    api_key = get_api_key()
    if not api_key:
        print('sorry, I guess your api key is invalid...')
        raise SystemExit
    all_vacancies = send_reqest(api_key)
    path = 'vacancies.json'
    dump_data(all_vacancies, path)
    print('vacancies saved into %s' % path)
