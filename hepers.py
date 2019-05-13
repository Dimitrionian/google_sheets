

class GoogleAPIHelper:
    @staticmethod
    def set_permissions(file_id, drive_service):
        drive_service.permissions().create(
            fileId=file_id,
            body={'type': 'user', 'role': 'writer', 'emailAddress': 'dimitrionian123@gmail.com'},
            fields='id'
        ).execute()
