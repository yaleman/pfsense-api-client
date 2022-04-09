""" system_service_things """

from typing import Any, Dict

from requests import Response

from pfsense_api_client.api_types import APIResponse

def get_service(self, *filterargs) -> APIResponse:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-read-services"""
    url = "/api/v1/services"
    return self.call_api(url, payload=filterargs)


def restart_all_service(self, **args) -> Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-restart-all-services"""
    url = "/api/v1/services/restart"
    method = "POST"
    return self.call(url=url, method=method, payload=args)


def start_all_service(self, **args) -> Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-start-all-services"""
    url = "/api/v1/services/start"
    method = "POST"
    return self.call(url=url, method=method, payload=args)


def stop_all_service(self, **args) -> Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-stop-all-services"""
    url = "/api/v1/services/stop"
    method = "POST"
    return self.call(url=url, method=method, payload=args)


def get_dhcpd_service_configuration(self, *filterargs) -> APIResponse:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-read-dhcpd-service-configuration"""
    url = "/api/v1/services/dhcpd"
    return self.call_api(url, payload=filterargs)


def restart_dhcpd_service(self, **args) -> Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-restart-dhcpd-service_"""
    url = "/api/v1/services/dhcpd/restart"
    method = "POST"
    return self.call(url=url, method=method, payload=args)


def start_dhcpd_service(self, **args) -> Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-start-dhcpd-service_"""
    url = "/api/v1/services/dhcpd/start"
    method = "POST"
    return self.call(url=url, method=method, payload=args)


def stop_dhcpd_service(self, **args) -> Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-stop-dhcpd-service_"""
    url = "/api/v1/services/dhcpd/stop"
    method = "POST"
    response: Response = self.call(url=url, method=method, payload=args)
    return response


def update_dhcpd_service_configuration(self, **args) -> Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#5-update-dhcpd-service-configuration"""
    url = "/api/v1/services/dhcpd"
    method = "PUT"
    return self.call(url=url, method=method, payload=args)


def get_dhcpd_leases(self, *filterargs) -> APIResponse:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-read-dhcpd-leases"""
    url = "/api/v1/services/dhcpd/lease"
    return self.call_api(url, payload=filterargs)


def create_dhcpd_static_mappings(self, **args) -> Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-dhcpd-static-mappings"""
    url = "/api/v1/services/dhcpd/static_mapping"
    method = "POST"
    return self.call(url=url, method=method, payload=args)


def delete_dhcpd_static_mappings(self, **args) -> Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-dhcpd-static-mappings"""
    url = "/api/v1/services/dhcpd/static_mapping"
    method = "DELETE"
    return self.call(url=url, method=method, payload=args)


def get_dhcpd_static_mappings(self, *filterargs) -> Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-read-dhcpd-static-mappings"""
    url = "/api/v1/services/dhcpd/static_mapping"
    return self.call(url, payload=filterargs)


def update_dhcpd_static_mappings(self, **args) -> Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-update-dhcpd-static-mappings"""
    url = "/api/v1/services/dhcpd/static_mapping"
    method = "PUT"
    return self.call(url=url, method=method, payload=args)


def restart_dnsmasq_service(self, **args) -> Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-restart-dnsmasq-service_"""
    url = "/api/v1/services/dnsmasq/restart"
    method = "POST"
    return self.call(url=url, method=method, payload=args)


def start_dnsmasq_service(self, **args) -> Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-start-dnsmasq-service_"""
    url = "/api/v1/services/dnsmasq/start"
    method = "POST"
    return self.call(url=url, method=method, payload=args)


def stop_dnsmasq_service(self, **args) -> Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#5-stop-dnsmasq-service_"""
    url = "/api/v1/services/dnsmasq/stop"
    method = "POST"
    return self.call(url=url, method=method, payload=args)


def restart_dpinger_service(self, **args) -> Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-restart-dpinger-service_"""
    url = "/api/v1/services/dpinger/restart"
    method = "POST"
    return self.call(url=url, method=method, payload=args)


def start_dpinger_service(self, **args) -> Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-start-dpinger-service_"""
    url = "/api/v1/services/dpinger/start"
    method = "POST"
    return self.call(url=url, method=method, payload=args)


def stop_dpinger_service(self, **args) -> Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-stop-dpinger-service_"""
    url = "/api/v1/services/dpinger/stop"
    method = "POST"
    return self.call(url=url, method=method, payload=args)


def get_ntpd_service(self, *filterargs) -> Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-read-ntpd-service_"""
    url = "/api/v1/services/ntpd"
    return self.call(url, payload=filterargs)


