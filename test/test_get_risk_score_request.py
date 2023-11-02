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
from onelogin.models.get_risk_score_request import GetRiskScoreRequest  # noqa: E501
from onelogin.rest import ApiException

class TestGetRiskScoreRequest(unittest.TestCase):
    """GetRiskScoreRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetRiskScoreRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetRiskScoreRequest`
        """
        model = onelogin.models.get_risk_score_request.GetRiskScoreRequest()  # noqa: E501
        if include_optional :
            return GetRiskScoreRequest(
                ip = '', 
                user_agent = '', 
                user = onelogin.models.risk_user.risk_user(
                    id = '', 
                    name = '', 
                    authenticated = True, ), 
                source = onelogin.models.source.source(
                    id = '', 
                    name = '', ), 
                session = onelogin.models.session.session(
                    id = '', ), 
                device = onelogin.models.risk_device.risk_device(
                    id = '', ), 
                fp = ''
            )
        else :
            return GetRiskScoreRequest(
                ip = '',
                user_agent = '',
                user = onelogin.models.risk_user.risk_user(
                    id = '', 
                    name = '', 
                    authenticated = True, ),
        )
        """

    def testGetRiskScoreRequest(self):
        """Test GetRiskScoreRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
