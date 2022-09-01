from rest_framework.response import Response
from rest_framework.decorators import api_view
from authentication import firebase_key
from firebase_admin import firestore 
import firebase_admin

db = firebase_admin.firestore.client()

# method to be used under auth...
def add_user(email, username, role):
    data = {"username": username, "role": role}
    db.collection("Users").document(email).set(data)

