""" Test for flight """
import mock

from flightApi.tests.base import BaseTestCase


# pylint: disable=unused-argument
class TestFlight(BaseTestCase):
    """ Test for flight view function """
    @mock.patch('flightApi.views.flights.send_booking_email_task')
    def test_view_flight_book_single_ticket_successfully_valid_cred(self, mail_patched_func):
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

    @mock.patch('flightApi.views.flights.send_booking_email_task')
    def test_view_flight_book_round_ticket_successfully_valid_cred(self, mail_patched_func):
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

    def test_view_admin_retrieve_passengers_for_a_specific_flight(self):
        """
        Test the api for admin to get passengers for a specific flight
        """
        self.test_client().login(username='adminuser@mail.com', password='password')
        response = self.test_client().get(
            "/api/v1/admin/flights/?name=FT 807&date=2019-05-28 14:45:00")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['status'], 'success')
        self.assertEqual(len(response.data['passengers']), 1)

    def test_user_cannot_retrieve_passengers_for_a_specific_flight(self):
        """
         Test that an ordinary user can't query this admin api
        """
        response = self.test_client(token=self.token).get(
            "/api/v1/admin/flights/?name=FT 807&date=2019-05-28 14:45:00")
        self.assertEqual(response.status_code, 403)
        expected_message = 'You do not have permission to perform this action.'
        self.assertEqual(response.data['detail'], expected_message)
