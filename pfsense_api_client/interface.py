""" interface-related things """

import requests

def create_interfaces(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-interfaces """
    url = "/api/v1/interface"
    method = "POST"
    return self.call(url=url, method=method, payload=args)

def delete_interfaces(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-interfaces """
    url = "/api/v1/interface"
    method = "DELETE"
    return self.call(url=url, method=method, payload=args)

def get_interfaces(self, *filterargs) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-read-interfaces """
    url = "/api/v1/interface"
    return self.call(url, payload=filterargs)

def update_interfaces(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-update-interfaces """
    url = "/api/v1/interface"
    method = "PUT"
    return self.call(url=url, method=method, payload=args)

def apply_interfaces(self) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-apply-interfaces """
    url = "/api/v1/interface/apply"
    method = "POST"
    return self.call(url=url, method=method)

def create_interface_bridges(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-interface-bridges """
    url = "/api/v1/interface/bridge"
    method = "POST"
    return self.call(url=url, method=method, payload=args)

def delete_interface_bridge(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-interface-bridges """
    url = "/api/v1/interface/bridge"
    method = "DELETE"
    return self.call(url=url, method=method, payload=args)

def get_interface_bridge(self, *filterargs) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-read-interface-bridges """
    url = "/api/v1/interface/bridge"
    return self.call(url, payload=filterargs)

def update_interface_bridge(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-update-interface-bridges """
    url = "/api/v1/interface/bridge"
    method = "PUT"
    return self.call(url=url, method=method, payload=args)


def create_interface_vlan(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-interface-vlans """
    url = "/api/v1/interface/vlan"
    method = "POST"
    return self.call(url=url, method=method, payload=args)

def delete_interface_vlan(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-interface-vlans """
    url = "/api/v1/interface/vlan"
    method = "DELETE"
    return self.call(url=url, method=method, payload=args)

def get_interface_vlan(self, *filterargs) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-read-interface-vlans """
    url = "/api/v1/interface/vlan"
    return self.call(url, payload=filterargs)

def update_interface_vlan(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-update-interface-vlans """
    url = "/api/v1/interface/vlan"
    method = "PUT"
    return self.call(url=url, method=method, payload=args)
