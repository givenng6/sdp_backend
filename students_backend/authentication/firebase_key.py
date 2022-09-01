from firebase_admin import credentials
import firebase_admin

cred = credentials.Certificate({
  "type": "service_account",
  "project_id": "wits-services-ea5cf",
  "private_key_id": "c39ec15d1c9e76b8f9a2fc2fb512ad8f3d4510ba",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCfygz41d22wJkF\n++/uSykhcLesYIpnWXILKHEUFji1JfarL2EU1Cq7ZE8LXqyEJdxNRSSgQzyeMD1f\nY/DsGH9YvFbNxXmaGQR2DEz1Hu6qFQdaaRzEndytRPl9g8ijrLVgxTVq511QIEaF\nrTUNxiXj6MA48SWRWChrcmyUyF3j0yubV2tnRNvvgWV+jTgjM5JE1QxDd7Dmiy81\nZ8WcezbOsctbroqxOUMYFcgSiTK7nJIIGo2chNoFqOVS8TvzQZ8xNlaRj2cbEvTW\n5HI0rPnosU8pELgvoVrf+SMjEcytENxEmSgmLB/83joc2YVoERy82pUngwXSz8T1\nfG9419gbAgMBAAECggEAGcmBU20sVVB6wZj5jSLrFd77fWGtJGWufnd93EiDyVRB\nnTnNuI9PACP9j6+tNrxnc77rXMPNFhhh5zGZUXjYoGjwt0+dws0zx5tPliVyTdeL\n8r7Q6jgxw3LEsslgSW3XbbEV4FVLXWGAEBW2YK0wMzo+P1JHhk/MYh66wD4fzOLn\npD3DIuk1WKv7m9N+Dmsz4/kLJj3jf5SeZy1qghIa9ivV2xS/RA7Uw5nA1o0DwoSv\ncYvnmka8aSFGy4gKbEat3/GKhMLBXqdVncNIehNj5+W2vahlFRPIrTUZGLG/gle3\nW3PDfyMx9gJ8fh/j0vLJqY9BqWKhDx60tY6vD7c9hQKBgQDUZ47QmbEYNQBIW2Nx\nsLFOifpzXqTEmuXoB+3kb+8p7PYrphpQKo1G6Z+7jrKmOM7OeHcqd3KwF+v478UT\nBPf7ODBKUEJu9gkJYVSl13wMythuEGVGwI4j/IFVjSJHoR6bn76bd1ybnhC+qDtG\nrxpZvVoI1P5+tVbcJsz+2DPPpwKBgQDAlelR95mj2p2rIE353CrzeawoYkmd2V9y\nugZGHqBuCEidcrxKe0sWFQJy/WvfJQlVFe3WSB+FK9F5k9b/QUIxpsQtC4YEM2Y0\nlDgisXNYGA80AykepIi+7kTI1aJA8d9bIb8dZ5JizkEI8/Ye/oNdE39CixOpvvJo\nltX1bbHibQKBgDPAh6uLxvp+73Kx0akBxDG+rKcviDXfB+VhCTV/kGZGtjQsZHzj\n4UhF5AVu31hgvwLPlzlhoTAGpBgjU4Eu1L0BE8MHiyg+CjWe4WEG/9KeGd23YPW8\nNOXPwDN4D8IkH7ELWwXGL2o7ORk7JDY0s9bpq+Y6/0cgJ+m8CnaNdxJBAoGAbQhy\nwGVeJtZuzaPMgdmUt6P7RCHha+zVjS6kvq44RhOKiRmcYM7NBAOBD3lKyVs+nV18\n+gR7U/oq7po07u8TeujfyGDtzxMKmloQLhQpKYb1lIz1itO8V9yuNMY+xmYp/n5s\npUkuJ6J+T4NPpNyTou6W7iWvTDs/ItfC6uDgBUECgYBvP91szUIR6Fo+u6oS6X13\nIgCMxAiwtbJ0gXK4ZMCblHhymQb8c3S3Q7IlbRCRb2sYSAXoZ/PknfDc66FikgjI\nZ7HBkaWGg9m++jv7JapNVtvdilZrQo2F4K30kQa6uLqbpPlLMAQnfdAiEH4AAbeZ\n3wM+x8qln6FjMXxDsLv2ZA==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-ueokb@wits-services-ea5cf.iam.gserviceaccount.com",
  "client_id": "113007003523896804736",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-ueokb%40wits-services-ea5cf.iam.gserviceaccount.com"
})

firebase_admin.initialize_app(cred)


