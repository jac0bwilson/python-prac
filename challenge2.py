f = open("challenge2-data.txt", "r")
output = ""
lines = f.readlines()
for line in lines:
    for char in line:
        if char.isalpha():
            output += char

print (output)
