import os
import json
import random


d = os.listdir(os.getcwd())
base_src = os.path.basename(os.getcwd())  # 相对路径 根目录名称
b = []

for i in d:
  if os.path.isdir(i):  # 获取子目录
    b.append(i)

for i in b:
  datas = []
  a = i
  b = "./{0}/".format(a)
  base_path = os.listdir(b)

  for department in base_path:
    d = list(os.listdir(b + "{0}/".format(department)))  #获取部门

    for j in d:
      path = ("./" + base_src + "/" + a + "/" + "{0}/{1}".format(department, j))  # 获取图片路径
      name = os.path.splitext(j)[0]  # 获取姓名
      photo_data = {}
      photo_data["name"] = name
      photo_data["avatar"] = path
      photo_data["data"] = {}
      photo_data["data"]["department"] = department

      #  photo_data = json.JSONEncoder(ensure_ascii=False).encode(photo_data)
      datas.append(photo_data)
      random.shuffle(datas)  # 生成随机列表
    with open('../json_data/{0}.json'.format(a), 'w') as f:  # 写入JSON文件
      json.dump(datas, f)
      # json.dump(datas, f, ensure_ascii=False)