def restart_ntpd_service(self, **args) -> Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-restart-ntpd-service_"""
    url = "/api/v1/services/ntpd/restart"
    method = "POST"
    return self.call(url=url, method=method, payload=args)


def start_ntpd_service(self, **args) -> Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-start-ntpd-service_"""
    url = "/api/v1/services/ntpd/start"
    method = "POST"
    return self.call(url=url, method=method, payload=args)


def stop_ntpd_service(self, **args) -> Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-stop-ntpd-service_"""
    url = "/api/v1/services/ntpd/stop"
    method = "POST"
    return self.call(url=url, method=method, payload=args)


def update_ntpd_service(self, **args) -> Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#5-update-ntpd-service_"""
    url = "/api/v1/services/ntpd"
    method = "PUT"
    return self.call(url=url, method=method, payload=args)


def create_ntpd_time_server(self, **args) -> Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-ntpd-time-server"""
    url = "/api/v1/services/ntpd/time_server"
    method = "POST"
    return self.call(url=url, method=method, payload=args)


def delete_ntpd_time_server(self, **args) -> Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-ntpd-time-server"""
    url = "/api/v1/services/ntpd/time_server"
    method = "DELETE"
    return self.call(url=url, method=method, payload=args)


def create_openvpn_client_specific_overrides(self, **args) -> Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-openvpn-client-specific-overrides"""
    url = "/api/v1/services/openvpn/csc"
    method = "POST"
    return self.call(url=url, method=method, payload=args)


def delete_openvpn_client_specific_override(self, **args) -> Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-openvpn-client-specific-override"""
    url = "/api/v1/services/openvpn/csc"
    method = "DELETE"
    return self.call(url=url, method=method, payload=args)


def get_openvpn_client_specific_overrides(self, *filterargs) -> Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-read-openvpn-client-specific-overrides"""
    url = "/api/v1/services/openvpn/csc"
    return self.call(url, payload=filterargs)


def update_openvpn_client_specific_overrides(self, **args) -> Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-update-openvpn-client-specific-overrides"""
    url = "/api/v1/services/openvpn/csc"
    method = "PUT"
    return self.call(url=url, method=method, payload=args)


def get_sshd_configuration(self, *filterargs) -> Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-read-sshd-configuration"""
    url = "/api/v1/services/sshd"
    return self.call(url, payload=filterargs)


def restart_sshd_service(self, **args) -> Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-restart-sshd-service_"""
    url = "/api/v1/services/sshd/restart"
    method = "POST"
    return self.call(url=url, method=method, payload=args)


def start_sshd_service(self, **args) -> Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-start-sshd-service_"""
    url = "/api/v1/services/sshd/start"
    method = "POST"
    return self.call(url=url, method=method, payload=args)


def stop_sshd_service(self, **args) -> Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-stop-sshd-service_"""
    url = "/api/v1/services/sshd/stop"
    method = "POST"
    return self.call(url=url, method=method, payload=args)


def update_sshd_configuration(self, **args: Dict[str, Any]) -> Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#5-update-sshd-configuration"""
    url = "/api/v1/services/sshd"
    method = "PUT"
    return self.call(url=url, method=method, payload=args)


def restart_syslogd_service(self, **args) -> Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-restart-syslogd-service_"""
    url = "/api/v1/services/syslogd/restart"
    method = "POST"
    return self.call(url=url, method=method, payload=args)


def start_syslogd_service(self, **args) -> Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-start-syslogd-service_"""
    url = "/api/v1/services/syslogd/start"
    method = "POST"
    return self.call(url=url, method=method, payload=args)


def stop_syslogd_service(self, **args) -> Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-stop-syslogd-service_"""
    url = "/api/v1/services/syslogd/stop"
    method = "POST"
    return self.call(url=url, method=method, payload=args)


def restart_unbound_service(self, **args) -> Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-restart-unbound-service_"""
    url = "/api/v1/services/unbound/restart"
    method = "POST"
    return self.call(url=url, method=method, payload=args)


def start_unbound_service(self, **args) -> Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-start-unbound-service_"""
    url = "/api/v1/services/unbound/start"
    method = "POST"
    return self.call(url=url, method=method, payload=args)


def stop_unbound_service(self, **args) -> Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#5-stop-unbound-service_"""
    url = "/api/v1/services/unbound/stop"
    method = "POST"
    return self.call(url=url, method=method, payload=args)
