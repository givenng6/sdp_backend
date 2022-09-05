import pyrebase

pyre_cred = {
  "apiKey": "AIzaSyD5hma8Y5uVWKnG0kOzurCRedMR9Er1uCM",
  "authDomain": "wits-services-ea5cf.firebaseapp.com",
  "projectId": "wits-services-ea5cf",
  "storageBucket": "wits-services-ea5cf.appspot.com",
  "messagingSenderId": "147092371359",
  "appId": "1:147092371359:web:501ef87c23a1d4814dafaa",
  "measurementId": "G-VQ8DBKB9T1",
  "databaseURL": "null",
}

app = pyrebase.initialize_app(pyre_cred)
auth = app.auth()

# send veryfication link...
def sendLink(email, password):
    try:
      user = auth.sign_in_with_email_and_password(email, password)
      # before the 1 hour expiry:
      user = auth.refresh(user['refreshToken'])
      # now we have a fresh token
      auth.send_email_verification(user['idToken'])
    except:
      pass

def signIn(email, password):
  try:
    auth.sign_in_with_email_and_password(email, password);
    #data = self.getUser()
    return True
  except:
      return False

# reset the password of the user...
def resetPassword(email):
  try:
    auth.send_password_reset_email(email)
    return True
  except:
    return False
