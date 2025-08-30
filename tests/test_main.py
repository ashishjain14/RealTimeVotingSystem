import unittest
from unittest.mock import MagicMock, patch
import psycopg2
import simplejson as json
from src.main import (
    generate_voter_data,
    generate_candidate_data,
    insert_voters,
    create_tables,
    delivery_report
)

class TestMain(unittest.TestCase):
    # Test that generate_voter_data returns correct voter info when API call is successful
    @patch('src.main.requests.get')
    def test_generate_voter_data_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'results': [{
                'login': {'uuid': '123', 'username': 'user1'},
                'name': {'first': 'John', 'last': 'Doe'},
                'dob': {'date': '2000-01-01'},
                'gender': 'male',
                'nat': 'GB',
                'location': {
                    'street': {'number': 1, 'name': 'Main St'},
                    'city': 'London', 'state': 'London', 'country': 'UK', 'postcode': '12345'
                },
                'email': 'john@example.com',
                'phone': '123456789',
                'cell': '987654321',
                'picture': {'large': 'url'},
                'registered': {'age': 22}
            }]
        }
        voter = generate_voter_data()
        self.assertEqual(voter['voter_id'], '123')
        self.assertEqual(voter['voter_name'], 'John Doe')

    # Test that generate_voter_data returns error string when API call fails
    @patch('src.main.requests.get')
    def test_generate_voter_data_failure(self, mock_get):
        mock_get.return_value.status_code = 404
        voter = generate_voter_data()
        self.assertEqual(voter, 'Error fetching data')

    # Test that generate_candidate_data returns correct candidate info when API call is successful
    @patch('src.main.requests.get')
    def test_generate_candidate_data_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'results': [{
                'login': {'uuid': '456'},
                'name': {'first': 'Jane', 'last': 'Smith'},
                'picture': {'large': 'url'}
            }]
        }
        candidate = generate_candidate_data(1, 3)
        self.assertEqual(candidate['candidate_id'], '456')
        self.assertEqual(candidate['candidate_name'], 'Jane Smith')

    # Test that generate_candidate_data returns error string when API call fails
    @patch('src.main.requests.get')
    def test_generate_candidate_data_failure(self, mock_get):
        mock_get.return_value.status_code = 404
        candidate = generate_candidate_data(1, 3)
        self.assertEqual(candidate, 'Error fetching data')

    # Test that delivery_report prints success message when no error is present
    def test_delivery_report_success(self):
        msg = MagicMock()
        msg.topic.return_value = 'topic'
        msg.partition.return_value = 0
        with patch('builtins.print') as mock_print:
            delivery_report(None, msg)
            mock_print.assert_called_with('Message delivered to topic [0]')

    # Test that delivery_report prints error message when error is present
    def test_delivery_report_failure(self):
        with patch('builtins.print') as mock_print:
            delivery_report('error', None)
            mock_print.assert_called_with('Message delivery failed: error')

    # Test that create_tables and insert_voters call commit on the connection
    def test_create_tables_and_insert_voters(self):
        conn = MagicMock()
        cur = MagicMock()
        create_tables(conn, cur)
        voter = {
            "voter_id": "1",
            "voter_name": "Test User",
            "date_of_birth": "2000-01-01",
            "gender": "male",
            "nationality": "GB",
            "registration_number": "reg1",
            "address": {
                "street": "1 Main St",
                "city": "London",
                "state": "London",
                "country": "UK",
                "postcode": "12345"
            },
            "email": "test@example.com",
            "phone_number": "123456789",
            "cell_number": "987654321",
            "picture": "url",
            "registered_age": 22
        }
        insert_voters(conn, cur, voter)
        self.assertTrue(conn.commit.called)

if __name__ == '__main__':
    unittest.main()
