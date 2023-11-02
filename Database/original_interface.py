class Database:
    def __init__(self, key_func):
        # Initialize with the function key_func that takes a key and returns a
        self.key_func = key_func

    def add(self, key):
        raise NotImplementedError("Add")

    def get(self, key):
        raise NotImplementedError("Get")
