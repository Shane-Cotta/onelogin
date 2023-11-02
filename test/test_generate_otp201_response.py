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
from onelogin.models.generate_otp201_response import GenerateOTP201Response  # noqa: E501
from onelogin.rest import ApiException

class TestGenerateOTP201Response(unittest.TestCase):
    """GenerateOTP201Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GenerateOTP201Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GenerateOTP201Response`
        """
        model = onelogin.models.generate_otp201_response.GenerateOTP201Response()  # noqa: E501
        if include_optional :
            return GenerateOTP201Response(
                mfa_token = 'UIOWE787979', 
                reusable = True, 
                expires_at = '2020-06-26T21:52:56Z', 
                device_id = 'user_temp_otp_36216766'
            )
        else :
            return GenerateOTP201Response(
        )
        """

    def testGenerateOTP201Response(self):
        """Test GenerateOTP201Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
