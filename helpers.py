import requests
import json
import matplotlib.pyplot as plt
from getpass import getpass


def get_api_key():
    api_key = getpass('Enter your api key:')
    header = {'X-Api-App-Id': api_key}
    try:
        parametrs = {'count':1, 'catalogue_id': 48}
        reqest = requests.get('https://api.superjob.ru/2.0/vacancies', headers=header, params=parametrs)
        code_of_error = reqest.json()["subscription_id"]
    except KeyError:
        print('sorry, I guess your api key is invalid...')
        raise SystemExit
    return api_key

def send_reqest(api_key):
    header = {'X-Api-App-Id': api_key}
    parametrs = {'keyword': 'программист', 'town': '4', 'count': 100, 'catalogue_id': 48}
    reqest = requests.get('https://api.superjob.ru/2.0/vacancies', headers=header, params=parametrs)
    return reqest.json()

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

def get_vacancy_params(vacancy):
    parameters = {
            'name': vacancy['profession'],
            'requirements': vacancy['candidat'],
            'payment_from': vacancy['payment_from'],
            'agreement': vacancy['agreement'],
            'currency': vacancy['currency']
        }
    return parameters

def make_list_of_languages():
    languages = {'1c': [0, 0],
                 'vba': [0, 0],
                 'python': [0, 0],
                 'c': [0, 0],
                 'c++': [0, 0],
                 'c#': [0, 0],
                 'vb': [0, 0],
                 'java': [0, 0],
                 'delphi': [0, 0],
                 'haskell': [0, 0],
                 'assembler': [0, 0],
                 'pascal': [0, 0],
                 'css': [0, 0],
                 'html': [0, 0],
                 'php': [0, 0],
                 'js': [0, 0],
                 'ruby': [0, 0],
                 'swift': [0, 0],
                 }
    return languages

def find_prog_lang(data, chart):
    for vacancy in data:
        for language in chart:
            if vacancy['requirements'] == None:
                continue
            if vacancy['name'] == None:
                continue
                """
                really strange piece of code.
                i don't know why some of names or requirements are empty, by the way it is fixed.
                """
            if (language in vacancy['name'].lower()) or (language in vacancy['requirements'].lower()):
                chart[language][0] += 1
                if vacancy['payment_from'] != 0:
                    chart[language][1] += vacancy['payment_from']
    for language in chart:
        if chart[language][1] != 0:
            chart[language][1] = chart[language][1]/chart[language][0]
    return chart

def draw_graph(chart):
    plt.xlabel('Language')
    plt.ylabel('Average value of payment')
    plt.title('Statistics')
    languages, payments = [language for language in chart], [chart[payment][1] for payment in chart]
    plt.bar(range(len(chart)), payments, tick_label=languages, label="kek")
    plt.show()
