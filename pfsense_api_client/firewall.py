""" firewall-rule related things """

from enum import Enum
from typing import List, Union

import pydantic

__all__ = [
    'get_firewall_rules',
]


class AliasTypes(str, Enum):
    """ types for firewall aliases """
    host = "host" # pylint: disable=invalid-name
    network = "network" # pylint: disable=invalid-name
    port = "port" # pylint: disable=invalid-name

def get_firewall_alias(self):
    """ get a list of firewall aliases
    https://github.com/jaredhendrickson13/pfsense-api#3-read-firewall-aliases
    """
    # TODO: support filtering
    method="GET"
    url = "/api/v1/firewall/alias"
    return self.call(url=url, method=method)

#pylint: disable=too-many-arguments
@pydantic.validate_arguments()
def create_firewall_alias(
    self,
    name: str,
    alias_type: str,
    descr: str,
    address: Union[str, List[str]],
    detail: Union[str, List[str]],
    apply: bool = True,
):
    """ Add a new host, network or port firewall alias.
https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-firewall-aliases
    """
    url = "/api/v1/firewall/alias"
    method="POST"
    payload = {}

    class FirewallAlias(pydantic.BaseModel):
        """ validating the firewall alias """
        name: str
        type: AliasTypes
        descr: str
        address: Union[str, List[str]]
        detail: Union[str, List[str]]
        apply: bool

    payload = FirewallAlias(
        name=name,
        type=alias_type,
        descr=descr,
        address=address,
        detail=detail,
        apply=apply,
    ).dict()

    return self.call(
        url=url,
        method=method,
        payload=payload,
        )

@pydantic.validate_arguments()
def delete_firewall_alias(
    self,
    alias_id: str,
    apply: bool = True,
):
    """ Delete an existing alias and (optionally) reload filter.
https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-firewall-aliases
    """
    url = "/api/v1/firewall/alias"
    method="DELETE"
    payload = { "id": alias_id, "apply": apply}
    return self.call(url=url, method=method, payload=payload)

# TODO: url = "/api/v1/firewall/alias/entry"
# TODO: url = "/api/v1/firewall/apply"
# TODO: url = "/api/v1/firewall/nat/one_to_one"
# TODO: url = "/api/v1/firewall/nat/outbound"
# TODO: url = "/api/v1/firewall/nat/outbound/mapping"
# TODO: url = "/api/v1/firewall/nat/port_forward"
# TODO: url = "/api/v1/firewall/rule/flush"
# TODO: url = "/api/v1/firewall/schedule"
# TODO: url = "/api/v1/firewall/schedule/time_range"
# TODO: url = "/api/v1/firewall/states"
# TODO: url = "/api/v1/firewall/states/size"
# TODO: url = "/api/v1/firewall/traffic_shaper"
# TODO: url = "/api/v1/firewall/traffic_shaper/limiter"
# TODO: url = "/api/v1/firewall/traffic_shaper/limiter/bandwidth"
# TODO: url = "/api/v1/firewall/traffic_shaper/limiter/queue"
# TODO: url = "/api/v1/firewall/traffic_shaper/queue"
# TODO: url = "/api/v1/firewall/virtual_ip"

def get_firewall_rules(self,
    ):
    """ gets the firewall rules

    https://github.com/jaredhendrickson13/pfsense-api#3-read-firewall-rules
    """
    url = "/api/v1/firewall/rule"
    method = "GET"
    results = self.call(url=url, method=method)

    return results
