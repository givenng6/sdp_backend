from rest_framework.response import Response
from rest_framework.decorators import api_view
from authentication import firebase_key
from firebase_admin import firestore 
import firebase_admin

db = firebase_admin.firestore.client()

@api_view(["POST"])
def add_sub(request):
    email = request.data["email"]
    services = request.data["service"]

    ref = db.collection("Users").document(email)

    ref.update({u'capital': True})




    