""" system_service_things """

import requests


def get_service(self, *filterargs) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-read-services """
    url = "/api/v1/services"
    return self.call(url, payload=filterargs)

def restart_all_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-restart-all-services """
    url="/api/v1/services/restart"
    method = "POST"
    return self.call(url=url, method=method, payload=args)

def start_all_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-start-all-services """
    url="/api/v1/services/start"
    method = "POST"
    return self.call(url=url, method=method, payload=args)

def stop_all_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-stop-all-services """
    url="/api/v1/services/stop"
    method = "POST"
    return self.call(url=url, method=method, payload=args)


def get_dynamic_dns(self, *filterargs) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-read-dynamic-dns """
    url = "/api/v1/services/ddns"
    return self.call(url, payload=filterargs)


def get_dhcpd_service_configuration(self, *filterargs) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-read-dhcpd-service-configuration """
    url = "/api/v1/services/dhcpd"
    return self.call(url, payload=filterargs)

def restart_dhcpd_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-restart-dhcpd-service_"""
    url="/api/v1/services/dhcpd/restart"
    method = "POST"
    return self.call(url=url, method=method, payload=args)

def start_dhcpd_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-start-dhcpd-service_"""
    url="/api/v1/services/dhcpd/start"
    method = "POST"
    return self.call(url=url, method=method, payload=args)

def stop_dhcpd_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-stop-dhcpd-service_"""
    url="/api/v1/services/dhcpd/stop"
    method = "POST"
    return self.call(url=url, method=method, payload=args)

def update_dhcpd_service_configuration(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#5-update-dhcpd-service-configuration """
    url="/api/v1/services/dhcpd"
    method = "PUT"
    return self.call(url=url, method=method, payload=args)


def get_dhcpd_leases(self, *filterargs) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-read-dhcpd-leases """
    url = "/api/v1/services/dhcp/lease"
    return self.call(url, payload=filterargs)


def create_dhcpd_static_mappings(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-dhcpd-static-mappings """
    url="/api/v1/services/dhcpd/static_mapping"
    method = "POST"
    return self.call(url=url, method=method, payload=args)


