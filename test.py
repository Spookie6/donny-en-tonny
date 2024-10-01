import threading

def ja():
    while True:
        print("ja")

thread = threading.Thread(target=ja,)
thread.start()

while True:
    print(2)