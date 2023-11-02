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
from onelogin.models.auth_claim import AuthClaim  # noqa: E501
from onelogin.rest import ApiException

class TestAuthClaim(unittest.TestCase):
    """AuthClaim unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AuthClaim
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AuthClaim`
        """
        model = onelogin.models.auth_claim.AuthClaim()  # noqa: E501
        if include_optional :
            return AuthClaim(
                name = 'email_address', 
                user_attribute_mappings = 'email', 
                user_attribute_macros = ''
            )
        else :
            return AuthClaim(
                name = 'email_address',
        )
        """

    def testAuthClaim(self):
        """Test AuthClaim"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
