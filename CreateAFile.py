# x = create file
#f = open("myfile.txt", "x")
"""
f = open("files/myfile.txt", "a")
f.write("\nNow the file has more content!")
f.close()

f = open("files/myfile.txt", "r")
print(f.read())
f.close()
"""
f = open("files/myfile.txt", "w")
f.write("Woops! You've been hacked")
f.close()

f = open("files/myfile.txt", "r")
print(f.read())
