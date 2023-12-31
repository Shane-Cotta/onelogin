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
from onelogin.models.email_config import EmailConfig
from onelogin.models.get_email_settings200_response_one_of import GetEmailSettings200ResponseOneOf
from typing import Any, List
from pydantic import StrictStr, Field

GETEMAILSETTINGS200RESPONSE_ONE_OF_SCHEMAS = ["EmailConfig", "GetEmailSettings200ResponseOneOf"]

class GetEmailSettings200Response(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    # data type: GetEmailSettings200ResponseOneOf
    __oneof_schema_1: Optional[GetEmailSettings200ResponseOneOf] = None
    # data type: EmailConfig
    __oneof_schema_2: Optional[EmailConfig] = None
    actual_instance: Any
    one_of_schemas: List[str] = Field(GETEMAILSETTINGS200RESPONSE_ONE_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    @validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        error_messages = []
        match = 0
        # validate data type: GetEmailSettings200ResponseOneOf
        if type(v) is not GetEmailSettings200ResponseOneOf:
            error_messages.append(f"Error! Input type `{type(v)}` is not `GetEmailSettings200ResponseOneOf`")
        else:
            match += 1

        # validate data type: EmailConfig
        if type(v) is not EmailConfig:
            error_messages.append(f"Error! Input type `{type(v)}` is not `EmailConfig`")
        else:
            match += 1

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into GetEmailSettings200Response with oneOf schemas: EmailConfig, GetEmailSettings200ResponseOneOf. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into GetEmailSettings200Response with oneOf schemas: EmailConfig, GetEmailSettings200ResponseOneOf. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> GetEmailSettings200Response:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> GetEmailSettings200Response:
        """Returns the object represented by the json string"""
        instance = cls()
        error_messages = []
        match = 0

        # deserialize data into GetEmailSettings200ResponseOneOf
        try:
            instance.actual_instance = GetEmailSettings200ResponseOneOf.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))
        # deserialize data into EmailConfig
        try:
            instance.actual_instance = EmailConfig.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into GetEmailSettings200Response with oneOf schemas: EmailConfig, GetEmailSettings200ResponseOneOf. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into GetEmailSettings200Response with oneOf schemas: EmailConfig, GetEmailSettings200ResponseOneOf. Details: " + ", ".join(error_messages))
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





