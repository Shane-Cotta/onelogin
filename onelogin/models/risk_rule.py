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
from pydantic import BaseModel, Field, StrictStr, validator
from onelogin.models.source import Source

class RiskRule(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[StrictStr] = None
    name: Optional[StrictStr] = Field(None, description="The name of this rule")
    description: Optional[StrictStr] = None
    type: Optional[StrictStr] = Field(None, description="The type parameter specifies the type of rule that will be created.")
    target: Optional[StrictStr] = Field(None, description="The target parameter that will be used when evaluating the rule against an incoming event.")
    filters: Optional[List[StrictStr]] = Field(None, description="A list of IP addresses or country codes or names to evaluate against each event.")
    source: Optional[Source] = None
    __properties = ["id", "name", "description", "type", "target", "filters", "source"]

    @validator('type')
    def type_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('blacklist', 'whitelist'):
            raise ValueError("must validate the enum values ('blacklist', 'whitelist')")
        return v

    @validator('target')
    def target_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('location.ip', 'location.address.country_iso_code'):
            raise ValueError("must validate the enum values ('location.ip', 'location.address.country_iso_code')")
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
    def from_json(cls, json_str: str) -> RiskRule:
        """Create an instance of RiskRule from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RiskRule:
        """Create an instance of RiskRule from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return RiskRule.parse_obj(obj)

        _obj = RiskRule.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "type": obj.get("type"),
            "target": obj.get("target"),
            "filters": obj.get("filters"),
            "source": Source.from_dict(obj.get("source")) if obj.get("source") is not None else None
        })
        return _obj

