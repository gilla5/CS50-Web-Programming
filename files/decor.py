def announce(f):
    def wrapper():
        print("start")
        f()
        print("end")
    return wrapper

@announce
def hello():
    print("hello world")