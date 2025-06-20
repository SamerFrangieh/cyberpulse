import requests

API_KEY = 'yg48QpXuqnH4iEmzyGtqLBu0qqmsMwbT'

def get_shodan_info(ip):
    url = f'https://api.shodan.io/shodan/host/{ip}?key={API_KEY}'
    try:
        r = requests.get(url)
        return r.json()
    except Exception as e:
        return {'error': str(e)}
