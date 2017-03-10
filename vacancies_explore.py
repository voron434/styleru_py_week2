import matplotlib.pyplot as plt
from filework_helpers import load_data

def make_dict_of_languages():
    dict_of_languages ={}
    languages = ['python', 'c++', 'c#', 'vb', 'java', 'delphi', 'css', 'html', 'php', 'js', 'sql']
    for language in languages:
        dict_of_languages[language] = {'popularity': 0, 'payment_from': 0}
    return dict_of_languages

def collect_statistics_into_chart(data, chart):
    for vacancy in data:
        for language in chart:
            if not vacancy['requirements'] or not vacancy['name']:
                continue #for some reason some of them are empty...
            if (language in vacancy['name'].lower()) or (language in vacancy['requirements'].lower()):
                chart[language]['popularity'] += 1 #this slot for popularity
                chart[language]['payment_from'] += vacancy['payment_from']
    for language in chart:
        if chart[language]['payment_from'] != 0:
            chart[language]['average_payment_from'] = chart[language]['payment_from']/chart[language]['popularity']
    return chart

def draw_graph(chart):
    plt.xlabel('Language')
    plt.ylabel('Average value of payment_from')
    plt.title('Statistics')
    languages, payments = [language for language in chart], [chart[language]['average_payment_from'] for language in chart]
    plt.bar(range(len(chart)), payments, tick_label=languages)
    plt.savefig('statistics.png')
    plt.show()

if __name__ == '__main__':
    path = input('Enter path to DataBase:')
    vacancies_data = load_data(path)
    if not vacancies_data:
        print('File not found, sorry...')
        raise SystemExit
    chart = make_dict_of_languages()
    chart = collect_statistics_into_chart(vacancies_data, chart)
    draw_graph(chart)
