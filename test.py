try:
    from run import app
    import unittest

except Exception as e:
    print("Some Modules are Missing{} ".format(e))


class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        tester = app.test_client(self)
        self.valid_response = tester.get("/fib?n=10")
        self.invalid_response = tester.get("/fib?n=-1")
        self.str_response = tester.get("/fib?n=a")

    def test_200_when_request_parameter_is_valid(self):
        statuscode = self.valid_response.status_code
        self.assertEqual(statuscode, 200)

    def test_400_when_request_parameter_is_invalid(self):
        statuscode = self.invalid_response.status_code
        self.assertEqual(statuscode, 400)

    def test_400_when_request_parameter_is_str(self):
        statuscode = self.str_response.status_code
        self.assertEqual(statuscode, 400)

    def test_valid_content_is_json(self):
        self.assertEqual(self.valid_response.content_type, "application/json")

    def test_should_return_correct_result(self):
        self.assertTrue(b'result' in self.valid_response.data)
        self.assertTrue(b'55' in self.valid_response.data)

    def test_invalid_content_is_json(self):
        self.assertEqual(self.invalid_response.content_type,
                         "application/json")

    def test_should_return_invalid_status(self):
        self.assertTrue(b'status' in self.invalid_response.data)
        self.assertTrue(b'message' in self.invalid_response.data)

    def test_str_content_is_json(self):
        self.assertEqual(self.str_response.content_type, "application/json")

    def test_should_return_str_status(self):
        self.assertTrue(b'status' in self.str_response.data)
        self.assertTrue(b'message' in self.str_response.data)


if __name__ == "__main__":
    unittest.main()
