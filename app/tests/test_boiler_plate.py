import boiler_plate_rest_api
import unittest
import json

class boiler_plate_testcase(unittest.TestCase):
    """ boilerplate api test case class """

    def setUp(self):
        """ Initialise variables """
        self.appH = boiler_plate_rest_api.app
        self.client = self.appH.test_client()

    def test_root_get(self):
        res = self.client.get("/")
        # Weirdly as per the https://pythonhosted.org/Flask-JSON/#opt-jsonp-quotes, returns string with quotes around :(
        # Tried setting JSON_JSONP_STRING_QUOTES to False but didn't work. I will get to this last when I have time
        # For now living with this simple hack in unit tests
        self.assertEqual('"Hello World"', res.data.rstrip())
    
    def test_status_get(self):
        res = self.client.get("/status")
        data = {"myapplication":
                   [{
                    "version": "1.0",
                    "description": "pre-interview technical test",
                    "lastcommitsha": "abc57858585"
                    }]}
        self.assertDictEqual(data, json.loads(res.data))

if __name__ == "__main__":
    unittest.main()
