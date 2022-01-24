""" system-related endpoints """

from typing import List, Optional

import pydantic

# TODO: url = "/api/v1/system/api/error"

def get_system_api_error(self):
    """ gets the list of error codes

    https://github.com/jaredhendrickson13/pfsense-api#2-read-system-api-error-library
    """
    url = "/api/v1/system/api/error"
    return self.call(url)

def get_system_api_version(self):
    """ Read the current API version and locate available version updates.

    https://github.com/jaredhendrickson13/pfsense-api#3-read-system-api-version
    """
    url = "/api/v1/system/api/version"
    method = "GET"
    return self.call(url, method)

def update_system_api_configuration(self, **kwargs):
    """ Update the API configuration.

    https://github.com/jaredhendrickson13/pfsense-api#3-read-system-api-version
    """
    url = "/api/v1/system/api"
    method = "PUT"

    class APIConfiguration(pydantic.BaseModel):
        """ API Config options"""
        enable: Optional[bool]
        persist: Optional[bool]
        readonly: bool
        allow_options: Optional[bool]
        available_interfaces: Optional[List[str]]
        authmode: Optional[str]
        jwt_exp: Optional[int]
        keyhash: Optional[str]
        keybytes: Optional[int]
        custom_headers: Optional[List[str]]
        hasync: Optional[bool]
        hasync_hosts: Optional[List[str]]
        hasync_username: Optional[str]
        hasync_password: Optional[str]

    payload = APIConfiguration(**kwargs)

    return self.call(url, method, payload=payload.dict())

# TODO: url = "/api/v1/system/api"


# TODO: url = "/api/v1/system/arp"
# TODO: url = "/api/v1/system/ca"
# TODO: url = "/api/v1/system/certificate"
# TODO: url = "/api/v1/system/config"
# TODO: url = "/api/v1/system/console"
# TODO: url = "/api/v1/system/dns"
# TODO: url = "/api/v1/system/dns/server"
# TODO: url = "/api/v1/system/halt"
# TODO: url = "/api/v1/system/hostname"
# TODO: url = "/api/v1/system/notifications/email"
# TODO: url = "/api/v1/system/reboot"
# TODO: url = "/api/v1/system/table"
# TODO: url = "/api/v1/system/tunable"
# TODO: url = "/api/v1/system/version"
