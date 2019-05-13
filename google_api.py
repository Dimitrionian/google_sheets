from pprint import pprint
from apiclient import discovery
from google_drive import GoogleDriveAbstraction
from google_sheets import GoogleSheetsAbstraction
from google_docs import GoogleDocsAbstraction
from hepers import GoogleAPIHelper

# Instantiate apis
sheets = GoogleSheetsAbstraction()
drive = GoogleDriveAbstraction()
docs = GoogleDocsAbstraction()

# Auth
credentials = sheets.auth()

# Spreadsheet creation
# spreadsheet = sheets.get_spreadsheet(credentials)
# pprint(spreadsheet['spreadsheetId'])
# pprint(spreadsheet['spreadsheetUrl'])

# Assign credentials via Google drive API
drive_service = discovery.build('drive', 'v3', credentials=credentials)
document_service = discovery.build('docs', 'v1', credentials=credentials)
document = docs.create_doc(document_service)
GoogleAPIHelper.set_permissions(document['documentId'], drive_service)
pprint(document)







