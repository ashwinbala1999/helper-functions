import os
import pickle

import firebase_admin
from firebase_admin import credentials, storage


# demo class to pickle to firebase storage bucket
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"This is a property of {self.name} who is {self.age} years old."


# initialize firebase-admin
cred = credentials.Certificate(
    "credentials.json")

firebase_admin.initialize_app(cred, {
    "storageBucket": "flask-demo-4809b.appspot.com"
})

# initialize bucket object
bucket = storage.bucket()


# this method saves a python object to firebase cloud storage bucket as a pickle file
def upload_file(object, filename):
    with open(filename, 'wb') as f:
        pickle.dump(object, f)

    blob = bucket.blob(filename)
    blob.upload_from_filename(filename)

    os.remove(filename)


# this method downloads file from bucket and then reads it
def read_file_1(filename):
    blob = bucket.blob(filename)
    blob.download_to_filename(filename)

    with open(filename, 'rb') as f:
        obj = pickle.load(f)

    os.remove(filename)

    return obj


# this method reads file from bucket directly
def read_file_2(filename):
    blob = bucket.blob(filename)
    obj = pickle.load(blob.open('rb'))

    return obj


# the below lines demonstrate how to use the above methods
# upload files to bucket
obj1 = Person("jdoe99", 22)
obj2 = Person("jdoe97", 24)

upload_file(obj1, "jdoe99.pkl")
upload_file(obj2, "jdoe97.pkl")

# read files from bucket
obj1 = read_file_2("jdoe99.pkl")
obj2 = read_file_2("jdoe97.pkl")

print(obj1)  # Output: This is a property of jdoe99 who is 22 years old.
print(obj2)  # Output: This is a property of jdoe97 who is 24 years old.
