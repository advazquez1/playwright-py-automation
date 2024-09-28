import pytest


@pytest.mark.sanity
class TestMessageAPI:

    @pytest.mark.parametrize('expected_response', [
        {'name': 'Test User', 'email': 'testing@email.com', 'phone': '15252225555',
         'subject': 'Test Subject', 'description': 'This is a sample message'}
    ])
    def test_post_message_happy_path(self, expected_response, submit_message_api) -> None:
        response = submit_message_api
        # Validating that expected keys are coming in response
        assert 'messageid' in response
        assert 'name' in response
        assert 'email' in response
        assert 'phone' in response
        assert 'subject' in response
        assert 'description' in response

        # Validating expected values
        assert response['name'] == expected_response['name']
        assert response['email'] == expected_response['email']
        assert response['phone'] == expected_response['phone']
        assert response['subject'] == expected_response['subject']
        assert response['description'] == expected_response['description']

    @pytest.mark.parametrize('expected_response', [
        {'name': 'Test User', 'subject': 'Test Subject', 'read': False}
    ])
    def test_get_message_happy_path(self, expected_response, get_message_api) -> None:
        response = get_message_api
        # Validating that there are messages being returned
        assert 'messages' in response
        assert len(response['messages']) > 0

        # Looking for particular message given in parameter
        for message in response['messages']:
            if (message['name'] == expected_response['name'] and
                    message['subject'] == expected_response['subject'] and
                    message['read'] == expected_response['read']):
                assert True
                return

        # Couldn't find a match
        assert False

    def test_get_message_count_happy_path(self, get_message_count_api) -> None:
        response = get_message_count_api
        # Validating that there are should be at least 1 message
        # There could be more, but due to this website cleaning the DB every 10 min, we'll just look for 1
        assert response['count'] >= 1
