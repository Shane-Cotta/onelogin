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
from onelogin.models.configuration_saml_all_of import ConfigurationSamlAllOf  # noqa: E501
from onelogin.rest import ApiException

class TestConfigurationSamlAllOf(unittest.TestCase):
    """ConfigurationSamlAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ConfigurationSamlAllOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConfigurationSamlAllOf`
        """
        model = onelogin.models.configuration_saml_all_of.ConfigurationSamlAllOf()  # noqa: E501
        if include_optional :
            return ConfigurationSamlAllOf(
                signature_algorithm = 'SHA-512', 
                certificate_id = 123456
            )
        else :
            return ConfigurationSamlAllOf(
                signature_algorithm = 'SHA-512',
        )
        """

    def testConfigurationSamlAllOf(self):
        """Test ConfigurationSamlAllOf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
