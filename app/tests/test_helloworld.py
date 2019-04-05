import boiler_plate_rest_api
import unittest

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
    
if __name__ == "__main__":
    unittest.main()
