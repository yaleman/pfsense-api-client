""" firewall-rule related things """

from enum import Enum
from typing import List, Union, Optional

import pydantic
import requests

__all__ = [
    'get_firewall_rule',
    "get_firewall_alias",
    "create_firewall_alias",
    "delete_firewall_alias",

]

class AliasTypes(str, Enum):
    """ types for firewall aliases """
    host = "host" # pylint: disable=invalid-name
    network = "network" # pylint: disable=invalid-name
    port = "port" # pylint: disable=invalid-name

def get_firewall_alias(self, **filterargs) -> requests.Response:
    """ get a list of firewall aliases
    https://github.com/jaredhendrickson13/pfsense-api#3-read-firewall-aliases
    """
    url = "/api/v1/firewall/alias"
    return self.call(url=url, payload=filterargs)

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
) -> requests.Response:
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
    name: str,
    apply: bool = True,
) -> requests.Response:
    """ Delete an existing alias and (optionally) reload filter.
https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-firewall-aliases

    field: id in the API is 'name' because 'id' is reserved in python.
    """
    url = "/api/v1/firewall/alias"
    method="DELETE"
    payload = { "id": name, "apply": apply}
    return self.call(url=url, method=method, payload=payload)


class FirewallAliasUpdate(pydantic.BaseModel):
    """ validating the firewall alias update """
    name: str
    type: AliasTypes
    descr: Optional[str]
    address: Union[str, List[str]]
    detail: Union[str, List[str]]
    apply: bool

@pydantic.validate_arguments()
def update_firewall_alias(self, *args: FirewallAliasUpdate) -> requests.Response:
    """Modify an existing firewall alias.

    https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-update-firewall-aliases
    """
    method = "PUT"
    url = "/api/v1/firewall/alias"

    payload = FirewallAliasUpdate(*args).dict()

    return self.call(url=url,method=method,payload=payload)

# TODO: def create_firewall_alias_entry(self, **filterargs) -> requests.Response:
# Add new entries to an existing firewall alias.
# https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-firewall-alias-entries

# method = "POST"
# url = "/api/v1/firewall/alias/entry"


# TODO: Delete Firewall Alias Entries

# Delete existing entries from an existing firewall alias.
# https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-firewall-alias-entries

# method = "DELETE"
# url = "/api/v1/firewall/alias/entry"

def apply_firewall_changes(self) -> requests.Response:
    """Apply pending firewall changes. This will reload all filter items. This endpoint returns no data.

    https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-apply-firewall
    """

    url = "/api/v1/firewall/apply"
    method = "POST"
    return self.call(url, method)


# create_firewall_nat_one_to_one
# Add a new NAT 1:1 Mapping.
# https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-nat-1-to-1-mappings
# method = "POST"
# url = "/api/v1/firewall/nat/one_to_one"

# delete_firewall_nat_one_to_one
# Delete a NAT 1:1 Mapping.
# https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-nat-1-to-1-mappings
# method = "DELETE"
# url = "/api/v1/firewall/nat/one_to_one"

# update_firewall_nat_one_to_one
# Update a NAT 1:1 Mapping.
# https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-update-nat-1-to-1-mappings
# method = "PUT"
# url = "/api/v1/firewall/nat/one_to_one"

def get_firewall_nat_one_to_one(self, **filterargs) -> requests.Response:
    """Read 1:1 NAT mappings.

    https://github.com/jaredhendrickson13/pfsense-api#3-read-nat-1-to-1-mappings
    """
    url = "/api/v1/firewall/nat/one_to_one"
    return self.call(url, payload=filterargs)

# TODO: def update_nat_outbound_settings(self, **filterargs) -> requests.Response:
# mode: str, apply: Optional[bool]
# Update outbound NAT mode settings.
# https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-update-outbound-nat-settings
# method = "PUT"
# url = "/api/v1/firewall/nat/outbound"


# TODO: def create_outbound_nat_mapping(self, **filterargs) -> requests.Response:
# Create new outbound NAT mappings.
# https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-outbound-nat-mappings
# method = "POST"
# url = "/api/v1/firewall/nat/outbound/mapping"

# TODO: def delete_outbound_nat_mapping(self, **filterargs) -> requests.Response:
# name: str
# apply: Optional[bool]
# Delete outbound NAT mappings.
# https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-outbound-nat-mappings
# method = "DELETE"
# url = "/api/v1/firewall/nat/outbound/mapping"


def get_nat_outbound_mapping(self, **filterargs) -> requests.Response:
    """Read existing outbound NAT mode mappings.

    https://github.com/jaredhendrickson13/pfsense-api#3-read-outbound-nat-mappings
    """
    url = "/api/v1/firewall/nat/outbound/mapping"
    return self.call(url, payload=filterargs)


# TODO: def update_outbound_nat_mapping(self, **filterargs) -> requests.Response:
# Update existing outbound NAT mappings.
# https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-update-outbound-nat-mappings
# method = "PUT"
# url = "/api/v1/firewall/nat/outbound/mapping"


