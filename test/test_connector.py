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
from onelogin.models.connector import Connector  # noqa: E501
from onelogin.rest import ApiException

class TestConnector(unittest.TestCase):
    """Connector unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Connector
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Connector`
        """
        model = onelogin.models.connector.Connector()  # noqa: E501
        if include_optional :
            return Connector(
                id = 1061937, 
                name = 'Amazon Web Services Multi-Role', 
                icon_url = 'https://cdn-shadow.onlgn.net/images/icons/square/amazonwebservices3multirole/old_original.png?1421095823', 
                auth_method = 8, 
                allows_new_parameters = True
            )
        else :
            return Connector(
        )
        """

    def testConnector(self):
        """Test Connector"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
