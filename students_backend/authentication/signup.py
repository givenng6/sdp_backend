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
    auth.create_user(
    email = userEmail,
    email_verified = False,
    password = userPassword,
    display_name = username,
    disabled=False)


@api_view(['POST'])
def signUp(request):
    kind = request.data["kind"]
    email = request.data["email"]
    password = request.data["password"]
    username = request.data["username"]


    if(isUserValid(kind, email)):
        createAccount(email, password, username)
        pyrebase.sendLink(email, password)
        return Response('Wits Account')
    else:
        return Response('Not Wits account')

    