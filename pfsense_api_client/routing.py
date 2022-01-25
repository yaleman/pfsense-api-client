""" routing-related things """

import requests


def apply_routing(self, **args) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-apply-routing"""
    url = "/api/v1/routing/apply"
    method = "POST"
    return self.call(url=url, method=method, payload=args)


def create_routing_gateway(self, **args) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-routing-gateways"""
    url = "/api/v1/routing/gateway"
    method = "POST"
    return self.call(url=url, method=method, payload=args)


def delete_routing_gateway(self, **args) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-routing-gateways"""
    url = "/api/v1/routing/gateway"
    method = "DELETE"
    return self.call(url=url, method=method, payload=args)


def get_routing_gateway(self, *filterargs) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-read-routing-gateways"""

    url = "/api/v1/routing/gateway"
    return self.call(url, payload=filterargs)


def update_routing_gateway(self, **args) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-update-routing-gateways"""

    url = "/api/v1/routing/gateway"
    method = "PUT"
    return self.call(url=url, method=method, payload=args)


def get_routing_gateway_details(self, *filterargs) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-read-routing-gateway-details"""
    url = "/api/v1/routing/gateway/detail"
    return self.call(url, payload=filterargs)


def create_static_route(self, **args) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-static-routes"""
    url = "/api/v1/routing/static_route"
    method = "POST"
    return self.call(url=url, method=method, payload=args)


def delete_static_route(self, **args) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-static-routes"""
    url = "/api/v1/routing/static_route"
    method = "DELETE"
    return self.call(url=url, method=method, payload=args)


def get_static_route(self, *filterargs) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-read-static-routes"""
    url = "/api/v1/routing/static_route"
    return self.call(url, payload=filterargs)


def update_static_route(self, **args) -> requests.Response:
    """https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-update-static-routes"""
    url = "/api/v1/routing/static_route"
    method = "PUT"
    return self.call(url=url, method=method, payload=args)
