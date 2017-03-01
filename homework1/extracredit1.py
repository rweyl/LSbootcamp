import requests

header = {"Content-Type": "application/json; charset=utf-8"}

message = {"mymessage": "Hey LambdaSchool!!!"}

r = requests.post("https://LambdaSchool.com/contact", headers=header, data=message)

print(r.text)
