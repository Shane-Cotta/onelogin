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
from onelogin.models.rule import Rule  # noqa: E501
from onelogin.rest import ApiException

class TestRule(unittest.TestCase):
    """Rule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Rule
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Rule`
        """
        model = onelogin.models.rule.Rule()  # noqa: E501
        if include_optional :
            return Rule(
                id = 196670, 
                name = 'My first app rule', 
                match = 'all', 
                enabled = True, 
                position = 1, 
                conditions = [
                    onelogin.models.condition.condition(
                        source = 'last_login', 
                        operator = '>', 
                        value = '90', )
                    ], 
                actions = [
                    onelogin.models.action_obj.action_obj(
                        action = '', 
                        value = [
                            '2'
                            ], )
                    ]
            )
        else :
            return Rule(
        )
        """

    def testRule(self):
        """Test Rule"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
