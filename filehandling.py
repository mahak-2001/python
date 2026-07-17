
# # #absolute and manually path
# # # mode,path,encoding
# # # file=open("C:\Users\Monika\OneDrive\Documents\GitHub\python\python\loop.py","r",encoding="utf-8")

# file=open("test.py","r",encoding="utf-8")
# print(file.read())
# file.close()
# print(file.closed)

with open("set.py","r",encoding="utf-8") as file:
    print(file.read())
    file.close()
print(file.closed)