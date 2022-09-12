from rest_framework.response import Response
from rest_framework.decorators import api_view
from authentication import firebase_key
from firebase_admin import firestore 
import firebase_admin

db = firebase_admin.firestore.client()

@api_view(["GET"])
def get_bus_schedule(request):
    
    schedule = []
    # fetch all the list of buses...
    docs = db.collection('Buses').stream()

    for doc in docs:
        schedule.append(doc.to_dict())

    return Response(schedule)