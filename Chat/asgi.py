"""
ASGI config for Chat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Chat.settings')

application = get_asgi_application()



"""





{
  "type": "service_account",
  "project_id": "chat-3bdc8",
  "private_key_id": "b4abcf2c71f7b8ac4753679811126a95a477808c",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC3SKdi96XSEnB9\ne9hcbVD9QZR6a84YV/HvCdG5os9Hl5i/H4pw+Kwc5PSTDM/QlvW8Dro1GLmlg5xr\nzbsx+/UcM1TkDk6o1VFzGzIEw7jecgDM/P1t9Dv2u8fU7QeXuChkpadpKKPlyCYX\nygjYCcvLwDv38KhwhRhsdvZmen357Fv9mEv6O2BLgMH5ZgHE1or2YEdYkOXGQQlv\nJKelW1gnHjOPEkWqeCBJ5FrTiXT9qfKK0Oys1X3psjOxgXK/tl2YDN+88fy2h4Bn\nzI1dST7bUrSIZyQjYxlIzOClNT2u1l5jKTo0elirMsNblfmWMORgj/Y3uG8VrSrV\nceEHeuAlAgMBAAECggEAGUFPI1F5jWlSC9BxX0cG5mbPdVD+jJcttKD3P6uiATzv\n5MINWwTA/phD5TFaP2VVxgyHdwKJrjdk6evm0/viafjexS/9gcEnIIPKUCLCChDO\ncHCZ4TlKu/RjFEF3Dt5m3nt/Bnv9nY+HRDboIhCzfsdl3APSyfJlC6kWyccuLa46\nn2Y2LsK/E6pYq9WBO3a/078h+aNjjMFOlfXyCvKJMjkJiplgIGr3c7R5nKFCfdyU\nMDtujVZ0Z2Zu8XwdVgdxzZSFoDRhL9jFQt/wIblB/9NwZmaqFewjd+V1maRK6ChP\n/kKGO7FQ8Q2O9nsFoQnrRB21KXw872QB5r3S29YNfwKBgQDpiE7F2tAcByVlpyQA\nYak1D4Z0SGjAr6Qyop3Wp5ti7ClWrvZCd42W94H2duFHnq1UDNAMzOlIV8K/Zghi\nopNmiAfDfvqyYwyHsrREA6/+YUgDZiJz/3HszwEfumtDpasqKAKFhdoL66gBBHh9\nqrWeIFM2IT/cAwCUZ2EGdaKu4wKBgQDI6sR/MTzr8z18b1aZQCOW8n0wmuXKSM64\n+Aa9AjZks/R1W4MjMiXqcEBdcSRsuemGamWour5c8zepeosyYgeDsrr81v2HsaQE\nU3xbKZDBVPa+ELRlK7Bi+Xqigrmh6pMcWHLgyTrPDiNNIgFCmQPHAhzSevulPZhh\nkT1i4NqbVwKBgQCIy0yBPzRKRrFUQzymcI6CQ07aDJQ30mrXMkRMua8emgF5AlHE\nC23H8cGSEn7RyhPzuPGhneJEewvbu7PLuzmmhKYvkNDe74AmeLp5YMOVuXxKaWhj\nFE2yjms1H6i3XnLN5dPcTNS1yNuHhQvjaLysHHlBquZSRPvw8kF2XC/oSwKBgGCM\nWHKasaDc2W4jfqTUKoYN7tTdipEjXZuLLInFN2g7Bb0jhafzID9BQ9zjUtKgoDSE\nimeDnZjDE7twdNV4QA4sZCi+E0USuzOM/tQ77CDLeGqrUlTPospdAm53jUbel2Tm\nqAWXDZiUPaiCL8LWDveh70HB8Y1dRQ2Vor8SOFqvAoGBAMPwjVv3Kh1ljNM7GQzJ\nYeOOupbF/QowDGoSdzjkoInvDIrdw0Dvu5G1oRMDRux2/iuvyMfQ3jH3Eo4OAtWW\nIajGnwtODQZE31fHPgfN6RZgkHAmrPqGpTEy1pUi8lytr4/WVrIdCQkaDt+3IaRl\nqgGwiXdgUXUdhpmQnHNb1k0N\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-pv61d@chat-3bdc8.iam.gserviceaccount.com",
  "client_id": "104143831304668617192",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-pv61d%40chat-3bdc8.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
"""