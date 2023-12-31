# coding: utf-8

"""
    OneLogin API

    OpenAPI Specification for OneLogin  # noqa: E501

    The version of the OpenAPI document: 3.1.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import onelogin
from onelogin.models.get_assigned_user200_response import GetAssignedUser200Response  # noqa: E501
from onelogin.rest import ApiException

class TestGetAssignedUser200Response(unittest.TestCase):
    """GetAssignedUser200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetAssignedUser200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetAssignedUser200Response`
        """
        model = onelogin.models.get_assigned_user200_response.GetAssignedUser200Response()  # noqa: E501
        if include_optional :
            return GetAssignedUser200Response(
                total = 56, 
                users = [
                    56
                    ], 
                before_cursor = 'none', 
                previous_link = 'none', 
                after_cursor = 'none', 
                next_link = 'none'
            )
        else :
            return GetAssignedUser200Response(
        )
        """

    def testGetAssignedUser200Response(self):
        """Test GetAssignedUser200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
