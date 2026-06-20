try:
    open(file.txt)
    print("file found")
except Exception as e:
    print(e)