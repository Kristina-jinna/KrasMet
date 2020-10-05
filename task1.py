import requests

def taskOne(url):
    sendRequestGet = requests.get(url,allow_redirects=True)
    with open(r'file1.txt', 'wb') as f:
        f.write(sendRequestGet.content)
    f.close()
    print('The file was written')


taskOne('https://www.ya.ru/')