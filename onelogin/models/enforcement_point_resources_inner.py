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


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, validator

class EnforcementPointResourcesInner(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    path: Optional[StrictStr] = None
    is_path_regex: Optional[StrictBool] = None
    require_auth: Optional[StrictBool] = None
    permission: Optional[StrictStr] = None
    conditions: Optional[StrictStr] = Field(None, description="required if permission == \"conditions\"")
    __properties = ["path", "is_path_regex", "require_auth", "permission", "conditions"]

    @validator('permission')
    def permission_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('allow', 'deny', 'conditions'):
            raise ValueError("must validate the enum values ('allow', 'deny', 'conditions')")
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
    def from_json(cls, json_str: str) -> EnforcementPointResourcesInner:
        """Create an instance of EnforcementPointResourcesInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if is_path_regex (nullable) is None
        if self.is_path_regex is None:
            _dict['is_path_regex'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EnforcementPointResourcesInner:
        """Create an instance of EnforcementPointResourcesInner from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return EnforcementPointResourcesInner.parse_obj(obj)

        _obj = EnforcementPointResourcesInner.parse_obj({
            "path": obj.get("path"),
            "is_path_regex": obj.get("is_path_regex"),
            "require_auth": obj.get("require_auth"),
            "permission": obj.get("permission"),
            "conditions": obj.get("conditions")
        })
        return _obj

