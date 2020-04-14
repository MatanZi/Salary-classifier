# A function that sends the email of the result to hadas.c@velismedia.com.

from __future__ import print_function

import httplib2
from apiclient import discovery
from oauth2client import tools

# set up
try:
    import argparse

    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

import google_api_auth


# provide labels
def get_labels():
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])


# static params
SCOPES = 'https://mail.google.com/'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Gmail API Python Quickstart'
authInst = google_api_auth.auth(SCOPES, CLIENT_SECRET_FILE, APPLICATION_NAME)
credentials = authInst.get_credentials()

http = credentials.authorize(httplib2.Http())
service = discovery.build('gmail', 'v1', http=http)

import gmail_send_email


# Send mail with header and body using Gmail API
def sendemail(message):
    sendInst = gmail_send_email.send_email(service)

    from_addr = 'matanzilka@gmail.com'
    subject = 'Finished The Program'
    login = 'hopetoworkforyou'
    password = 'velismedia'
    to = "hadas.c@velismedia.com"

    message = sendInst.create_message(from_addr, to, subject,
                                      message)
    sendInst.send_message('me', message)
