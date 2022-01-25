""" system-related endpoints """

from typing import List, Optional

import pydantic
import requests

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


def get_system_api_configuration(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-read-system-api-configuration """

def get_system_api_error_library(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-read-system-api-error-library """

def delete_system_arp_table(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-delete-system-arp-table """

def get_system_arp_table(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-read-system-arp-table """


def create_system_ca(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-system-ca """

def delete_system_ca(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-system-ca """

def get_system_cas(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-read-system-cas """


def create_system_certificates(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-system-certificates """

def delete_system_certificates(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-system-certificates """

def get_system_certificates(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-read-system-certificates """


def get_system_configuration(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-read-system-configuration """

def update_system_configuration(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-update-system-configuration """


def update_console_settings(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-update-console-settings """


def get_system_dns(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-read-system-dns """

def update_system_dns(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-update-system-dns """


def create_system_dns_server(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-system-dns-server """

def delete_system_dns_server(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-system-dns-server """


def halt_system(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-halt-system """


def get_system_hostname(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-read-system-hostname """

def update_system_hostname(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-update-system-hostname """


def get_system_email_notification_settings(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-read-system-email-notification-settings """

def update_system_email_notification_settings(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-update-system-email-notification-settings """


def create_system_reboot(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-system-reboot """


def get_system_tables(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-read-system-tables """


def create_system_tunables(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-system-tunables """

def delete_system_tunables(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-system-tunables """

def get_system_tunables(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-read-system-tunables """

def update_system_tunables(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-update-system-tunables """

def get_system_version(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-read-system-version """
