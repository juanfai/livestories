import requests


class DocumentsHTTPMethods:
    """Class that defines the `Documents HTTP Methods`.

    Args:
        session (:obj:`Request`): The user session.
        base_url (str): The environment url.

    """

    def __init__(self, session, base_url):
        self._session = session
        self._base_url = f'{base_url}/api'
        self._res = None
        self._business_license = None


    @property
    def res(self):
        """dict: The `json` response from the last `HTTP` request."""
        return self._res

    @property
    def status_code(self):
        """int: Get the last `HTTP status code` response received."""
        return self._status_code

    @property
    def business_license(self):
        """str: Get the Business License´s `ds_s3_url` value from the response"""
        return self._business_license

    def get_documents(self):
        filters = r'{%22where%22:{%22cd_business%22:33740,%20%22ic_active%22:%20true%20}}'
        url = f'{self._base_url}/business-documents?filter={filters}'

        r = self._session.get(url)
        self._status_code = r.status_code
        self._res = r.json()

    def get_uploaded_file_name(self, file_name):
        for doc in self._res:
            if file_name in doc['ds_s3_url']:
                return doc['ds_s3_url']

    def verify_file_download(self, file_name):
        url = f'{self._base_url}/download-file'
        payload = {
            's3_url': file_name
        }
        r = self._session.post(url, json=payload)
        self._status_code = r.status_code
        self._res = r.text

    def remove_file(self, file_name):
        url = f'{self._base_url}/remove-file'
        payload = {
            's3_url': file_name
        }
        r = self._session.post(url, json=payload)
        self._status_code = r.status_code