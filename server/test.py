try:
    from app import app
    import unittest
    from database_config import User
except Exception as e:
    print("Modules are missing {} ".format(e))


class FlaskTest(unittest.TestCase):
    # test the response code of 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/users")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # test the response type of json
    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get("/users")
        self.assertEqual(response.content_type, "application/json")

if __name__ == "__main__":
    unittest.main()