""" DNS services """

from typing import Any, Dict

import requests

from ..api_types import BasePFSenseAPIClient


def get_dynamic_dns(self: BasePFSenseAPIClient, **filterargs: Dict[str, Any]) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-read-dynamic-dns"""
    url = "/api/v1/services/ddns"
    return self.call(url, payload=filterargs)


def apply_pending_dnsmasq_changes(
    self: BasePFSenseAPIClient, **args: Dict[str, Any]
) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-apply-pending-dnsmasq-changes"""
    url = "/api/v1/services/dnsmasq/apply"
    method = "POST"
    return self.call(url=url, method=method, payload=args)


def get_dnsmasq_configuration(
    self: BasePFSenseAPIClient, **filterargs: Dict[str, Any]) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-read-dnsmasq-configuration"""
    url = "/api/v1/services/dnsmasq"
    return self.call(url, payload=filterargs)


def create_dnsmasq_host_override(
    self: BasePFSenseAPIClient, **args: Dict[str, Any]
) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-dnsmasq-host-override"""
    url = "/api/v1/services/dnsmasq/host_override"
    method = "POST"
    return self.call(url=url, method=method, payload=args)


def delete_dnsmasq_host_override(
    self: BasePFSenseAPIClient, **args: Dict[str, Any]
) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-dnsmasq-host-override"""
    url = "/api/v1/services/dnsmasq/host_override"
    method = "DELETE"
    return self.call(url=url, method=method, payload=args)


def get_dnsmasq_host_override(
    self: BasePFSenseAPIClient, **filterargs: Dict[str, Any]) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-read-dnsmasq-host-override"""
    url = "/api/v1/services/dnsmasq/host_override"
    return self.call(url, payload=filterargs)


def update_dnsmasq_host_override(
    self: BasePFSenseAPIClient, **args: Dict[str, Any]
) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-update-dnsmasq-host-override"""
    url = "/api/v1/services/dnsmasq/host_override"
    method = "PUT"
    return self.call(url=url, method=method, payload=args)


def create_dnsmasq_host_override_alias(
    self: BasePFSenseAPIClient, **args: Dict[str, Any]
) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-dnsmasq-host-override-alias"""
    url = "/api/v1/services/dnsmasq/host_override/alias"
    method = "POST"
    return self.call(url=url, method=method, payload=args)


def apply_pending_unbound_changes(
    self: BasePFSenseAPIClient, **args: Dict[str, Any]
) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-apply-pending-unbound-changes"""
    url = "/api/v1/services/unbound/apply"
    method = "POST"
    return self.call(url=url, method=method, payload=args)


def get_unbound_configuration(
    self: BasePFSenseAPIClient, **filterargs: Dict[str, Any]) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-read-unbound-configuration"""
    url = "/api/v1/services/unbound"
    return self.call(url, payload=filterargs)


def create_unbound_access_list(
    self: BasePFSenseAPIClient, **args: Dict[str, Any]
) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-unbound-access-list"""
    url = "/api/v1/services/unbound/access_list"
    method = "POST"
    return self.call(url=url, method=method, payload=args)


def delete_unbound_access_list(
    self: BasePFSenseAPIClient, **args: Dict[str, Any]
) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-unbound-access-list"""
    url = "/api/v1/services/unbound/access_list"
    method = "DELETE"
    return self.call(url=url, method=method, payload=args)


def get_unbound_access_lists(
    self: BasePFSenseAPIClient, **filterargs: Dict[str, Any]) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-read-unbound-access-lists"""
    url = "/api/v1/services/unbound/access_list"
    return self.call(url, payload=filterargs)


def update_unbound_access_list(
    self: BasePFSenseAPIClient, **args: Dict[str, Any]
) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-update-unbound-access-list"""
    url = "/api/v1/services/unbound/access_list"
    method = "PUT"
    return self.call(url=url, method=method, payload=args)


def create_unbound_access_list_row(
    self: BasePFSenseAPIClient, **args: Dict[str, Any]
) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-unbound-access-list-row"""
    url = "/api/v1/services/unbound/access_list/row"
    method = "POST"
    return self.call(url=url, method=method, payload=args)


def create_unbound_host_override(
    self: BasePFSenseAPIClient, **args: Dict[str, Any]
) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-unbound-host-override"""
    url = "/api/v1/services/unbound/host_override"
    method = "POST"
    return self.call(url=url, method=method, payload=args)


def delete_unbound_host_override(
    self: BasePFSenseAPIClient, **args: Dict[str, Any]
) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-unbound-host-override"""
    url = "/api/v1/services/unbound/host_override"
    method = "DELETE"
    return self.call(url=url, method=method, payload=args)


def get_unbound_host_override(
    self: BasePFSenseAPIClient, **filterargs: Dict[str, Any]) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-read-unbound-host-override"""
    url = "/api/v1/services/unbound/host_override"
    return self.call(url, payload=filterargs)


def update_unbound_host_override(
    self: BasePFSenseAPIClient, **args: Dict[str, Any]
) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-update-unbound-host-override"""
    url = "/api/v1/services/unbound/host_override"
    method = "PUT"
    return self.call(url=url, method=method, payload=args)


def create_unbound_host_override_alias(
    self: BasePFSenseAPIClient, **args: Dict[str, Any]
) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-unbound-host-override-alias"""
    url = "/api/v1/services/unbound/host_override/alias"
    method = "POST"
    return self.call(url=url, method=method, payload=args)
