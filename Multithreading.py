import threading

class Multithreading:
    def __init__(self):
        self.threads = {}  # Create dictionary of all names and threads for future calling

    def openInactiveThread(self, name: str, function, arguments: tuple):
        if name in self.threads.keys():
            print(f'Overwriting previous {name} thread')  # Notify user if overwriting thread

        self.threads[name] = threading.Thread(target=function, args=arguments, name=name)  # Pass values into threaded function

    def openActiveThread(self, name: str, function, arguments: tuple):
        self.openInactiveThread(name, function, arguments)
        self.threads[name].start()  # Activating thread

    def isThreadAlive(self, name: str):
        return (True if self.threads[name].is_alive() else False) if name in self.threads.keys() else False

    def runAllThreads(self, join: bool):
        for thread in self.threads.values():
            if thread.is_alive():
                thread.start()
                if join:
                    thread.join()  # Prevents the main thread from closing until all joined threads have closed
            else:
                del self.threads[thread.name]

    def runThreads(self, names: list[str], join: list[bool]):
        if len(names) != len(join):
            print('List length error')
        else:
            for i in range(len(names)):
                self.runThread(names[i], join[i])

    def runThread(self, name: str, join: bool):
        if self.isThreadAlive(name):
            self.threads[name].start()  # Find and start specific thread if found
            if join:
                self.threads[name].join()
        else:
            print(f'{name} not active')  # Notify user of thread absence

    def convertDaemon(self, name: str, status):
        if self.isThreadAlive(name):
            self.threads[name].setDaemon(status)  # Set thread to also be closed by the main thread

    def pruneInactiveThreads(self):
        remove = []
        for thread in self.threads:
            if not self.isThreadAlive(thread):
                remove.append(thread)  # Remove inactive threads
        for thread in remove:
            del self.threads[thread]
