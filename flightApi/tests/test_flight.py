""" Test for flight """
from flightApi.tests.base import BaseTestCase


class TestFlight(BaseTestCase):
    """ Test for flight view function """
    def test_view_flight_book_single_ticket_successfully_valid_cred(self):
        """
        Test the api for booking single flight with valid credentials
        """
        body = {
            'departure_date': '2019-05-28',
            'departure_airport': 'LOS',
            'no_of_passenger': 2,
            'flight_class': 'Economy',
            'arriving_airport': 'KGL',
            'passenger': 2
        }
        response = self.test_client(token=self.token).post("/api/v1/flights/?type=single", body)
        user = f'{self.test_user.first_name} {self.test_user.last_name}'
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['message'], "flight successfully booked")
        self.assertEqual(response.data['booked by'], user)

    def test_view_flight_book_round_ticket_successfully_valid_cred(self):
        """
        Test the api for booking round flight with valid credentials
        """
        body = {
            'departure_date': '2019-05-28',
            'departure_airport': 'LOS',
            'no_of_passenger': 2,
            'flight_class': 'Economy',
            'arriving_airport': 'KGL',
            'return_date': '2019-09-05',
            'passenger': 2
        }
        response = self.test_client(token=self.token).post("/api/v1/flights/?type=round", body)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['message'], "flight successfully booked")
        self.assertIn('return_date', response.data['flightDetails'])

    def test_view_flight_book_ticket_fail_with_missing_field(self):
        """
        Test the api for booking flight fails with missing fields
        """
        body = {
            'departure_airport': 'LOS',
            'no_of_passenger': 2,
            'flight_class': 'Economy',
            'arriving_airport': 'KGL',
            'return_date': '2019-09-05',
        }
        response = self.test_client(token=self.token).post("/api/v1/flights/?type=round", body)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['error'], 'missing field(s)')
