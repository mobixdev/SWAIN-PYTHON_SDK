# coding: utf-8

"""
    SWAIN API

    A powerful dynamic CRUD API engine that automatically generates RESTful endpoints for your data models SWAIN provides automatic CRUD operations, filtering, pagination, and sorting capabilities for any data model. Features: - Automatic REST API generation - Dynamic model support - Complex filtering and querying - Pagination and sorting - Swagger/OpenAPI documentation - Multiple database support (SQL & NoSQL)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.auth_login_request import AuthLoginRequest

class TestAuthLoginRequest(unittest.TestCase):
    """AuthLoginRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AuthLoginRequest:
        """Test AuthLoginRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AuthLoginRequest`
        """
        model = AuthLoginRequest()
        if include_optional:
            return AuthLoginRequest(
                password = '',
                username = ''
            )
        else:
            return AuthLoginRequest(
        )
        """

    def testAuthLoginRequest(self):
        """Test AuthLoginRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
