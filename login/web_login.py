import requests
import webbrowser
from bs4 import BeautifulSoup

headers = {
    "user-agent": "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}

login_data = {
    "utf8": "&#x2713;",
    "user[email]": "", #ENTER EMAIL HERE
    "user[password]": "", #ENTER PASSWORD HERE
    "commit": "Log in" #HEADER FOR LOGIN ACTION
}

with requests.Session() as s:
    #ENTER LOGIN URL HERE
    url = ""

    #GET LOGIN URL
    #USE LOGIN URL CONTENT TO EXTRACT VALUES FOR REQUEST
    #EXTRACT authenticity_token VALUE FROM HTML for header
    r = s.get(url, headers=headers)
    soup = BeautifulSoup(r.content)
    login_data['authenticity_token'] = soup.find('input', attrs={"name": "authenticity_token"})["value"]

    #GET WEBSITE SESSION
    r = s.post(url, data=login_data, headers=headers)

    #ENTER SECOND URL TO NAVIGATE TO NEW WEBSITE PAGE USING ESTABLISHED SESSION
    #OPEN WEBPAGE TO ILLUSTRATE SUCCESSFUL LOGIN/SESSION ESTABLISHED
    url2 = ""
    r = s.get(url2, headers=headers)
    webbrowser.open(r.url)
