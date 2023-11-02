# coding: utf-8

"""
    OneLogin API

    OpenAPI Specification for OneLogin  # noqa: E501

    The version of the OpenAPI document: 3.1.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import List
from pydantic import BaseModel, Field, StrictStr, validator

class PrivilegePrivilegeStatementInner(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    effect: StrictStr = Field(..., alias="Effect", description="Set to “Allow.” By default, all actions are denied, this Statement allows the listed actions to be executed.")
    action: List[StrictStr] = Field(..., alias="Action", description="An array of strings that represent actions within OneLogin. Actions are prefixed with the class of object they are related to and followed by a specific action for the given class. e.g. users:List, where the class is users and the specific action is List. Don’t mix classes within an Action array. To create a privilege that includes multiple different classes, create multiple statements. A wildcard * that includes all actions is supported. Use wildcards to create a Super User privilege.")
    scope: List[StrictStr] = Field(..., alias="Scope", description="Target the privileged action against specific resources with the scope. The scope pattern is the class of object used by the Action, followed by an ID that represents a resource in OneLogin. e.g. apps/1234, where apps is the class and 1234 is the ID of an app. The wildcard * is supported and indicates that all resources of the class type declared, in the Action, are in scope. The Action and Scope classes must match. However, there is an exception, a scope of roles/{role_id} can be combined with Actions on the user or app class. The exception allows you to target groups of users or apps with specific actions.")
    __properties = ["Effect", "Action", "Scope"]

    @validator('action')
    def action_validate_enum(cls, v):
        if v not in ('Apps:Create', 'Apps:Delete', 'Apps:List', 'Apps:Get', 'Apps:Update', 'Apps:ManageConnectors', 'Apps:ManageRoles', 'Apps:ManageTabs', 'Apps:ManageUsers', 'Apps:ReapplyMappings', 'Users:Create', 'Users:Delete', 'Users:List', 'Users:Get', 'Users:Update', 'Users:AssumeUser', 'Users:ManageApps', 'Users:Unlock', 'Users:GenerateTempMfaToken', 'Users:ResetPassword', 'Users:ReapplyMappings', 'Users:ManageLicense', 'Users:Invite', 'Users:ManageRoles', 'Roles:Create', 'Roles:Get', 'Roles:List', 'Roles:Update', 'Roles:Delete', 'Roles:ManageUsers', 'Roles:ManageApps', 'Reports:Create', 'Reports:Get', 'Reports:List', 'Reports:Update', 'Reports:Delete', 'Reports:Clone', 'Events:Get', 'Events:List', 'Groups:Create', 'Groups:Get', 'Groups:List', 'Groups:Update', 'Groups:Delete', 'Policies:Create', 'Policies:Get', 'Policies:List', 'Policies:Update', 'Policies:Delete', 'Policies:SetDefault'):
            raise ValueError("must validate the enum values ('Apps:Create', 'Apps:Delete', 'Apps:List', 'Apps:Get', 'Apps:Update', 'Apps:ManageConnectors', 'Apps:ManageRoles', 'Apps:ManageTabs', 'Apps:ManageUsers', 'Apps:ReapplyMappings', 'Users:Create', 'Users:Delete', 'Users:List', 'Users:Get', 'Users:Update', 'Users:AssumeUser', 'Users:ManageApps', 'Users:Unlock', 'Users:GenerateTempMfaToken', 'Users:ResetPassword', 'Users:ReapplyMappings', 'Users:ManageLicense', 'Users:Invite', 'Users:ManageRoles', 'Roles:Create', 'Roles:Get', 'Roles:List', 'Roles:Update', 'Roles:Delete', 'Roles:ManageUsers', 'Roles:ManageApps', 'Reports:Create', 'Reports:Get', 'Reports:List', 'Reports:Update', 'Reports:Delete', 'Reports:Clone', 'Events:Get', 'Events:List', 'Groups:Create', 'Groups:Get', 'Groups:List', 'Groups:Update', 'Groups:Delete', 'Policies:Create', 'Policies:Get', 'Policies:List', 'Policies:Update', 'Policies:Delete', 'Policies:SetDefault')")
        return v

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> PrivilegePrivilegeStatementInner:
        """Create an instance of PrivilegePrivilegeStatementInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PrivilegePrivilegeStatementInner:
        """Create an instance of PrivilegePrivilegeStatementInner from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return PrivilegePrivilegeStatementInner.parse_obj(obj)

        _obj = PrivilegePrivilegeStatementInner.parse_obj({
            "effect": obj.get("Effect"),
            "action": obj.get("Action"),
            "scope": obj.get("Scope")
        })
        return _obj

