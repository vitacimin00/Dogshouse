import random
import requests
import time
from datetime import datetime




headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'Origin': 'https://onetime.dog',
        'Referer': 'https://onetime.dog/',
        'content-length': '0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site'
    }
def load_credentials():
    try:
        with open('query_id.txt', 'r') as f:
            queries = [line.strip() for line in f.readlines()]
        return queries
    except FileNotFoundError:
        print("File query_id.txt not found.")
        return [  ]
    except Exception as e:
        print("Terjadi kesalahan saat memuat token:", str(e))
        return [  ]

def get_reward(query):
    time.sleep(2)
    url = f'https://api.onetime.dog/join'
    try:
        response_codes_done = range(200, 250)
        response_code_failed = range(500, 530)
        response_code_notfound = range(400, 413)
        response = requests.post(url, headers=headers, data=query)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_failed:
            print(response.text)
            return None
        elif response.status_code in response_code_notfound:
            print(response.text)
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def calendar(id):
    time.sleep(2)
    url = f'https://api.onetime.dog/advent/calendar?user_id={id}'
    try:
        response_codes_done = range(200, 250)
        response_code_failed = range(500, 530)
        response_code_notfound = range(400, 413)
        response = requests.get(url, headers=headers,)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_failed:
            print(response.text)
            return None
        elif response.status_code in response_code_notfound:
            print(response.text)
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def timer(id):
    time.sleep(2)
    url = f'https://api.onetime.dog/advent/calendar/timer?user_id={id}'
    try:
        response_codes_done = range(200, 250)
        response_code_failed = range(500, 530)
        response_code_notfound = range(400, 413)
        response = requests.get(url, headers=headers,)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_failed:
            print(response.text)
            return None
        elif response.status_code in response_code_notfound:
            print(response.text)
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def checkin(id, ids):
    url = f'https://api.onetime.dog/advent/calendar/check?user_id={id}&day={ids}'
    try:
        response_codes_done = range(200, 250)
        response_code_failed = range(500, 530)
        response_code_notfound = range(400, 413)
        response = requests.post(url, headers=headers)
        if response.status_code in response_codes_done:
            print(f"Checkin day {ids} Done")
        elif response.status_code in response_code_failed:
            print(response.text)
            return None
        elif response.status_code in response_code_notfound:
            print(response.text)
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def visit(id):
    url = f'https://api.onetime.dog/advent/calendar/first-visit?user_id={id}'
    try:
        response_codes_done = range(200, 250)
        response_code_failed = range(500, 530)
        response_code_notfound = range(400, 413)
        response = requests.get(url, headers=headers)
        if response.status_code in response_codes_done:
            json = response.json()
            visit = json.get('FirstVisit', False)
            print(f"first Visit {visit}")
        elif response.status_code in response_code_failed:
            print(response.text)
            return None
        elif response.status_code in response_code_notfound:
            print(response.text)
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def main():
        ids = load_credentials()
        for index, id in enumerate(ids):
            print(f'======== {index+1} ========')
            data_reward = get_reward(id)
            if data_reward is not None:
                print(f"Username : {data_reward.get('username','')} | Age : {data_reward.get('age',0)} | Balance : {data_reward.get('wallet_balance',0)}")
                id = data_reward.get('telegram_id')
                ref = data_reward.get('reference')
                is_withdrawn = data_reward.get('is_withdrawn', True)
                friendly_wallet_address = data_reward.get('friendly_wallet_address',None)
                print(f"Address : {friendly_wallet_address} | {is_withdrawn}")
                time.sleep(2)
                visit(id)
                data_calendar = calendar(id)
                if data_calendar is not None:
                    for datas in data_calendar:
                        ids = datas.get('ID')
                        IsOpened = datas.get('IsOpened')
                        IsAvailable = datas.get('IsAvailable')
                        IsChecked = datas.get('IsChecked')
                        Text = datas.get('Text')
                        Title = Text.get('Title')
                        if IsAvailable == True:
                            if IsChecked == True:
                                print(f"Checkin Day {ids} Done, {Title}")
                            else:
                                data_timer = timer(id)
                                if data_timer is not None:
                                    checkin(id, ids)


               
                    
            else:
                print('Users not found')
            time.sleep(3)
            

if __name__ == "__main__":
    main()