""" system_service_things """

import requests


def get_service(self, *filterargs) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-read-services """
    url = ""
    return self.call(url, payload=filterargs)

def restart_all_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-restart-all-services """

def start_all_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-start-all-services """

def stop_all_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-stop-all-services """


def get_dynamic_dns(self, *filterargs) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-read-dynamic-dns """
    url = ""
    return self.call(url, payload=filterargs)


def get_dhcpd_service_configuration(self, *filterargs) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-read-dhcpd-service-configuration """
    url = ""
    return self.call(url, payload=filterargs)

def restart_dhcpd_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-restart-dhcpd-service_"""

def start_dhcpd_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-start-dhcpd-service_"""

def stop_dhcpd_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-stop-dhcpd-service_"""

def update_dhcpd_service_configuration(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#5-update-dhcpd-service-configuration """


def get_dhcpd_leases(self, *filterargs) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-read-dhcpd-leases """
    url = ""
    return self.call(url, payload=filterargs)


def create_dhcpd_static_mappings(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-dhcpd-static-mappings """

def delete_dhcpd_static_mappings(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-dhcpd-static-mappings """

def get_dhcpd_static_mappings(self, *filterargs) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-read-dhcpd-static-mappings """
    url = ""
    return self.call(url, payload=filterargs)

def update_dhcpd_static_mappings(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-update-dhcpd-static-mappings """


def apply_pending_dnsmasq_changes(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-apply-pending-dnsmasq-changes """

def get_dnsmasq_configuration(self, *filterargs) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-read-dnsmasq-configuration """
    url = ""
    return self.call(url, payload=filterargs)

def restart_dnsmasq_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-restart-dnsmasq-service_"""

def start_dnsmasq_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-start-dnsmasq-service_"""

def stop_dnsmasq_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#5-stop-dnsmasq-service_"""


def create_dnsmasq_host_override(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-dnsmasq-host-override """

def delete_dnsmasq_host_override(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-dnsmasq-host-override """

def get_dnsmasq_host_override(self, *filterargs) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-read-dnsmasq-host-override """
    url = ""
    return self.call(url, payload=filterargs)

def update_dnsmasq_host_override(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-update-dnsmasq-host-override """


def create_dnsmasq_host_override_alias(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-dnsmasq-host-override-alias """


def restart_dpinger_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-restart-dpinger-service_"""

def start_dpinger_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-start-dpinger-service_"""

def stop_dpinger_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-stop-dpinger-service_"""

def get_ntpd_service(self, *filterargs) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-read-ntpd-service_"""
    url = ""
    return self.call(url, payload=filterargs)

def restart_ntpd_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-restart-ntpd-service_"""

def start_ntpd_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-start-ntpd-service_"""

def stop_ntpd_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-stop-ntpd-service_"""

def update_ntpd_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#5-update-ntpd-service_"""


def create_ntpd_time_server(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-ntpd-time-server """

def delete_ntpd_time_server(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-ntpd-time-server """


def create_openvpn_client_specific_overrides(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-openvpn-client-specific-overrides """

def delete_openvpn_client_specific_override(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-openvpn-client-specific-override """

def get_openvpn_client_specific_overrides(self, *filterargs) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-read-openvpn-client-specific-overrides """
    url = ""
    return self.call(url, payload=filterargs)

def update_openvpn_client_specific_overrides(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-update-openvpn-client-specific-overrides """


def get_sshd_configuration(self, *filterargs) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-read-sshd-configuration """
    url = ""
    return self.call(url, payload=filterargs)

def restart_sshd_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-restart-sshd-service_"""

def start_sshd_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-start-sshd-service_"""

def stop_sshd_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-stop-sshd-service_"""

def update_sshd_configuration(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#5-update-sshd-configuration """


def restart_syslogd_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-restart-syslogd-service_"""

def start_syslogd_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-start-syslogd-service_"""

def stop_syslogd_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-stop-syslogd-service_"""


def apply_pending_unbound_changes(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-apply-pending-unbound-changes """

def get_unbound_configuration(self, *filterargs) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-read-unbound-configuration """
    url = ""
    return self.call(url, payload=filterargs)

def restart_unbound_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-restart-unbound-service_"""

def start_unbound_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-start-unbound-service_"""

def stop_unbound_service(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#5-stop-unbound-service_"""


def create_unbound_access_list(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-unbound-access-list """

def delete_unbound_access_list(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-unbound-access-list """

def get_unbound_access_lists(self, *filterargs) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-read-unbound-access-lists """
    url = ""
    return self.call(url, payload=filterargs)

def update_unbound_access_list(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-update-unbound-access-list """


def create_unbound_access_list_row(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-unbound-access-list-row """


def create_unbound_host_override(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-unbound-host-override """

def delete_unbound_host_override(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-unbound-host-override """

def get_unbound_host_override(self, *filterargs) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-read-unbound-host-override """
    url = ""
    return self.call(url, payload=filterargs)

def update_unbound_host_override(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-update-unbound-host-override """


def create_unbound_host_override_alias(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-unbound-host-override-alias """
