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
from onelogin.models.create_app_request import CreateAppRequest  # noqa: E501
from onelogin.rest import ApiException

class TestCreateAppRequest(unittest.TestCase):
    """CreateAppRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateAppRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateAppRequest`
        """
        model = onelogin.models.create_app_request.CreateAppRequest()  # noqa: E501
        if include_optional :
            return CreateAppRequest(
                id = 775664, 
                name = 'A Sample App', 
                visible = True, 
                description = '', 
                notes = 'This app is in beta.', 
                icon_url = '/images/missing_connector_icon/square/old_original.png', 
                auth_method = 8, 
                policy_id = 56, 
                allow_assumed_signin = False, 
                tab_id = 196885, 
                connector_id = 108419, 
                created_at = '2018-04-12T21:50:42Z', 
                updated_at = '2019-05-16T19:20:34Z', 
                role_ids = [192513], 
                provisioning = onelogin.models.generic_app_provisioning.generic_app_provisioning(
                    enabled = True, ), 
                sso = None, 
                configuration = None, 
                parameters = {
                    'key' : onelogin.models.app_parameters_value.app_parameters_value(
                        user_attribute_mappings = '', 
                        user_attribute_macros = '', 
                        label = '', 
                        include_in_saml_assertion = True, )
                    }, 
                enforcement_point = onelogin.models.enforcement_point.enforcement_point(
                    require_sitewide_authentication = False, 
                    conditions = '', 
                    session_expiry_fixed = {"value":30,"unit":1}, 
                    session_expiry_inactivity = {"value":30,"unit":1}, 
                    permissions = 'allow', 
                    token = 'b491c647f5e0cff854ad606722ac98342b4b0882', 
                    target = '', 
                    resources = [{"resource_id":809,"conditions":"","is_path_regex":false,"permissions":"allow","require_auth":false,"path":"/"}], 
                    context_root = '/', 
                    use_target_host_header = False, 
                    vhost = '', 
                    landing_page = '', 
                    case_sensitive = False, )
            )
        else :
            return CreateAppRequest(
                name = 'A Sample App',
                visible = True,
                description = '',
                policy_id = 56,
                connector_id = 108419,
                configuration = None,
                parameters = {
                    'key' : onelogin.models.app_parameters_value.app_parameters_value(
                        user_attribute_mappings = '', 
                        user_attribute_macros = '', 
                        label = '', 
                        include_in_saml_assertion = True, )
                    },
        )
        """

    def testCreateAppRequest(self):
        """Test CreateAppRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()