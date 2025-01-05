# Pytest API Testing Example
This repository contains a simple API testing example using the pytest framework to validate the login functionality of the ReqRes (a dummy API available for testing purposes) endpoint.


The Python script provided defines a function `test_login_valid()` intended for use with the pytest framework to test an API login functionality. The function sends a POST request to the "https://reqres.in/api/login/" endpoint with a predefined set of credentials (email and password). It then checks that the HTTP response status is 200, indicating success, and verifies that the returned JSON contains a specific token. This approach helps ensure that the API's authentication mechanism is functioning correctly and that it returns the expected token when given valid credentials. This kind of testing is essential for verifying the security and reliability of web applications.
