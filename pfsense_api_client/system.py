""" system-related endpoints """

from typing import Any, Dict, List, Optional

import pydantic
import requests

__all__ = [
    "create_system_ca",
    "create_system_certificates",
    "create_system_dns_server",
    "create_system_reboot",
    "create_system_tunables",
    "delete_system_arp_table",
    "delete_system_ca",
    "delete_system_certificates",
    "delete_system_dns_server",
    "delete_system_tunables",
    "get_system_api_configuration",
    "get_system_api_error",
    "get_system_api_error_library",
    "get_system_api_version",
    "get_system_arp_table",
    "get_system_cas",
    "get_system_certificates",
    "get_system_configuration",
    "get_system_dns",
    "get_system_email_notification_settings",
    "get_system_hostname",
    "get_system_tables",
    "get_system_tunables",
    "get_system_version",
    "halt_system",
    "update_console_settings",
    "update_system_api_configuration",
    "update_system_configuration",
    "update_system_dns",
    "update_system_email_notification_settings",
    "update_system_hostname",
    "update_system_tunables",
]


def get_system_api_error(self):
    """gets the list of error codes

    https://github.com/jaredhendrickson13/pfsense-api#2-read-system-api-error-library
    """
    url = "/api/v1/system/api/error"
    return self.call(url)


def get_system_api_version(self):
    """Read the current API version and locate available version updates.

    https://github.com/jaredhendrickson13/pfsense-api#3-read-system-api-version
    """
    url = "/api/v1/system/api/version"
    method = "GET"
    return self.call(url, method)


def update_system_api_configuration(self, **kwargs: Dict[str, Any]) -> requests.Response:
    """Update the API configuration.

    https://github.com/jaredhendrickson13/pfsense-api#3-read-system-api-version
    """
    url = "/api/v1/system/api"
    method = "PUT"

    class APIConfiguration(pydantic.BaseModel):
        """API Config options"""

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


def get_system_api_configuration(self, *filterargs) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-read-system-api-configuration"""
    url = "/api/v1/system/api"
    return self.call(url, payload=filterargs)


def get_system_api_error_library(self, *filterargs) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-read-system-api-error-library"""
    url = "/api/v1/system/api/error"
    return self.call(url, payload=filterargs)


def delete_system_arp_table(self, **args) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-delete-system-arp-table"""
    url = "/api/v1/system/arp"
    method = "DELETE"
    return self.call(url=url, method=method, payload=args)


def get_system_arp_table(self, *filterargs) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-read-system-arp-table"""
    url = "/api/v1/system/arp"
    return self.call(url, payload=filterargs)


def create_system_ca(self, **args) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-system-ca"""
    url = "/api/v1/system/ca"
    method = "POST"
    return self.call(url=url, method=method, payload=args)


def delete_system_ca(self, **args) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-system-ca"""
    url = "/api/v1/system/ca"
    method = "DELETE"
    return self.call(url=url, method=method, payload=args)


def get_system_cas(self, *filterargs) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-read-system-cas"""
    url = "/api/v1/system/ca"
    return self.call(url, payload=filterargs)


def create_system_certificates(self, **args) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-system-certificates"""
    url = "/api/v1/system/certificate"
    method = "POST"
    return self.call(url=url, method=method, payload=args)


def delete_system_certificates(self, **args) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-system-certificates"""
    url = "/api/v1/system/certificate"
    method = "DELETE"
    return self.call(url=url, method=method, payload=args)


def get_system_certificates(self, *filterargs) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-read-system-certificates"""
    url = "/api/v1/system/certificate"
    return self.call(url, payload=filterargs)


def get_system_configuration(self, *filterargs) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-read-system-configuration"""
    url = "/api/v1/system/config"
    return self.call(url, payload=filterargs)


def update_system_configuration(self, **args) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-update-system-configuration"""
    url = "/api/v1/system/config"
    method = "PUT"
    return self.call(url=url, method=method, payload=args)


def update_console_settings(self, **args) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-update-console-settings"""
    url = "/api/v1/system/console"
    method = "PUT"
    return self.call(url=url, method=method, payload=args)


def get_system_dns(self, *filterargs) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-read-system-dns"""
    url = "/api/v1/system/dns"
    return self.call(url, payload=filterargs)


def update_system_dns(self, **args) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-update-system-dns"""
    url = "/api/v1/system/dns"
    method = "PUT"
    return self.call(url=url, method=method, payload=args)


def create_system_dns_server(self, **args) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-system-dns-server"""
    url = "/api/v1/system/dns/server"
    method = "POST"
    return self.call(url=url, method=method, payload=args)


def delete_system_dns_server(self, **args) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-system-dns-server"""
    url = "/api/v1/system/dns/server"
    method = "DELETE"
    return self.call(url=url, method=method, payload=args)


def halt_system(self, **args) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-halt-system"""
    url = "/api/v1/system/halt"
    method = "POST"
    return self.call(url=url, method=method, payload=args)


def get_system_hostname(self, *filterargs) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-read-system-hostname"""
    url = "/api/v1/system/hostname"
    return self.call(url, payload=filterargs)


def update_system_hostname(self, **args) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-update-system-hostname"""
    url = "/api/v1/system/hostname"
    method = "PUT"
    return self.call(url=url, method=method, payload=args)


def get_system_email_notification_settings(self, *filterargs) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-read-system-email-notification-settings"""
    url = "/api/v1/system/notifications/email"
    return self.call(url, payload=filterargs)


def update_system_email_notification_settings(self, **args) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-update-system-email-notification-settings"""
    url = "/api/v1/system/notifications/email"
    method = "PUT"
    return self.call(url=url, method=method, payload=args)


def create_system_reboot(self, **args) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-system-reboot"""
    url = "/api/v1/system/reboot"
    method = "POST"
    return self.call(url=url, method=method, payload=args)


def get_system_tables(self, *filterargs) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-read-system-tables"""
    url = "/api/v1/system/table"
    return self.call(url, payload=filterargs)


def create_system_tunables(self, **args) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-system-tunables"""
    url = "/api/v1/system/tunable"
    method = "POST"
    return self.call(url=url, method=method, payload=args)


def delete_system_tunables(self, **args) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-system-tunables"""
    url = "/api/v1/system/tunable"
    method = "DELETE"
    return self.call(url=url, method=method, payload=args)


def get_system_tunables(self, *filterargs) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-read-system-tunables"""
    url = "/api/v1/system/tunable"
    return self.call(url, payload=filterargs)


def update_system_tunables(self, **args) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-update-system-tunables"""
    url = "/api/v1/system/tunable"
    method = "PUT"
    return self.call(url=url, method=method, payload=args)


def get_system_version(self, *filterargs) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-read-system-version"""
    url = "/api/v1/system/version"
    return self.call(url, payload=filterargs)
