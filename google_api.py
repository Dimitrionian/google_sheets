from pprint import pprint
from apiclient import discovery
from google_drive import GoogleDriveAbstraction
from google_sheets import GoogleSheetsAbstraction

# Instantiate apis
sheets = GoogleSheetsAbstraction()
drive = GoogleDriveAbstraction()

# Auth
credentials = sheets.auth()

# Spreadsheet creation
# spreadsheet = sheets.get_spreadsheet(credentials)
# pprint(spreadsheet['spreadsheetId'])
# pprint(spreadsheet['spreadsheetUrl'])

# Assign credentials via Google drive API
drive_service = discovery.build('drive', 'v3', credentials=credentials)




