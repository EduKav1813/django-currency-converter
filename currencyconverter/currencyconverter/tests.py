from django.test import TestCase
import json


class ConvertionTest(TestCase):

    def test_unary_convertion(self):
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
        self.assertEqual(value, "1.0", f"'{value}' should be '1.0'")
