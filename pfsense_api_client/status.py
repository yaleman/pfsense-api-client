""" status-related endpoints """
from typing import Any, Dict, Optional

import requests
import pydantic

from .api_types import APIResponse, APIResponseDict, BasePFSenseAPIClient

__all__ = [
    "StatusMixin",
]


#pylint: disable=too-many-public-methods
class StatusMixin(BasePFSenseAPIClient):
    """ status calls """
    def get_carp_status(
        self, **filterargs: Dict[str, Any]
    ) -> requests.Response:
        """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-read-carp-status"""
        url = "/api/v1/status/carp"
        return self.call(url, payload=filterargs)


    @pydantic.validate_arguments()
    def update_carp_status(
        self, enable: Optional[bool], maintenance_mode: Optional[bool]
    ) -> requests.Response:
        """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-update-carp-status"""
        url = "/api/v1/status/carp"
        method = "PUT"
        payload = {}
        if enable is not None:
            payload["enable"] = enable
        if maintenance_mode is not None:
            payload["maintenance_mode"] = maintenance_mode
        return self.call(url=url, method=method, payload=payload)


    def get_gateway_status(
        self, **filterargs: Dict[str, Any]
    ) -> requests.Response:
        """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-read-gateway-status"""
        url = "/api/v1/status/gateway"
        return self.call(url, payload=filterargs)


    def get_interface_status(
        self, **filterargs: Dict[str, Any]
    ) -> requests.Response:
        """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-read-interface-status"""
        url = "/api/v1/status/interface"
        return self.call(url, payload=filterargs)


    def get_configuration_history_status_log(
        self,
        **filterargs: Dict[str, Any],
    ) -> requests.Response:
        """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-read-configuration-history-status-log"""
        url = "/api/v1/status/log/config_history"
        return self.call(url, payload=filterargs)


    def get_dhcp_status_log(
        self, **filterargs: Dict[str, Any]
    ) -> APIResponse:
        """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-read-dhcp-status-log"""
        url = "/api/v1/status/log/dhcp"
        return self.call_api(url, payload=filterargs)


    def get_firewall_status_log(
        self, **filterargs: Dict[str, Any]
    ) -> requests.Response:
        """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-read-firewall-status-log"""
        url = "/api/v1/status/log/firewall"
        return self.call(url, payload=filterargs)


    def get_system_status_log(
        self, **filterargs: Dict[str, Any]
    ) -> requests.Response:
        """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-read-system-status-log"""
        url = "/api/v1/status/log/system"
        return self.call(url, payload=filterargs)


    def get_openvpn_status(
        self, **filterargs: Dict[str, Any]
    ) -> requests.Response:
        """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-read-openvpn-status"""
        url = "/api/v1/status/openvpn"
        return self.call(url, payload=filterargs)


    def get_system_status(
        self, **filterargs: Dict[str, Any]
    ) -> APIResponseDict:
        """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-read-system-status"""
        url = "/api/v1/status/system"
        result = APIResponseDict.parse_obj(self.call_json(url, payload=filterargs))
        return result
