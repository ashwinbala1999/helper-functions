import pickle


def makePickle(path, data):
  with open(path, 'wb') as f:
    pickle.dump(data, f)


def openPickle(path):
  with open(path, 'rb') as f:
    data = pickle.load(f)
  return data
