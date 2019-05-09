import os
from apiclient import discovery
from google.oauth2 import service_account
from pprint import pprint

SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive.file']

SPREADSHEET_ID = '1UALwb0Pj-g11W0xsk0oq82xPJlqdPEN61_FgR0GjOnk'
RANGE_NAME = 'A1:D2'

secret_file = os.path.join(os.getcwd(), 'client_secret.json')
credentials = service_account.Credentials.from_service_account_file(secret_file, scopes=SCOPES)
service = discovery.build('sheets', 'v4', credentials=credentials)

spreadsheet_body = {}

request = service.spreadsheets().create(body=spreadsheet_body)
spreadsheet = request.execute()

# TODO: Change code below to process the `response` dict:
pprint(spreadsheet)

driveService = discovery.build('drive', 'v3', credentials=credentials)
shareRes = driveService.permissions().create(
    fileId=spreadsheet['spreadsheetId'],
    body={'type': 'user', 'role': 'writer', 'emailAddress': 'dimitrionian123@gmail.com'},
    fields='id'
).execute()

# values = [
#     ['a1', 'b1', 'c1', 123],
#     ['a2', 'b2', 'c2', 456]
# ]
#
# data = {
#     'values': values
# }
#
# service.spreadsheets().values().update(
#     spreadsheetId=SPREADSHEET_ID,
#     body=data,
#     range=RANGE_NAME,
#     valueInputOption='USER_ENTERED'
# ).execute()
