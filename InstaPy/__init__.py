import requests
from .utils import tmp_output, find, fall, save, payload, TmpObject

class Instagram:
    def __init__(self, cookie: str) -> None:
        self.session = requests.session()
        self.session.cookies['cookie'] = cookie

        __src = self.session.get('https://www.instagram.com/').text
        #--> user information 
        self.username = find(r'"username":"(.*?)"', __src).group(1)
        self.id = find(r'"id":"(.*?)"', __src).group(1)
        self.name = find(r'"full_name":"(.*?)"', __src).group(1)
        self.headers = {'authority': 'www.instagram.com','accept': '*/*','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','content-type': 'application/x-www-form-urlencoded','origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/','sec-ch-prefers-color-scheme': 'dark','sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"','sec-ch-ua-full-version-list': '"Not A(Brand";v="8.0.0.0", "Chromium";v="132.0.6961.0"','sec-ch-ua-mobile': '?1','sec-ch-ua-model': '"23108RN04Y"','sec-ch-ua-platform': '"Android"','sec-ch-ua-platform-version': '"15.0.0"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36','x-asbd-id': '359341','x-csrftoken': find(r'"csrf_token":"(.*?)"', __src).group(1)}
        self.base_data = payload(source=__src)

