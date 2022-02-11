import requests

def request(endpoint, param):
    r = requests.get(f'https://api.jeyy.xyz/image/{endpoint}', params=param)
    return r.content
            
                
    