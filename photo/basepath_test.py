import os
import fnmatch
import glob
#
# def pwd(d):
#   ls = os.listdir(d)
#   b = []
#   for i in d:
#     if os.path.isdir(i):
#       b.append(i)
#   return b
#
#
# print(pwd())
#
# a = os.listdir(os.getcwd())
#
# b = []
# for i in a:
#   if os.path.isdir(i):
#     b.append(i)
#
# ls_root = []
# ls_a = []
# ls_jpg = []
# for root, dirs, files in os.walk(os.getcwd(),True):
#     print("root:{0}".format(root))
#     print("dirs:{0}".format(dirs))
#     print("files:{0}".format(files))
#     print(len(dirs))
#     if len(dirs) > 0:
#       ls_a.append(dirs)
#     ls_root.append(root)
#
#     ls_jpg = glob.glob('.jpg')
#
#     for name in files:
#       if fnmatch.fnmatch(name, '*.jpg'):
#         print((files))
#
#       else:
#         break
#
#     print("-------------------------------")
#
# print(ls_a)
# print(ls_root)
# print("-------------------------------")
# print(ls_jpg)

a = os.getcwd()
print(a)
