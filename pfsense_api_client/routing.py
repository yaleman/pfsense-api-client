""" routing-related things """

import requests

# TODO: url = "/api/v1/routing/apply"
# TODO: url = "/api/v1/routing/gateway"
# TODO: url = "/api/v1/routing/gateway/detail"
# TODO: url = "/api/v1/routing/static_route"


def apply_routing(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-apply-routing """

def create_routing_gateway(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-routing-gateways """

def delete_routing_gateway(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-routing-gateways """

def get_routing_gateway(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-read-routing-gateways """

def update_routing_gateway(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-update-routing-gateways """


def get_routing_gateway_details(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-read-routing-gateway-details """


def create_static_route(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-static-routes """

def delete_static_route(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-static-routes """

def get_static_route(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-read-static-routes """

def update_static_route(self, **args) -> requests.Response:
    """ https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-update-static-routes """
