rom getpass import getpass
import json
import requests

def get_api_key():
    api_key = getpass('Enter your api key:')
    header = {'X-Api-App-Id': api_key}
    try:
        parametrs = {'count': 1, 'catalogue_id': 48}
        reqest = requests.get('https://api.superjob.ru/2.0/vacancies', headers=header, params=parametrs)
        code_of_error = reqest.json()["subscription_id"]
    except KeyError:
        print('sorry, I guess your api key is invalid...')
        raise SystemExit
    return api_key

def send_reqest(api_key, count=100):
    header = {'X-Api-App-Id': api_key}
    parametrs = {'keyword': 'программист',
                 'town': '4', 'count': count,
                 'catalogue_id': 48,
                 'no_agreement': 1}
    reqest = requests.get('https://api.superjob.ru/2.0/vacancies', headers=header, params=parametrs)
    return reqest.json()

if __name__ == '__main__':
    api_key = get_api_key()
    big_data = send_reqest(api_key)
    path = 'vacancies.json'
    with open(path, mode='w', encoding='utf-8') as my_file:
        json.dump(big_data, my_file)
