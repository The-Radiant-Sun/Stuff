import threading

class Mulitithreading:
    def __init__(self):
        self.threads = {}

    def openThread(self, name: str, function, arguments: tuple):
        if name in self.threads.keys():
            print(f'Overwriting previous {name} thread')

        self.threads[name] = threading.Thread(target=function, args=arguments)

    def runAllThreads(self):
        for thread in self.threads.values():
            thread.start()

    def runThreads(self, name: str):
        if name in self.threads.keys():
            self.threads[name].start()
        else:
            print(f'{name} not found')

