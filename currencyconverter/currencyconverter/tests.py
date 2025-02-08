from django.test import TestCase
import json


class ConvertionTest(TestCase):

    def test_convertion_unary(self):
        payload = {
            "from": "USD",
            "to": "USD",
            "value": "1.0",
        }
        response = self.client.post(
            "/convert/", data=json.dumps(payload), content_type="application/json"
        )
        response_data = response.json()
        value = response_data.get("value", "None")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(value, 1.0, f"'{value}' should be '1.0'")

    def test_convertion(self):
        payload = {
            "from": "EUR",
            "to": "USD",
            "value": "1.0",
        }
        response = self.client.post(
            "/convert/", data=json.dumps(payload), content_type="application/json"
        )
        response_data = response.json()
        value = response_data.get("value", "None")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(value, 0.9, f"'{value}' should be '0.9'")
        
    def test_convertion_negative(self):
        payload = {
            "from": "USD",
            "to": "USD",
            "value": "-1.0",
        }
        response = self.client.post(
            "/convert/", data=json.dumps(payload), content_type="application/json"
        )
        response_data = response.json()
        error = response_data.get("error", "None")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(error, "Cannot convert negative value: '-1.0'")


    def test_convertion_zero(self):
        payload = {
            "from": "USD",
            "to": "EUR",
            "value": "0",
        }
        response = self.client.post(
            "/convert/", data=json.dumps(payload), content_type="application/json"
        )
        response_data = response.json()
        value = response_data.get("value", "None")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(value, 0.0, f"'{value}' should be '0.0'")
        

    def test_nonsupported_currency(self):
        payload = {
            "from": "USD",
            "to": "XYZ",
            "value": "1.0",
        }
        response = self.client.post(
            "/convert/", data=json.dumps(payload), content_type="application/json"
        )
        response_data = response.json()
        error = response_data.get("error", "None")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(error, "Currency 'XYZ' is not supported")