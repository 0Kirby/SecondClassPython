import requests
import json

url="http://voy.jxyouth.org.cn/voy_cms/wx/api.json?module=wxusermodule&action=applogin&name=13003484228&password=236322&apptoken=8888"
url2="http://voy.jxyouth.org.cn/voy_cms/app/V1.0/api.json"

r = requests.post(url)

with open('request.html','wb') as f:
    f.write(r.content)
print(json.loads(r.text)['data']['userToken'])

session = requests.Session()
data = {
    "apptoken":8888,
    "usertoken":json.loads(r.text)['data']['userToken'],
    "module":"secmodule",
    "action":"courselist",
    "type":"school",
    "word":"",
    "page_index":1,
    "page_size":10
}

headers = {
    "Accept":"application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.8",
    "Connection":"keep-alive",
    "Content-Length":"139",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie":"JSESSIONID=69F5CFB6DED6F8E9B28E58427541DB03; Hm_lvt_bd81f02e5329554415de9ee15f916a98=1529036127",
    "Host":"voy.jxyouth.org.cn",
    "Origin":"http://voy.jxyouth.org.cn",
    "Referer":"http://voy.jxyouth.org.cn/resource/site_1/youth_wx/login.html",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4092.1 Safari/537.36",
}
r2 = session.post(url2, headers=headers, data=data)
print(r2.text)
with open('request2.html','wb') as f:
    f.write(r2.content)

session2 = requests.Session()
data = {
    "apptoken":8888,
    "usertoken":json.loads(r.text)['data']['userToken'],
    "module":"secmodule",
    "action":"apply",
    "id":json.loads(r2.text)['data']['list'][0]['id']
}

headers = {
    "Accept":"application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.8",
    "Connection":"keep-alive",
    "Content-Length":"139",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie":"JSESSIONID=69F5CFB6DED6F8E9B28E58427541DB03; Hm_lvt_bd81f02e5329554415de9ee15f916a98=1529036127",
    "Host":"voy.jxyouth.org.cn",
    "Origin":"http://voy.jxyouth.org.cn",
    "Referer":"http://voy.jxyouth.org.cn/resource/site_1/youth_wx/login.html",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4092.1 Safari/537.36",
}
r3 = session.post(url2, headers=headers, data=data)
print(r3.text)
with open('request3.html','wb') as f:
    f.write(r3.content)
