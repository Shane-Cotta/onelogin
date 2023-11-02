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
from onelogin.models.get_rate_limit200_response import GetRateLimit200Response  # noqa: E501
from onelogin.rest import ApiException

class TestGetRateLimit200Response(unittest.TestCase):
    """GetRateLimit200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetRateLimit200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetRateLimit200Response`
        """
        model = onelogin.models.get_rate_limit200_response.GetRateLimit200Response()  # noqa: E501
        if include_optional :
            return GetRateLimit200Response(
                status = onelogin.models.error.Error(
                    error = False, 
                    code = 200, 
                    type = 'Success', 
                    message = 'Success', ), 
                data = onelogin.models.rate_limit.rate_limit(
                    x_rate_limit_limit = 5000, 
                    x_rate_limit_remaining = 4988, 
                    x_rate_limit_reset = 832, )
            )
        else :
            return GetRateLimit200Response(
        )
        """

    def testGetRateLimit200Response(self):
        """Test GetRateLimit200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()