import json
import matplotlib.pyplot as plt

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

def make_list_of_languages():
    languages = {'1c': [0, 0],
                 'python': [0, 0],
                 'c++': [0, 0],
                 'c#': [0, 0],
                 'vb': [0, 0],
                 'java': [0, 0],
                 'delphi': [0, 0],
                 'css': [0, 0],
                 'html': [0, 0],
                 'php': [0, 0],
                 'js': [0, 0],
                 'sql': [0, 0],
                 }
    return languages

def find_prog_lang(data, chart):
    for vacancy in data:
        for language in chart:
            if (vacancy['requirements'] == None) or (vacancy['name'] == None):
                continue #for some reason some of them are empty...
            if (language in vacancy['name'].lower()) or (language in vacancy['requirements'].lower()):
                chart[language][0] += 1 #this slot for popularity
                chart[language][1] += vacancy['payment_from']
    for language in chart:
        if chart[language][1] != 0:
            chart[language][1] = chart[language][1]/chart[language][0]
    return chart

def draw_graph(chart):
    plt.xlabel('Language')
    plt.ylabel('Average value of payment_from')
    plt.title('Statistics')
    languages, payments = [language for language in chart], [chart[payment][1] for payment in chart]
    plt.bar(range(len(chart)), payments, tick_label=languages)
    plt.show()

if __name__ == '__main__':
    data = load_data()
    chart = make_list_of_languages()
    chart = find_prog_lang(data, chart)
    draw_graph(chart)
