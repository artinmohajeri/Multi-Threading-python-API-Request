import threading, requests, time

# using multy-threading programming for sending requests in a efficient way ↓↓↓
start = time.time()
class MyThread(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url
    def send_request(self):
        requests.get(self.url)
    def run(self):
        self.send_request()

thread1 = MyThread("https://github.com/artinmohajeri")
thread2 = MyThread("https://github.com/artinmohajeri")
thread3 = MyThread("https://github.com/artinmohajeri")
thread4 = MyThread("https://github.com/artinmohajeri")

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread1.join()
thread2.join()
thread3.join()
thread4.join()
end = time.time()
print("It takes", round(end - start, 2), "seconds to run multy-threading requests")



# Ordinary requests in python ↓↓↓
start = time.time()
requests.get("https://github.com/artinmohajeri")
requests.get("https://github.com/artinmohajeri")
requests.get("https://github.com/artinmohajeri")
requests.get("https://github.com/artinmohajeri")
end = time.time()
print("It takes", round(end - start, 2), "seconds to run ordinary requests")
