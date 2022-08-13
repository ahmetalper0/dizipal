import requests
import json
from bs4 import BeautifulSoup
from datetime import datetime

JSON_PATH = 'links.json'

def update_json(data):

    with open(JSON_PATH, 'w', encoding='utf-8') as file:

        json.dump(data, file, indent=4)

def add_link(link,status):

    with open(JSON_PATH, 'r', encoding='utf-8') as json_file:

        data = json.load(json_file)


    links = []

    for i in data:

        links.append(i['link']) 

    if link in links:

        for i in data:

            if i['link'] == link:

                i['status'] = status
                i['date'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                update_json(data)

            else:
                pass

    else:

        data.append({

            'status' : status,
            'link' : link,
            'date' : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            })

        update_json(data)

def finder(number1,number2,timeout):

    for number in range(number1,number2 + 1):

        url = f'https://dizipal{number}.com'

        try:
            
            r = requests.get(url, timeout=timeout)

            if r.status_code == 200:

                if BeautifulSoup(r.content,'html.parser').title.text == 'DiziPAL - dizi, film ve anime izle':

                    add_link(url,'success')

                else:

                    add_link(url, 'error')
            else:

                add_link(url, 'error')

        except:

            add_link(url, 'error')

def find_success():

    with open(JSON_PATH, 'r', encoding='utf-8') as json_file:

        data = json.load(json_file)

        for i in data:

            if i['status'] == 'success':

                print(f'''\n{i['link']} | {i['status']} | {i['date']}\n''')

