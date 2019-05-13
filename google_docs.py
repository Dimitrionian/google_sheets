

class GoogleDocsAbstraction:
    def create_doc(self, service):
        title = 'My Document'
        body = {
            'title': title
        }
        return service.documents() \
            .create(body=body).execute()

