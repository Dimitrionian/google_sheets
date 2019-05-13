from google.oauth2 import service_account
from vars import secret_file, SCOPES
from apiclient import discovery


class GoogleSheetsAbstraction:
    def auth(self):
        return service_account.Credentials.from_service_account_file(secret_file, scopes=SCOPES)

    def get_spreadsheet(self, credentials):
        service = discovery.build('sheets', 'v4', credentials=credentials)
        spreadsheet_body = {
            'properties': {'title': 'Смета на памятник', 'locale': 'ru_RU'}
        }
        request = service.spreadsheets().create(body=spreadsheet_body)
        return request.execute()
