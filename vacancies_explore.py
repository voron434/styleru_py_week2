from helpers import load_data
from helpers import find_prog_lang
from helpers import make_list_of_languages
from helpers import draw_graph

if __name__ == '__main__':
    data = load_data()
    chart = make_list_of_languages()
    chart = find_prog_lang(data, chart)
    draw_graph(chart)
