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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, validator

class Event(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    account_id: Optional[StrictInt] = Field(None, description="Account that triggered the event.")
    actor_system: Optional[StrictStr] = Field(None, description="Acting system that triggered the event when the actor is not a user.")
    actor_user_id: Optional[StrictInt] = Field(None, description="ID of the user whose action triggered the event.")
    actor_user_name: Optional[StrictStr] = Field(None, description="First and last name of the user whose action triggered the event.")
    adc_id: Optional[StrictInt] = None
    app_name: Optional[StrictStr] = Field(None, alias="app-name", description="Name of the app involved in the event, if applicable.")
    app_id: Optional[StrictInt] = Field(None, description="ID of the app involved in the event, if applicable.")
    assumed_by_superadmin_or_reseller: Optional[StrictInt] = None
    assuming_acting_user_id: Optional[StrictInt] = Field(None, description="ID of the user who assumed the role of the acting user to trigger the event, if applicable.")
    certificate_id: Optional[StrictInt] = None
    client_id: Optional[StrictStr] = Field(None, description="Client ID used to generate the access token that made the API call that generated the event.")
    created_at: Optional[StrictStr] = Field(None, description="ISO8601 Time and date at which the event was created. This value is autogenerated by OneLogin.")
    custom_message: Optional[StrictStr] = Field(None, description="More details about the event.")
    directory_sync_run_id: Optional[StrictInt] = Field(None, description="Directory sync run ID.")
    error_description: Optional[StrictStr] = Field(None, description="Provisioning error details, if applicable.")
    event_type_id: Optional[StrictInt] = Field(None, description="Type of event triggered.")
    group_name: Optional[StrictStr] = Field(None, alias="group-name", description="Name of a group involved in the event.")
    group_id: Optional[StrictInt] = Field(None, description="ID of a group involved in the event.")
    id: Optional[StrictInt] = Field(None, description="Event's unique ID in OneLogin. Autogenerated by OneLogin.")
    ipaddr: Optional[StrictStr] = Field(None, description="IP address of the machine used to trigger the event.")
    mapping_id: Optional[StrictInt] = None
    notes: Optional[StrictStr] = Field(None, description="More details about the event.")
    object_id: Optional[StrictInt] = None
    otp_device_id: Optional[StrictInt] = Field(None, description="ID of a device involved in the event.")
    otp_device_name: Optional[StrictStr] = Field(None, description="Name of a device involved in the event.")
    param: Optional[StrictStr] = None
    policy_id: Optional[StrictInt] = Field(None, description="ID of the policy involved in the event.")
    policy_name: Optional[StrictStr] = Field(None, description="Name of the policy involved in the event.")
    policy_type: Optional[StrictStr] = None
    privilege_id: Optional[StrictInt] = None
    proxy_ip: Optional[StrictStr] = None
    radius_config_id: Optional[StrictInt] = None
    resolved_at: Optional[StrictStr] = None
    resource_type_id: Optional[StrictInt] = Field(None, description="ID of the resource (user, role, group, and so forth) associated with the event.")
    risk_cookie_id: Optional[StrictStr] = Field(None, description="Identifier for risk cookie")
    risk_reasons: Optional[StrictStr] = None
    risk_score: Optional[StrictInt] = None
    role_id: Optional[StrictInt] = Field(None, description="ID of a role involved in the event.")
    role_name: Optional[StrictStr] = Field(None, description="Name of a role involved in the event.")
    service_directory_id: Optional[StrictInt] = None
    solved: Optional[StrictBool] = None
    trusted_idp_id: Optional[StrictInt] = None
    user_field_id: Optional[StrictInt] = None
    user_id: Optional[StrictInt] = Field(None, description="ID of the user that was acted upon to trigger the event.")
    user_name: Optional[StrictStr] = Field(None, description="Name of the user that was acted upon to trigger the event.")
    __properties = ["account_id", "actor_system", "actor_user_id", "actor_user_name", "adc_id", "app-name", "app_id", "assumed_by_superadmin_or_reseller", "assuming_acting_user_id", "certificate_id", "client_id", "created_at", "custom_message", "directory_sync_run_id", "error_description", "event_type_id", "group-name", "group_id", "id", "ipaddr", "mapping_id", "notes", "object_id", "otp_device_id", "otp_device_name", "param", "policy_id", "policy_name", "policy_type", "privilege_id", "proxy_ip", "radius_config_id", "resolved_at", "resource_type_id", "risk_cookie_id", "risk_reasons", "risk_score", "role_id", "role_name", "service_directory_id", "solved", "trusted_idp_id", "user_field_id", "user_id", "user_name"]

    @validator('event_type_id')
    def event_type_id_validate_enum(cls, v):
        if v is None:
            return v

        if v not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 95, 96, 100, 101, 102, 103, 104, 105, 106, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 291, 300, 301, 303, 304, 305, 306, 307, 330, 331, 332, 333, 334, 400, 401, 402, 410, 411, 412, 501, 502, 503, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 545, 546, 550, 551, 552, 553, 554, 555, 600, 601, 602, 700, 701, 702, 703, 704, 705, 706, 800, 801, 802, 803, 804, 805, 900, 901, 902, 903, 904, 905, 906, 907, 911, 912, 931, 932, 950, 1001, 1002, 1010, 1100, 1101, 1200, 1201, 1244, 1245, 1300, 1301, 1302, 1303, 1304, 1305, 1400, 1401, 1402, 1403, 1404, 1405, 1406, 1407, 1408, 1409, 1410, 1411, 1412, 1413, 1414, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1422, 1423, 1424, 1500, 1501, 1502, 1503, 1504, 1505, 1506, 1507, 1508, 1509, 1510, 1511, 1512, 1513, 1514, 1600, 1601, 1602, 1603, 1604, 1605, 1606, 1607, 1608, 1609, 1700, 1701, 1702, 1801, 1802, 1900, 1901, 1902, 1903, 1904, 1905, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2100, 2101, 2102, 2103, 2104, 2105, 2106, 2107, 2108, 2109, 2110, 2111, 2112, 2113, 2114, 2201, 2202, 2203, 2204, 3000, 3001, 3002, 3003, 3004, 3005, 3006, 3007, 3008, 3009, 3010, 3011, 3012, 3013, 3014, 3015, 3016, 3017, 3018, 3019, 3020, 3021, 3022, 3023, 3024, 3025, 3026, 3027, 3028, 9000, 9001, 9002, 9003, 9004, 9005, 9006, 9007, 9008, 9009, 9010, 9011, 9012, 9013, 9014, 9015, 9016, 9017, 9018, 9019, 9020, 9021, 9022, 9023, 9024, 9025, 9026, 9027, 9028, 9029, 9030, 9031, 9032, 9033, 9034, 9035, 9036, 9037, 9038, 9039, 9040, 9041, 9042, 9043, 9044, 9045, 9046, 9047, 9048, 9049, 9050, 9051, 9052, 9053, 9054, 9055, 9056, 9057, 9058, 9059):
            raise ValueError("must validate the enum values (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 95, 96, 100, 101, 102, 103, 104, 105, 106, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 291, 300, 301, 303, 304, 305, 306, 307, 330, 331, 332, 333, 334, 400, 401, 402, 410, 411, 412, 501, 502, 503, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 545, 546, 550, 551, 552, 553, 554, 555, 600, 601, 602, 700, 701, 702, 703, 704, 705, 706, 800, 801, 802, 803, 804, 805, 900, 901, 902, 903, 904, 905, 906, 907, 911, 912, 931, 932, 950, 1001, 1002, 1010, 1100, 1101, 1200, 1201, 1244, 1245, 1300, 1301, 1302, 1303, 1304, 1305, 1400, 1401, 1402, 1403, 1404, 1405, 1406, 1407, 1408, 1409, 1410, 1411, 1412, 1413, 1414, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1422, 1423, 1424, 1500, 1501, 1502, 1503, 1504, 1505, 1506, 1507, 1508, 1509, 1510, 1511, 1512, 1513, 1514, 1600, 1601, 1602, 1603, 1604, 1605, 1606, 1607, 1608, 1609, 1700, 1701, 1702, 1801, 1802, 1900, 1901, 1902, 1903, 1904, 1905, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2100, 2101, 2102, 2103, 2104, 2105, 2106, 2107, 2108, 2109, 2110, 2111, 2112, 2113, 2114, 2201, 2202, 2203, 2204, 3000, 3001, 3002, 3003, 3004, 3005, 3006, 3007, 3008, 3009, 3010, 3011, 3012, 3013, 3014, 3015, 3016, 3017, 3018, 3019, 3020, 3021, 3022, 3023, 3024, 3025, 3026, 3027, 3028, 9000, 9001, 9002, 9003, 9004, 9005, 9006, 9007, 9008, 9009, 9010, 9011, 9012, 9013, 9014, 9015, 9016, 9017, 9018, 9019, 9020, 9021, 9022, 9023, 9024, 9025, 9026, 9027, 9028, 9029, 9030, 9031, 9032, 9033, 9034, 9035, 9036, 9037, 9038, 9039, 9040, 9041, 9042, 9043, 9044, 9045, 9046, 9047, 9048, 9049, 9050, 9051, 9052, 9053, 9054, 9055, 9056, 9057, 9058, 9059)")
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
    def from_json(cls, json_str: str) -> Event:
        """Create an instance of Event from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Event:
        """Create an instance of Event from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return Event.parse_obj(obj)

        _obj = Event.parse_obj({
            "account_id": obj.get("account_id"),
            "actor_system": obj.get("actor_system"),
            "actor_user_id": obj.get("actor_user_id"),
            "actor_user_name": obj.get("actor_user_name"),
            "adc_id": obj.get("adc_id"),
            "app_name": obj.get("app-name"),
            "app_id": obj.get("app_id"),
            "assumed_by_superadmin_or_reseller": obj.get("assumed_by_superadmin_or_reseller"),
            "assuming_acting_user_id": obj.get("assuming_acting_user_id"),
            "certificate_id": obj.get("certificate_id"),
            "client_id": obj.get("client_id"),
            "created_at": obj.get("created_at"),
            "custom_message": obj.get("custom_message"),
            "directory_sync_run_id": obj.get("directory_sync_run_id"),
            "error_description": obj.get("error_description"),
            "event_type_id": obj.get("event_type_id"),
            "group_name": obj.get("group-name"),
            "group_id": obj.get("group_id"),
            "id": obj.get("id"),
            "ipaddr": obj.get("ipaddr"),
            "mapping_id": obj.get("mapping_id"),
            "notes": obj.get("notes"),
            "object_id": obj.get("object_id"),
            "otp_device_id": obj.get("otp_device_id"),
            "otp_device_name": obj.get("otp_device_name"),
            "param": obj.get("param"),
            "policy_id": obj.get("policy_id"),
            "policy_name": obj.get("policy_name"),
            "policy_type": obj.get("policy_type"),
            "privilege_id": obj.get("privilege_id"),
            "proxy_ip": obj.get("proxy_ip"),
            "radius_config_id": obj.get("radius_config_id"),
            "resolved_at": obj.get("resolved_at"),
            "resource_type_id": obj.get("resource_type_id"),
            "risk_cookie_id": obj.get("risk_cookie_id"),
            "risk_reasons": obj.get("risk_reasons"),
            "risk_score": obj.get("risk_score"),
            "role_id": obj.get("role_id"),
            "role_name": obj.get("role_name"),
            "service_directory_id": obj.get("service_directory_id"),
            "solved": obj.get("solved"),
            "trusted_idp_id": obj.get("trusted_idp_id"),
            "user_field_id": obj.get("user_field_id"),
            "user_id": obj.get("user_id"),
            "user_name": obj.get("user_name")
        })
        return _obj

