from helpers import send_reqest
from helpers import get_api_key
import json


if __name__ == '__main__':
    api_key = get_api_key()
    big_data = send_reqest(api_key)
    path = 'vacancies.json'
    with open(path, mode='w', encoding='utf-8') as my_file:
        json.dump(big_data, my_file)
