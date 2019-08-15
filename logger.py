def log(msg):
    f = open("python_log.txt", "a")
    f.write(msg)
    f.close()     


# open and read the file after the appending:
# f = open("demofile2.txt", "r")
# print(f.read())