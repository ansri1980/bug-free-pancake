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
        self.assertIn('Hello World', res.data)
    
if __name__ == "__main__":
    unittest.main()