# TODO: def create_nat_port_forward(self, **filterargs) -> requests.Response:
# Add a new NAT port forward rule.
# method = "POST"
# url = "/api/v1/firewall/nat/port_forward"

# TODO: def delete_nat_port_forward(self, **filterargs) -> requests.Response:
# name: str
# apply: Optional[bool]
# Delete a NAT port forward rule.
# https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-nat-port-forwards
# method = "DELETE"
# url = "/api/v1/firewall/nat/port_forward"


def get_firewall_nat_port_forward(self, **filterargs) -> requests.Response:
    """Read NAT port forward rules.

    https://github.com/jaredhendrickson13/pfsense-api#3-read-nat-port-forwards"""
    url = "/api/v1/firewall/nat/port_forward"
    return self.call(url, payload=filterargs)


# TODO: def update_nat_port_forward(self, **filterargs) -> requests.Response:
# Update a NAT port forward rule.
# https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-update-nat-port-forwards
# method = "PUT"
# url = "/api/v1/firewall/nat/port_forward"

# TODO: url = "/api/v1/firewall/nat/port_forward"

# pylint: disable=line-too-long
def delete_all_firewall_rules(self):
    """Deletes all existing firewall rules. This is useful for scripts that need to setup the firewall rules from scratch.

    Note: this endpoint will not reload the firewall filter automatically, you must make another API call to the /api/v1/firewall/apply endpoint to do so. Ensure firewall rules are created before reloading the filter to prevent lockout!.

    https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-delete-all-firewall-rules
"""
    url = "/api/v1/firewall/rule/flush"
    method = "DELETE"
    self.call(url=url, method=method)

# TODO: def create_firewall_schedule(self, **filterargs) -> requests.Response:
# Add a firewall schedule.
# https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-schedule
# method = "POST"
# url = "/api/v1/firewall/schedule"

# TODO: def delete_firewall_schedule(self, **filterargs) -> requests.Response:
# Delete a firewall schedule.
# https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-schedule
# method = "DELETE"
# url = "/api/v1/firewall/schedule"

def get_firewall_schedule(self, **filterargs) -> requests.Response:
    """Read all existing firewall schedules.


    """
    url = "/api/v1/firewall/schedule"
    return self.call(url, payload=filterargs)

# TODO: def update_firewall_schedule(self, **filterargs) -> requests.Response:
# Update a firewall schedule.
# https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-update-schedule
# method = "PUT"
# url = "/api/v1/firewall/schedule"

# TODO: def create_schedule_time_range(self, **filterargs) -> requests.Response:
#  Add a time range to an existing firewall schedule.
# https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-schedule-time-range
# method = "POST"
# url = "/api/v1/firewall/schedule/time_range"

# TODO: def delete_schedule_time_range(self, **filterargs) -> requests.Response:
#  Delete a time range from an existing firewall schedule.
# https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-schedule-time-range
# method = "DELETE"
# url = "/api/v1/firewall/schedule/time_range"

def get_firewall_states(self, **filterargs) -> requests.Response:
    """Read the current firewall states.

    https://github.com/jaredhendrickson13/pfsense-api#1-read-firewall-states
    """
    url = "/api/v1/firewall/states"
    return self.call(url, payload=filterargs)

def get_firewall_states_size(self, **filterargs) -> requests.Response:
    """Read the maximum firewall state size, the current firewall state size, and the default firewall state size.

    https://github.com/jaredhendrickson13/pfsense-api#1-read-firewall-state-size
    """
    url = "/api/v1/firewall/states/size"
    return self.call(url, payload=filterargs)


# TODO: def update_firewall_state_size(self, **filterargs) -> requests.Response:
# Modify the maximum number of firewall state table entries allowed by the system
# Note: use caution when making this call, setting the maximum state table size to a value lower than the current number of firewall state entries WILL choke the system
# https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-update-firewall-state-size

# TODO: Add a check for current states > state size and require the user to pass force=True if they want to bypass the state check
# method = "PUT"
# url = "/api/v1/firewall/states/size"


# TODO: def create_traffic_shaper(self, **filterargs) -> requests.Response:
# Add a traffic shaper policy to an interface.
# https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-traffic-shaper
# method = "POST"
# url = "/api/v1/firewall/traffic_shaper"

# TODO: def delete_traffic_shaper(self, **filterargs) -> requests.Response:
# Delete a traffic shaper policy from an interface.
# https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-traffic-shaper
# method = "DELETE"
# url = "/api/v1/firewall/traffic_shaper"


def get_traffic_shaper(self, **filterargs) -> requests.Response:
    """Read all configured traffic shapers.

    https://github.com/jaredhendrickson13/pfsense-api#3-read-traffic-shapers
    """
    url = "/api/v1/firewall/traffic_shaper"
    return self.call(url, payload=filterargs)

