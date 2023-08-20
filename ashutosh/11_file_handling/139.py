#
# * 139. Reading Data From A File


file = open("/home/diego/Desktop/stout_selenium/ashutosh/11_file_handling/files/data.txt", "r")

content = file.read()

print(content)

file.close()