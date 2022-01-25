""" interface-related things """

import requests

def create_interfaces(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-interfaces """

def delete_interfaces(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-interfaces """

def get_interfaces(self, *filterargs) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-read-interfaces """
    url = ""
    return self.call(url, payload=filterargs)

def update_interfaces(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-update-interfaces """


def apply_interfaces(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-apply-interfaces """


def create_interface_bridges(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-interface-bridges """

def delete_interface_bridge(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-interface-bridges """

def get_interface_bridge(self, *filterargs) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-read-interface-bridges """
    url = ""
    return self.call(url, payload=filterargs)

def update_interface_bridge(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-update-interface-bridges """


def create_interface_vlan(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-interface-vlans """

def delete_interface_vlan(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-interface-vlans """

def get_interface_vlan(self, *filterargs) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-read-interface-vlans """
    url = ""
    return self.call(url, payload=filterargs)

def update_interface_vlan(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-update-interface-vlans """
