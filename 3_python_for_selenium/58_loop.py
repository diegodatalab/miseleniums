#
# * 58. File Handling

file = open("/home/diego/Desktop/stout_selenium/3_python_for_selenium/files/sample.txt", "r")

for line in file:
    print(line)

file.close()

