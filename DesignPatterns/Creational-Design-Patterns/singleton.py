from threading import Lock, Thread

class SingletonMeta(type):
    _instances = {}
    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    def __init__(self):
        print("Creating database connection")

    def query(self, query):
        print(f"Executing query: {query}")

def create_database():
    db = Database()
    db.query("SELECT * FROM users")

if __name__ == "__main__":
    threads = []
    for i in range(5):
        thread = Thread(target=create_database)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    db = Database()
    db.query("SELECT * FROM products")