import pytest
import requests
from .page_objects.helper import load_json
from .page_objects.authentication_page import Authentication
from .page_objects.document_page import Document
from .page_objects.documents_http_methods import DocumentsHTTPMethods


@pytest.fixture(scope='class', autouse=True)
def before_all_after_all(driver, base_url):
    credentials = load_json('credentials.json')
    auth = Authentication(driver)
    auth.login(credentials['user_name'], credentials['password'])


class TestDocuments:
    """Class to test Documents."""

    def test_documents_license_upload(self, driver, session, base_url):
        """Verify Business License upload.

        Verify that a Business License can be uploaded properly and then it´s possible to
        download it, as satus code for download request is 200.

        Args:
            driver (:obj:`WebDriver`): The interface class.
            session (:obj:`Request`): A logged session for requests.
            base_url (str): The base API url.

        """
        data = load_json('documents.json')
        document = Document(driver)
        docs_http = DocumentsHTTPMethods(session, base_url)

        document.go_to_documents_section()
        document.upload_file(data['file_name'])
        document.verify_uploaded_file(data['file_name'])

        docs_http.get_documents()
        assert docs_http.status_code == requests.codes['ok']

        uploaded_file_name = docs_http.get_uploaded_file_name(data['file_name'])
        docs_http.verify_file_download(uploaded_file_name)
        assert docs_http.status_code == requests.codes['ok']

        docs_http.remove_file(uploaded_file_name)
        assert docs_http.status_code == requests.codes['no_content']