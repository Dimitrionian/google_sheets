from googleapiclient.http import MediaFileUpload


class GoogleDriveAbstraction:

    def file_upload(self, drive_service, FOLDER_ID):
        file_metadata = {
            'name': 'photo.png',
            'parents': [FOLDER_ID]
        }
        media = MediaFileUpload('files/photo.png',
                                mimetype='image/png',
                                resumable=True)
        return drive_service.files().create(body=file_metadata,
                                            media_body=media,
                                            fields='id').execute()

    def create_folder(self, drive_service):
        file_metadata = {
            'name': 'Invoices test',
            'mimeType': 'application/vnd.google-apps.folder'
        }
        return drive_service.files().create(body=file_metadata,
                                            fields='id').execute()


