#
# * 58. File Handling

file = open("/home/diego/Desktop/stout_selenium/3_python_for_selenium/files/sample.txt", "r")

lines = file.readlines() # ! retorna lista de linhas

print(lines)

for line in lines:
    print(line)

file.close()

