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
from onelogin.models.generate_mf_atoken200_response import GenerateMFAtoken200Response  # noqa: E501
from onelogin.rest import ApiException

class TestGenerateMFAtoken200Response(unittest.TestCase):
    """GenerateMFAtoken200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GenerateMFAtoken200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GenerateMFAtoken200Response`
        """
        model = onelogin.models.generate_mf_atoken200_response.GenerateMFAtoken200Response()  # noqa: E501
        if include_optional :
            return GenerateMFAtoken200Response(
                mfa_token = '55647655', 
                resuable = True, 
                expires_at = '2019-01-16T22:16:38.000Z'
            )
        else :
            return GenerateMFAtoken200Response(
        )
        """

    def testGenerateMFAtoken200Response(self):
        """Test GenerateMFAtoken200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
