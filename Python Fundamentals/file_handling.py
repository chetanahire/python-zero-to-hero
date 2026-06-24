f = open("sample.txt")
# f = open("C:\AIML\python-zero-to-hero\Python Fundamentals\sample.txt")
# print(f.read())
# print(f.readline())
f.close()


# Using With statement
with open("sample.txt") as f:
#   print(f.read())
  print(f.read(6))

with open("sample.txt") as f:
  for x in f:
    print(f)

#Append - append new content at end
with open("sample.txt", "a") as f:
  f.write("This is extra text added")

with open("sample.txt") as f:
  print(f.read())

#write - override content
# with open("sample.txt", "w") as f:
#   f.write("This is new text added")

with open("sample.txt") as f:
  print(f.read())

# f = open("myfile.txt", "x")

import os
if os.path.exists("myfile.txt"):
  os.remove("myfile.txt")
else:
  print("The file does not exist")

import os
os.rmdir("myfolder")
