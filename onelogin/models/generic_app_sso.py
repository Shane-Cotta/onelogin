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
import json
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from onelogin.models.sso_oidc import SsoOidc
from onelogin.models.sso_saml import SsoSaml
from typing import Any, List
from pydantic import StrictStr, Field

GENERICAPPSSO_ONE_OF_SCHEMAS = ["SsoOidc", "SsoSaml"]

class GenericAppSso(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    # data type: SsoOidc
    __oneof_schema_1: Optional[SsoOidc] = None
    # data type: SsoSaml
    __oneof_schema_2: Optional[SsoSaml] = None
    actual_instance: Any
    one_of_schemas: List[str] = Field(GENERICAPPSSO_ONE_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    @validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        error_messages = []
        match = 0
        # validate data type: SsoOidc
        if type(v) is not SsoOidc:
            error_messages.append(f"Error! Input type `{type(v)}` is not `SsoOidc`")
        else:
            match += 1

        # validate data type: SsoSaml
        if type(v) is not SsoSaml:
            error_messages.append(f"Error! Input type `{type(v)}` is not `SsoSaml`")
        else:
            match += 1

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into GenericAppSso with oneOf schemas: SsoOidc, SsoSaml. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into GenericAppSso with oneOf schemas: SsoOidc, SsoSaml. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> GenericAppSso:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> GenericAppSso:
        """Returns the object represented by the json string"""
        instance = cls()
        error_messages = []
        match = 0

        # deserialize data into SsoOidc
        try:
            instance.actual_instance = SsoOidc.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))
        # deserialize data into SsoSaml
        try:
            instance.actual_instance = SsoSaml.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into GenericAppSso with oneOf schemas: SsoOidc, SsoSaml. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into GenericAppSso with oneOf schemas: SsoOidc, SsoSaml. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is not None:
            return self.actual_instance.to_json()
        else:
            return "null"

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is not None:
            return self.actual_instance.to_dict()
        else:
            return dict()

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())





