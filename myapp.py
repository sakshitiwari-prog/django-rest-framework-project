# from re import S
import requests
URL='http://127.0.0.1:8000/studentinfo/1'
res=requests.get(url=URL)
data=res.json()
print(data)
