""" status-related endpoints """
import requests


def get_carp_status(self, *filterargs) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-read-carp-status """
    url = ""
    return self.call(url, payload=filterargs)

def update_carp_status(self, *filterargs) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-update-carp-status """
    url = ""
    return self.call(url, payload=filterargs)


def get_gateway_status(self, *filterargs) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-read-gateway-status """
    url = ""
    return self.call(url, payload=filterargs)


def get_interface_status(self, *filterargs) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-read-interface-status """
    url = ""
    return self.call(url, payload=filterargs)


def get_configuration_history_status_log(self, **filterargs) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-read-configuration-history-status-log """
    url = ""
    return self.call(url, payload=filterargs)

def get_dhcp_status_log(self, *filterargs) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-read-dhcp-status-log """
    url = ""
    return self.call(url, payload=filterargs)

def get_firewall_status_log(self, *filterargs) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-read-firewall-status-log """
    url = ""
    return self.call(url, payload=filterargs)

def get_system_status_log(self, *filterargs) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-read-system-status-log """
    url = ""
    return self.call(url, payload=filterargs)


def get_openvpn_status(self, *filterargs) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-read-openvpn-status """
    url = ""
    return self.call(url, payload=filterargs)


def get_system_status(self, *filterargs) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-read-system-status """
    url = ""
    return self.call(url, payload=filterargs)
