# import os
# import json
# import random
#
# datas = []
# base_path = os.listdir("./photo/tb/")
# for department in base_path:
#   d = list(os.listdir("./photo/tb/{0}/".format(department)))  #获取部门
#   for j in d:
#     path = ("./photo/tb/{0}/{1}".format(department, j))  #获取图片路径
#     name = os.path.splitext(j)[0] #获取姓名
#     test_data = {}
#     test_data["name"] = name
#     test_data["avatar"] = path
#     test_data["data"] = {}
#     test_data["data"]["department"] = department
#
#     # test_data = json.JSONEncoder(ensure_ascii=False).encode(test_data)
#     datas.append(test_data)
#     random.shuffle(datas)
# print(datas)
#
# with open('test.json', 'w') as f:
#     json.dump(datas, f)
#     # json.dump(datas, f, ensure_ascii=False)
