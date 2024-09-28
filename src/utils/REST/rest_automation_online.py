import requests


class RestAutomationOnline:
    def __init__(self):
        self.base_url = 'https://automationintesting.online/message/'

    @property
    def get_headers(self) -> dict:
        headers_dict = {'content-type': 'application/json'}
        return headers_dict

    def rest_submit_message(self):
        """
        REST POST function that submits a message
        Can create variables to customize the message body, but for the purposes of this demo,
        we'll just keep it hard-coded
        """
        url = self.base_url
        headers = self.get_headers
        message_body = {'name': 'Test User', 'email': 'testing@email.com', 'phone': '15252225555',
                        'subject': 'Test Subject',
                        'description': 'This is a sample message'}
        response = requests.post(url=url, headers=headers, json=message_body)
        assert response.ok
        return response.json()

    def rest_get_message(self):
        """
        REST GET function that retrieves all messages
        """
        url = self.base_url
        headers = self.get_headers
        response = requests.get(url=url, headers=headers)
        assert response.ok
        return response.json()

    def rest_get_message_count(self):
        """
        REST GET function that retrieves a count of all messages
        """
        url = self.base_url + 'count'
        headers = self.get_headers
        response = requests.get(url=url, headers=headers)
        assert response.ok
        return response.json()
