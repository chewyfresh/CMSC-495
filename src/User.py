import pickle

class User:
    def __init__(self, username, password):
        self._pickled = pickle.dump(username + "\t" + password)
       
    def pickled(self):
        return self._pickled