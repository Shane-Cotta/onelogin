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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr
from onelogin.models.scope import Scope

class ClientAppFull(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    scopes: Optional[List[Scope]] = Field(None, description="List of All Scopes assigned to a client app")
    app_id: Optional[StrictInt] = Field(None, description="Unique Client App ID")
    name: Optional[StrictStr] = Field(None, description="Name of client app")
    api_auth_id: Optional[StrictInt] = None
    __properties = ["scopes", "app_id", "name", "api_auth_id"]

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
    def from_json(cls, json_str: str) -> ClientAppFull:
        """Create an instance of ClientAppFull from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in scopes (list)
        _items = []
        if self.scopes:
            for _item in self.scopes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['scopes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ClientAppFull:
        """Create an instance of ClientAppFull from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ClientAppFull.parse_obj(obj)

        _obj = ClientAppFull.parse_obj({
            "scopes": [Scope.from_dict(_item) for _item in obj.get("scopes")] if obj.get("scopes") is not None else None,
            "app_id": obj.get("app_id"),
            "name": obj.get("name"),
            "api_auth_id": obj.get("api_auth_id")
        })
        return _obj

