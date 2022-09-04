from rest_framework.response import Response
from rest_framework.decorators import api_view
from authentication import firebase_key
from firebase_admin import firestore 
import firebase_admin

db = firebase_admin.firestore.client()

@api_view(["POST"])
def add_sub(request):
    email = request.data["email"]
    service = request.data["service"]

    ref = db.collection("Users").document(email)
    ref.update({'subs': firestore.ArrayUnion([service])})

    return Response({"status": "sent"})

@api_view(["POST"])
def get_sub(request):
    email = request.data["email"]

    ref = db.collection('Users').document(email)

    doc = ref.get()
    subs = []
    try:
        subs = doc.to_dict()["subs"]
    except:
        pass

    return Response({"subs": subs})



    