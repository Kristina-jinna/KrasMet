import requests

class User:
    def __init__(self, id, email, first_name, last_name, avatar):
        self.id = id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.avatar = avatar

class Ad:
    def __init__(self, company, url, text):
        self.company = company
        self.url = url
        self.text=text

class Connection():
    def __init__(self, http, host):
        self.http = http
        self.host = host
        url = self.setUrl()
        r = self.setConnect()

    def getHttp(self):
        return self.http

    def getHost(self):
        return self.host

    def setUrl(self):
        self.url = (f"{self.getHttp()}://{self.getHost()}")

    def getUrl(self):
        return self.url

    def setConnect(self):
        try:
            self.r = requests.get(self.getUrl())
            print("Connection satisfy!")
            print(self.r)
        except requests.ConnectionError as e:
            print("Connection error!", e)
            raise SystemExit(e)
        except requests.exceptions.RequestException as e:
            print("Request Error", e)

    def getConnect(self):
        return self.r

    def getListOfUser(self,listParam):
        strUrl = self.getConnect().url
        for i in listParam:
            strUrl = strUrl + i + '/'
        print("Status ", requests.get(strUrl).status_code)
        listOfUsers = []
        for i in requests.get(strUrl).json()['data']:
            listOfUsers.append(i)
            print(i)
        return listOfUsers

    def getCurrentUser(self,listParam,n):
        strUrl = self.getConnect().url
        for i in listParam:
            strUrl = strUrl+i+'/'
        data = {'id':str(n)}
        r = requests.get(strUrl,params = data)
        print("Status ", r.status_code)
        listOfUser = []
        listOfUser.append(r.json()['data'])
        us1 = User(r.json()['data']['id'],r.json()['data']['email'],r.json()['data']['first_name'],r.json()['data']['last_name'],r.json()['data']['avatar'])
        company = Ad(r.json()['ad']['company'],r.json()['ad']['url'],r.json()['ad']['text'])
        print(" First name:",us1.first_name,'\n',"Last name: ", us1.last_name,'\n', "Email: ",us1.email,'\n', "Avatar: ",us1.avatar)
        return listOfUser



#if __name__ == "__main__":
#    con = Connection('https', 'reqres.in')
#    con.getListOfUser(['api', 'users'])
#    con.getCurrentUser(['api', 'users'], 1)
