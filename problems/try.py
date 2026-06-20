try:
    file = open('trial.txt')
except Exception as e:
    print(e)
else:
    print(file.read())
    file.close()
finally:
    print("executing the file......")
