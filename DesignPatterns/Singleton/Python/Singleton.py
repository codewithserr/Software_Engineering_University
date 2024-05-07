import threading
import time

class Singleton:
    _instance = None
    _mutex = threading.Lock()

    def __init__(self, value):
        self.value = value

    @classmethod
    def get_instance(cls, value):
        if cls._instance is None:
            with cls._mutex:
                if cls._instance is None:
                    cls._instance = cls(value)
        return cls._instance

    def some_business_logic(self):
        # ...
        pass

def thread_foo():
    time.sleep(1)
    singleton = Singleton.get_instance("FOO")
    print(singleton.value)

def thread_bar():
    time.sleep(1)
    singleton = Singleton.get_instance("BAR")
    print(singleton.value)

if __name__ == "__main__":
    print("If you see the same value, then singleton was reused (yay!)\n"
          "If you see different values, then 2 singletons were created (booo!!)\n\n"
          "RESULT:\n")

    t1 = threading.Thread(target=thread_foo)
    t2 = threading.Thread(target=thread_bar)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
