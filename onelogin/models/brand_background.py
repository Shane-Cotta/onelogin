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



from pydantic import BaseModel, StrictInt, StrictStr
from onelogin.models.brand_background_urls import BrandBackgroundUrls

class BrandBackground(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    urls: BrandBackgroundUrls = ...
    file_size: StrictInt = ...
    updated_at: StrictStr = ...
    content_type: StrictStr = ...
    __properties = ["urls", "file_size", "updated_at", "content_type"]

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
    def from_json(cls, json_str: str) -> BrandBackground:
        """Create an instance of BrandBackground from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of urls
        if self.urls:
            _dict['urls'] = self.urls.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BrandBackground:
        """Create an instance of BrandBackground from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return BrandBackground.parse_obj(obj)

        _obj = BrandBackground.parse_obj({
            "urls": BrandBackgroundUrls.from_dict(obj.get("urls")) if obj.get("urls") is not None else None,
            "file_size": obj.get("file_size"),
            "updated_at": obj.get("updated_at"),
            "content_type": obj.get("content_type")
        })
        return _obj

