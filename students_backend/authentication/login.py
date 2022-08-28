from rest_framework.response import Response
from rest_framework.decorators import api_view
from firebase_admin import auth
from authentication import firebase_key
from authentication import pyrebase

def getUser(email):
    # get info of an existing user...
    return auth.get_user_by_email(email)

@api_view(["POST"])
def login(request):
    email = request.data["email"]
    password = request.data["password"]

    # sign in the user...
    if(pyrebase.signIn(email, password)):
        data = getUser(email)
        user_data = {"status": "valid" ,"username": data.display_name, "uid": data.uid, "verified": data.email_verified, "email": data.email}
        if(not data.email_verified):
            #send verification email...
            pyrebase.sendLink(email, password)

        return Response(user_data)

    else:
        # not on our database or password and email do no match
        return Response({"status": "invalid", "reason": "Password or email incorrect"})

@api_view(["POST"])
def reset(request):
    email = request.data["email"]

    if(pyrebase.resetPassword(email)):
        return Response({"status": "valid"})
    
    return Response({"status": "invalid"})