# TODO: def update_traffic_shaper(self, **filterargs) -> requests.Response:
# Update a traffic shaper policy for an interface.
# https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-update-traffic-shaper
# method = "PUT"
# url = "/api/v1/firewall/traffic_shaper"

# TODO: def create_traffic_shaper_limiter(self, **filterargs) -> requests.Response:
# Add a traffic shaper limiter.
# https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-limiter
# method = "POST"
# url = "/api/v1/firewall/traffic_shaper/limiter"

# TODO: def delete_traffic_shaper_limiter(self, **filterargs) -> requests.Response:
# Add a traffic shaper limiter.
# https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-limiter
# method = "POST"
# url = "/api/v1/firewall/traffic_shaper/limiter"

def get_traffic_shaper_limiter(self, **filterargs) -> requests.Response:
    """Get the traffic shaper limiters

    https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-read-limiters"""
    url = "/api/v1/firewall/traffic_shaper/limiter"
    return self.call(url, payload=filterargs)

# TODO: def create_limiter_bandwidth(self, **filterargs) -> requests.Response:
# Create a limiter bandwidth setting.
# https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-limiter-bandwidth
# method = "POST"
# url = "/api/v1/firewall/traffic_shaper/limiter/bandwidth"

# TODO: def delete_limiter_bandwidth(self, **filterargs) -> requests.Response:
# Delete a limiter bandwidth setting.
# https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-limiter-bandwidth
# method = "DELETE"
# url = "/api/v1/firewall/traffic_shaper/limiter/bandwidth"


# TODO: def create_limiter_queue(self, **filterargs) -> requests.Response:
# Add a child queue to an existing traffic shaper limiter
# https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-limiter-queue
# method = "POST"
# url = "/api/v1/firewall/traffic_shaper/limiter/queue"

# TODO: def delete_limiter_queue(self, **filterargs) -> requests.Response:
# Delete a child queue from an existing traffic shaper limiter
# https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-limiter-queue
# method = "DELETE"
# url = "/api/v1/firewall/traffic_shaper/limiter/queue"

# TODO: def create_firewall_rule(self, **filterargs) -> requests.Response:
# def create_firewall_rule(self, **args) -> requests.Response:
#     """ Create firewall rules

#     https://github.com/jaredhendrickson13/pfsense-api#3-read-firewall-rules
#     """
#     url = "/api/v1/firewall/rule"
#     method = "POST"
#     return self.call(url=url, payload=args)

# TODO: def delete_firewall_rule(self, **filterargs) -> requests.Response:
# def delete_firewall_rule(self, name: str, apply: Optional[bool]) -> requests.Response:
#     """ Delete firewall rules

#     https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-firewall-rules
#     """
#     url = "/api/v1/firewall/rule"
#     method = "DELETE"
#     return self.call(url=url, payload=args)

# TODO: def update_firewall_rule(self, **filterargs) -> requests.Response:
# def update_firewall_rule(self, name: str, apply: Optional[bool]) -> requests.Response:
#     """ Update firewall rules

#     https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-update-firewall-rules
#     """
#     url = "/api/v1/firewall/rule"
#     method = "PUT"
#     return self.call(url=url, payload=args)


def get_firewall_rule(self, **filterargs) -> requests.Response:
    """ Read firewall rules

    https://github.com/jaredhendrickson13/pfsense-api#3-read-firewall-rules
    """
    url = "/api/v1/firewall/rule"
    return self.call(url=url, payload=filterargs)


# TODO: def create_traffic_shaper_queue(self, **filterargs) -> requests.Response:
# Add a queue to an traffic shaper interface.
# https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-traffic-shaper-queue
# Method: POST
# URL: https://{{$hostname}}/api/v1/firewall/traffic_shaper/queue

# TODO: def delete_traffic_shaper_queue(self, **filterargs) -> requests.Response:
# Delete a queue from an traffic shaper interface.
# https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-traffic-shaper-queue
# Method: DELETE
# URL: https://{{$hostname}}/api/v1/firewall/traffic_shaper/queue


# TODO: def create_virtual_ip(self, **filterargs) -> requests.Response:
# Add a new virtual IP.
# https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-virtual-ips
# Method: POST
# URL: https://{{$hostname}}/api/v1/firewall/virtual_ip

# TODO: def delete_virtual_ip(self, **filterargs) -> requests.Response:
# Delete a virtual IP.
# https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-virtual-ips
# Method: DELETE
# URL: https://{{$hostname}}/api/v1/firewall/virtual_ip

def get_virtual_ip(self, **filterargs) -> requests.Response:
    """ Read virtual IP assignments.

    https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-read-virtual-ips"""
    return self.call("/api/v1/firewall/virtual_ip", payload=filterargs)

# TODO: def update_virtual_ip(self, **filterargs) -> requests.Response:
# Update a virtual IP.
# https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-update-virtual-ips
# Method: PUT
# URL: https://{{$hostname}}/api/v1/firewall/virtual_ip
