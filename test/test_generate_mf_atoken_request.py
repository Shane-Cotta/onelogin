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
from onelogin.models.generate_mf_atoken_request import GenerateMFAtokenRequest  # noqa: E501
from onelogin.rest import ApiException

class TestGenerateMFAtokenRequest(unittest.TestCase):
    """GenerateMFAtokenRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GenerateMFAtokenRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GenerateMFAtokenRequest`
        """
        model = onelogin.models.generate_mf_atoken_request.GenerateMFAtokenRequest()  # noqa: E501
        if include_optional :
            return GenerateMFAtokenRequest(
                expires_in = 300, 
                reusable = False
            )
        else :
            return GenerateMFAtokenRequest(
        )
        """

    def testGenerateMFAtokenRequest(self):
        """Test GenerateMFAtokenRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()