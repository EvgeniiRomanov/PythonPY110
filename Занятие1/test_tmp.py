import os

os_name = os.name

print(os_name)

start_path = os.path.dirname()
print(start_path)

os.chdir("..")
os.getcwd()
print(start_path)