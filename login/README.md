# Login Example

The example in `web_login.py` shows aspects of automating making a login request to a website. A lot of information provided here came from the following YouTube [video](https://www.youtube.com/watch?v=fmf_y8zpOgA&feature=youtu.be).

The example here is specific to a rent portal website for an apartment complex; however, core parts of the request should be similar for most websites. The key components are the website url, request headers, and login data (i.e., request body).

### Login URL

The login url is the link where the website has its username and password login screen. This is where a user will enter his or her username and password to gain access to an account.

### Request Headers

Headers contain information used by the website to complete the request. Headers usually follow similar patterns for most websites, but there are certain to be differences across websites.

### Login Data (Request Body)

This is also known as form data or the body of the request that will contain login information, such as username and password. This information will be passed to establish a session.

### Using a Session After Authentication

After logging into a website via an automated process such as here, a session can be used to visit different pages of a website only available after being authenticated as a valid user.

### Python Login Broken Down and Explained

Define Headers and Login Data Using Python Dictionaries

```
headers = {
    "user-agent": "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}

login_data = {
    "utf8": "&#x2713;",
    "user[email]": "", #ENTER EMAIL HERE
    "user[password]": "", #ENTER PASSWORD HERE
    "commit": "Log in" #USED TO SPECIFY REQUEST IS FOR LOGIN ACTION
}
```

Create Session and Declare Login URL
```
with requests.Session() as s:
    #ENTER LOGIN URL HERE
    url = ""
```

Extract Content of Login URL to Make Request
```
r = s.get(url, headers=headers)
soup = BeautifulSoup(r.content)
login_data['authenticity_token'] = soup.find('input', attrs={"name": "authenticity_token"})["value"]
```

Make a POST Request Using Login URL, Headers, and Data to Establish Website Session
```
#GET WEBSITE SESSION
  r = s.post(url, data=login_data, headers=headers)
```

Enter Second URL to Navigate to After Establishing Session Through Login
```
#ENTER SECOND URL TO NAVIGATE TO NEW WEBSITE PAGE USING ESTABLISHED SESSION
#OPEN WEBPAGE TO ILLUSTRATE SUCCESSFUL LOGIN/SESSION ESTABLISHED
url2 = ""
r = s.get(url2, headers=headers)
webbrowser.open(r.url)
```
