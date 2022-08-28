from rest_framework.response import Response
from rest_framework.decorators import api_view
from firebase_admin import auth
from authentication import firebase_key
from authentication import pyrebase

# check userType
def isUserValid(kind, email):
    domain = email.split('@')[1]

    if(domain == "students.wits.ac.za" and kind == 'student'):
        return True
    elif(domain == "wits.ac.za" and kind == 'staff'):
        return True
    else:
        return False

def createAccount(userEmail, userPassword, username):
    try:
        auth.create_user(
        email = userEmail,
        email_verified = False,
        password = userPassword,
        display_name = username,
        disabled=False)

        #send the veryfication email...
        pyrebase.sendLink(userEmail, userPassword)
        return {"status": 'valid', "reason": 'Account created'}

    except:
        #failed to create account 
        return {"status": 'invalid', "reason": 'Account exits'}


@api_view(['POST'])
def signUp(request):
    kind = request.data["kind"]
    email = request.data["email"]
    password = request.data["password"]
    username = request.data["username"]

    if(isUserValid(kind, email)):
        return Response(createAccount(email, password, username))
    else:
        return Response({"status": 'invalid', "reason": 'Use correct Wits account'})

    