def delete_dhcpd_static_mappings(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-dhcpd-static-mappings """
    url="/api/v1/services/dhcpd/static_mapping"
    method = "DELETE"
    return self.call(url=url, method=method, payload=args)


def get_dhcpd_static_mappings(self, *filterargs) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-read-dhcpd-static-mappings """
    url="/api/v1/services/dhcpd/static_mapping"
    return self.call(url, payload=filterargs)

def update_dhcpd_static_mappings(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-update-dhcpd-static-mappings """
    url="/api/v1/services/dhcpd/static_mapping"
    method = "PUT"
    return self.call(url=url, method=method, payload=args)

def apply_pending_dnsmasq_changes(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-apply-pending-dnsmasq-changes """
    url="/api/v1/services/dnsmasq/apply"
    method = "POST"
    return self.call(url=url, method=method, payload=args)

def get_dnsmasq_configuration(self, *filterargs) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-read-dnsmasq-configuration """
    url = "/api/v1/services/dnsmasq"
    return self.call(url, payload=filterargs)

def restart_dnsmasq_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-restart-dnsmasq-service_"""
    url="/api/v1/services/dnsmasq/restart"
    method = "POST"
    return self.call(url=url, method=method, payload=args)

def start_dnsmasq_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-start-dnsmasq-service_"""
    url="/api/v1/services/dnsmasq/start"
    method = "POST"
    return self.call(url=url, method=method, payload=args)

def stop_dnsmasq_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#5-stop-dnsmasq-service_"""
    url="/api/v1/services/dnsmasq/stop"
    method = "POST"
    return self.call(url=url, method=method, payload=args)


def create_dnsmasq_host_override(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-dnsmasq-host-override """
    url="/api/v1/services/dnsmasq/host_override"
    method = "POST"
    return self.call(url=url, method=method, payload=args)

def delete_dnsmasq_host_override(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-dnsmasq-host-override """
    url="/api/v1/services/dnsmasq/host_override"
    method = "DELETE"
    return self.call(url=url, method=method, payload=args)

def get_dnsmasq_host_override(self, *filterargs) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-read-dnsmasq-host-override """
    url="/api/v1/services/dnsmasq/host_override"
    return self.call(url, payload=filterargs)

def update_dnsmasq_host_override(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-update-dnsmasq-host-override """
    url="/api/v1/services/dnsmasq/host_override"
    method = "PUT"
    return self.call(url=url, method=method, payload=args)

def create_dnsmasq_host_override_alias(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-dnsmasq-host-override-alias """
    url="/api/v1/services/dnsmasq/host_override/alias"
    method = "POST"
    return self.call(url=url, method=method, payload=args)


def restart_dpinger_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-restart-dpinger-service_"""
    url="/api/v1/services/dpinger/restart"
    method = "POST"
    return self.call(url=url, method=method, payload=args)

def start_dpinger_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-start-dpinger-service_"""
    url="/api/v1/services/dpinger/start"
    method = "POST"
    return self.call(url=url, method=method, payload=args)

def stop_dpinger_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-stop-dpinger-service_"""
    url="/api/v1/services/dpinger/stop"
    method = "POST"
    return self.call(url=url, method=method, payload=args)

def get_ntpd_service(self, *filterargs) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-read-ntpd-service_"""
    url = "/api/v1/services/ntpd"
    return self.call(url, payload=filterargs)

def restart_ntpd_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-restart-ntpd-service_"""
    url="/api/v1/services/ntpd/restart"
    method = "POST"
    return self.call(url=url, method=method, payload=args)

def start_ntpd_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-start-ntpd-service_"""
    url="/api/v1/services/ntpd/start"
    method = "POST"
    return self.call(url=url, method=method, payload=args)

def stop_ntpd_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-stop-ntpd-service_"""
    url="/api/v1/services/ntpd/stop"
    method = "POST"
    return self.call(url=url, method=method, payload=args)

def update_ntpd_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#5-update-ntpd-service_"""
    url="/api/v1/services/ntpd"
    method = "PUT"
    return self.call(url=url, method=method, payload=args)


def create_ntpd_time_server(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-ntpd-time-server """
    url="/api/v1/services/ntpd/time_server"
    method = "POST"
    return self.call(url=url, method=method, payload=args)

def delete_ntpd_time_server(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-ntpd-time-server """
    url="/api/v1/services/ntpd/time_server"
    method = "DELETE"
    return self.call(url=url, method=method, payload=args)


def create_openvpn_client_specific_overrides(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-openvpn-client-specific-overrides """
    url="/api/v1/services/openvpn/csc"
    method = "POST"
    return self.call(url=url, method=method, payload=args)

def delete_openvpn_client_specific_override(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-openvpn-client-specific-override """
    url="/api/v1/services/openvpn/csc"
    method = "DELETE"
    return self.call(url=url, method=method, payload=args)

def get_openvpn_client_specific_overrides(self, *filterargs) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-read-openvpn-client-specific-overrides """
    url="/api/v1/services/openvpn/csc"
    return self.call(url, payload=filterargs)

def update_openvpn_client_specific_overrides(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-update-openvpn-client-specific-overrides """
    url="/api/v1/services/openvpn/csc"
    method = "PUT"
    return self.call(url=url, method=method, payload=args)


def get_sshd_configuration(self, *filterargs) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-read-sshd-configuration """
    url = "/api/v1/services/sshd"
    return self.call(url, payload=filterargs)

def restart_sshd_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-restart-sshd-service_"""
    url = "/api/v1/services/sshd/restart"
    method = "POST"
    return self.call(url=url, method=method, payload=args)

def start_sshd_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-start-sshd-service_"""
    url = "/api/v1/services/sshd/start"
    method = "POST"
    return self.call(url=url, method=method, payload=args)

def stop_sshd_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-stop-sshd-service_"""
    url = "/api/v1/services/sshd/stop"
    method = "POST"
    return self.call(url=url, method=method, payload=args)

def update_sshd_configuration(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#5-update-sshd-configuration """
    url = "/api/v1/services/sshd"
    method = "PUT"
    return self.call(url=url, method=method, payload=args)


def restart_syslogd_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-restart-syslogd-service_"""
    url = "/api/v1/services/syslogd/restart"
    method = "POST"
    return self.call(url=url, method=method, payload=args)

def start_syslogd_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-start-syslogd-service_"""
    url = "/api/v1/services/syslogd/start"
    method = "POST"
    return self.call(url=url, method=method, payload=args)

def stop_syslogd_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-stop-syslogd-service_"""
    url = "/api/v1/services/syslogd/stop"
    method = "POST"
    return self.call(url=url, method=method, payload=args)


def apply_pending_unbound_changes(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-apply-pending-unbound-changes """
    url = "/api/v1/services/unbound/apply"
    method = "POST"
    return self.call(url=url, method=method, payload=args)

def get_unbound_configuration(self, *filterargs) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-read-unbound-configuration """
    url = "/api/v1/services/unbound"
    return self.call(url, payload=filterargs)

def restart_unbound_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-restart-unbound-service_"""
    url = "/api/v1/services/unbound/restart"
    method = "POST"
    return self.call(url=url, method=method, payload=args)

def start_unbound_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-start-unbound-service_"""
    url = "/api/v1/services/unbound/start"
    method = "POST"
    return self.call(url=url, method=method, payload=args)

def stop_unbound_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#5-stop-unbound-service_"""
    url = "/api/v1/services/unbound/stop"
    method = "POST"
    return self.call(url=url, method=method, payload=args)


def create_unbound_access_list(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-unbound-access-list """
    url = "/api/v1/services/unbound/access_list"
    method = "POST"
    return self.call(url=url, method=method, payload=args)

def delete_unbound_access_list(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-unbound-access-list """
    url = "/api/v1/services/unbound/access_list"
    method = "DELETE"
    return self.call(url=url, method=method, payload=args)

def get_unbound_access_lists(self, *filterargs) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-read-unbound-access-lists """
    url = "/api/v1/services/unbound/access_list"
    return self.call(url, payload=filterargs)

def update_unbound_access_list(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-update-unbound-access-list """
    url = "/api/v1/services/unbound/access_list"
    method = "PUT"
    return self.call(url=url, method=method, payload=args)


def create_unbound_access_list_row(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-unbound-access-list-row """
    url = "/api/v1/services/unbound/access_list/row"
    method = "POST"
    return self.call(url=url, method=method, payload=args)


def create_unbound_host_override(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-unbound-host-override """
    url = "/api/v1/services/unbound/host_override"
    method = "POST"
    return self.call(url=url, method=method, payload=args)

def delete_unbound_host_override(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-unbound-host-override """
    url = "/api/v1/services/unbound/host_override"
    method = "DELETE"
    return self.call(url=url, method=method, payload=args)

def get_unbound_host_override(self, *filterargs) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-read-unbound-host-override """
    url = "/api/v1/services/unbound/host_override"
    return self.call(url, payload=filterargs)

def update_unbound_host_override(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-update-unbound-host-override """
    url = "/api/v1/services/unbound/host_override"
    method = "PUT"
    return self.call(url=url, method=method, payload=args)


def create_unbound_host_override_alias(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-unbound-host-override-alias """
    url = "/api/v1/services/unbound/host_override/alias"
    method = "POST"
    return self.call(url=url, method=method, payload=args)
