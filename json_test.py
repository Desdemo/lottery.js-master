import json

a = [
    {
        "name": "东东",
        "avatar": "./photo/东东.jpg",
        "data": {
            "company": "腾讯",
            "title": "董事长"
        }
    },
    {
        "name": "结界",
        "avatar": "./photo/77777.jpg",
        "data": {
            "company": "百度",
            "title": "后端开发工程师"
        }
    }]


with open("test.json", "rb") as f:
  print(f)


with open("sample-data.json", "rb") as f:
  print(type(a[0]))
