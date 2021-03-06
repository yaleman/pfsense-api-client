""" firewall-rule related things """

from enum import Enum
from typing import Any, Dict, List, Union, Optional

import pydantic
import requests

from .api_types import BasePFSenseAPIClient

__all__ = [
    "FirewallMixin",
    # "apply_firewall_changes",
    # "create_firewall_alias",
    # "create_firewall_alias_entry",
    # "create_firewall_nat_one_to_one",
    # "create_firewall_rule",
    # "create_firewall_schedule",
    # "create_limiter_bandwidth",
    # "create_limiter_queue",
    # "create_nat_port_forward",
    # "create_outbound_nat_mapping",
    # "create_schedule_time_range",
    # "create_traffic_shaper",
    # "create_traffic_shaper_limiter",
    # "create_traffic_shaper_queue",
    # "create_virtual_ip",
    # "delete_all_firewall_rules",
    # "delete_firewall_alias",
    # "delete_firewall_alias_entry",
    # "delete_firewall_nat_one_to_one",
    # "delete_firewall_rule",
    # "delete_firewall_schedule",
    # "delete_limiter_bandwidth",
    # "delete_limiter_queue",
    # "delete_nat_port_forward",
    # "delete_outbound_nat_mapping",
    # "delete_schedule_time_range",
    # "delete_traffic_shaper",
    # "delete_traffic_shaper_limiter",
    # "delete_traffic_shaper_queue",
    # "delete_virtual_ip",
    # "get_firewall_alias",
    # "get_firewall_nat_one_to_one",
    # "get_firewall_nat_port_forward",
    # "get_firewall_rule",
    # "get_firewall_schedule",
    # "get_firewall_states",
    # "get_firewall_states_size",
    # "get_nat_outbound_mapping",
    # "get_traffic_shaper",
    # "get_traffic_shaper_limiter",
    # "get_virtual_ip",
    # "update_firewall_alias",
    # "update_firewall_nat_one_to_one",
    # "update_firewall_rule",
    # "update_firewall_schedule",
    # "update_firewall_state_size",
    # "update_nat_outbound_settings",
    # "update_nat_port_forward",
    # "update_outbound_nat_mapping",
    # "update_traffic_shaper",
    # "update_virtual_ip",
]


class AliasTypes(str, Enum):
    """types for firewall aliases"""

    host = "host"  # pylint: disable=invalid-name
    network = "network"  # pylint: disable=invalid-name
    port = "port"  # pylint: disable=invalid-name



class FirewallAliasUpdate(pydantic.BaseModel):
    """validating the firewall alias update"""

    name: str
    type: AliasTypes
    descr: Optional[str]
    address: Union[str, List[str]]
    detail: Union[str, List[str]]
    apply: bool

#pylint: disable=too-many-public-methods
class FirewallMixin(BasePFSenseAPIClient):
    """ mixin class for firewall functions """

    def get_firewall_alias(
        self, **kwargs: Any
    ) -> requests.Response:
        """get a list of firewall aliases
        https://github.com/jaredhendrickson13/pfsense-api#3-read-firewall-aliases
        """
        url = "/api/v1/firewall/alias"
        return self.call(url=url, payload=dict(kwargs))


    # pylint: disable=too-many-arguments
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
        """Add a new host, network or port firewall alias.
        https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-firewall-aliases
        """
        url = "/api/v1/firewall/alias"
        method = "POST"
        payload = {}

        class FirewallAlias(pydantic.BaseModel):
            """validating the firewall alias"""

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
        """Delete an existing alias and (optionally) reload filter.
        https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-firewall-aliases

            field: id in the API is 'name' because 'id' is reserved in python.
        """
        url = "/api/v1/firewall/alias"
        method = "DELETE"
        payload = {"id": name, "apply": apply}
        return self.call(url=url, method=method, payload=payload)



    @pydantic.validate_arguments
    def update_firewall_alias(
        self, *args: FirewallAliasUpdate
    ) -> requests.Response:
        """Modify an existing firewall alias.

        https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-update-firewall-aliases
        """
        method = "PUT"
        url = "/api/v1/firewall/alias"

        payload = FirewallAliasUpdate(*args).dict()

        return self.call(url=url, method=method, payload=payload)


    def create_firewall_alias_entry(
        self, **args: Dict[str, Any]
    ) -> requests.Response:
        """Add new entries to an existing firewall alias.
        https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-firewall-alias-entries
        """

        method = "POST"
        url = "/api/v1/firewall/alias/entry"
        return self.call(url=url, method=method, payload=args)


    def delete_firewall_alias_entry(
        self, **args: Dict[str, Any]
    ) -> requests.Response:
        """Delete existing entries from an existing firewall alias.
        https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-firewall-alias-entries"""
        method = "DELETE"
        url = "/api/v1/firewall/alias/entry"
        return self.call(url=url, method=method, payload=args)


    def apply_firewall_changes(self) -> requests.Response:
        """Apply pending firewall changes. This will reload all filter items. This endpoint returns no data.

        https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-apply-firewall
        """

        url = "/api/v1/firewall/apply"
        method = "POST"
        return self.call(url, method)


    def create_firewall_nat_one_to_one(
        self, **args: Dict[str, Any]
    ) -> requests.Response:
        """Add a new NAT 1:1 Mapping.
        https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-nat-1-to-1-mappings"""
        method = "POST"
        url = "/api/v1/firewall/nat/one_to_one"
        return self.call(url=url, method=method, payload=args)


    def delete_firewall_nat_one_to_one(
        self, **args: Dict[str, Any]
    ) -> requests.Response:
        """Delete a NAT 1:1 Mapping.
        https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-nat-1-to-1-mappings"""
        method = "DELETE"
        url = "/api/v1/firewall/nat/one_to_one"
        return self.call(url=url, method=method, payload=args)


    def update_firewall_nat_one_to_one(
        self, **args: Dict[str, Any]
    ) -> requests.Response:
        """Update a NAT 1:1 Mapping.
        https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-update-nat-1-to-1-mappings"""
        method = "PUT"
        url = "/api/v1/firewall/nat/one_to_one"
        return self.call(url=url, method=method, payload=args)


    def get_firewall_nat_one_to_one(
        self, **kwargs: Dict[str, Any]
    ) -> requests.Response:
        """Read 1:1 NAT mappings.

        https://github.com/jaredhendrickson13/pfsense-api#3-read-nat-1-to-1-mappings
        """
        url = "/api/v1/firewall/nat/one_to_one"
        return self.call(url, payload=kwargs)


    def update_nat_outbound_settings(
        self, **args: Dict[str, Any]
    ) -> requests.Response:
        """mode: str, apply: Optional[bool]
        Update outbound NAT mode settings.
        https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-update-outbound-nat-settings"""
        method = "PUT"
        url = "/api/v1/firewall/nat/outbound"
        return self.call(url, method=method, payload=args)


    def create_outbound_nat_mapping(
        self, **args: Dict[str, Any]
    ) -> requests.Response:
        """Create new outbound NAT mappings.
        https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-outbound-nat-mappings"""
        method = "POST"
        url = "/api/v1/firewall/nat/outbound/mapping"
        return self.call(url, method=method, payload=args)


    def delete_outbound_nat_mapping(
        self, **args: Dict[str, Any]
    ) -> requests.Response:
        """name: str
        apply: Optional[bool]
        Delete outbound NAT mappings.
        https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-outbound-nat-mappings"""
        method = "DELETE"
        url = "/api/v1/firewall/nat/outbound/mapping"
        return self.call(url, method=method, payload=args)


    def get_nat_outbound_mapping(
        self, **kwargs: Dict[str, Any]
    ) -> requests.Response:
        """Read existing outbound NAT mode mappings.

        https://github.com/jaredhendrickson13/pfsense-api#3-read-outbound-nat-mappings
        """
        url = "/api/v1/firewall/nat/outbound/mapping"
        return self.call(url, payload=kwargs)


    def update_outbound_nat_mapping(
        self, **args: Dict[str, Any]
    ) -> requests.Response:
        """Update existing outbound NAT mappings.
        https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-update-outbound-nat-mappings"""
        method = "PUT"
        url = "/api/v1/firewall/nat/outbound/mapping"
        return self.call(url=url, method=method, payload=args)


    def create_nat_port_forward(
        self, **args: Dict[str, Any]
    ) -> requests.Response:
        """Add a new NAT port forward rule."""
        url = "/api/v1/firewall/nat/port_forward"
        method = "POST"
        return self.call(url=url, method=method, payload=args)


    def delete_nat_port_forward(
        self, **args: Dict[str, Any]
    ) -> requests.Response:
        """Delete a NAT port forward rule.
        https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-nat-port-forwards"""
        # name: str
        # apply: Optional[bool]
        url = "/api/v1/firewall/nat/port_forward"
        method = "DELETE"
        return self.call(url=url, method=method, payload=args)


    def get_firewall_nat_port_forward(
        self, **kwargs: Dict[str, Any]
    ) -> requests.Response:
        """Read NAT port forward rules.

        https://github.com/jaredhendrickson13/pfsense-api#3-read-nat-port-forwards"""
        url = "/api/v1/firewall/nat/port_forward"
        return self.call(url, payload=kwargs)


    def update_nat_port_forward(
        self, **args: Dict[str, Any]
    ) -> requests.Response:
        """Update a NAT port forward rule.
        https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-update-nat-port-forwards"""
        method = "PUT"
        url = "/api/v1/firewall/nat/port_forward"
        return self.call(url=url, method=method, payload=args)


    # pylint: disable=line-too-long
    def delete_all_firewall_rules(self) -> requests.Response:
        """Deletes all existing firewall rules. This is useful for scripts that need to setup the firewall rules from scratch.

        Note: this endpoint will not reload the firewall filter automatically, you must make another API call to the /api/v1/firewall/apply endpoint to do so. Ensure firewall rules are created before reloading the filter to prevent lockout!.

        https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-delete-all-firewall-rules"""
        url = "/api/v1/firewall/rule/flush"
        method = "DELETE"
        return self.call(url=url, method=method)


    def create_firewall_schedule(
        self, **args: Dict[str, Any]
    ) -> requests.Response:
        """Add a firewall schedule.
        https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-schedule"""
        url = "/api/v1/firewall/schedule"
        method = "POST"
        return self.call(url=url, method=method, payload=args)


    def delete_firewall_schedule(
        self, **args: Dict[str, Any]
    ) -> requests.Response:
        """Delete a firewall schedule.
        https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-schedule"""
        method = "DELETE"
        url = "/api/v1/firewall/schedule"
        return self.call(url=url, method=method, payload=args)


    def get_firewall_schedule(
        self, **kwargs: Dict[str, Any]
    ) -> requests.Response:
        """Read all existing firewall schedules."""
        url = "/api/v1/firewall/schedule"
        return self.call(url, payload=kwargs)


    def update_firewall_schedule(
        self, **args: Dict[str, Any]
    ) -> requests.Response:
        """Update a firewall schedule.
        https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-update-schedule"""
        method = "PUT"
        url = "/api/v1/firewall/schedule"
        return self.call(url=url, method=method, payload=args)


    def create_schedule_time_range(
        self, **args: Dict[str, Any]
    ) -> requests.Response:
        """Add a time range to an existing firewall schedule.
        https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-schedule-time-range"""
        method = "POST"
        url = "/api/v1/firewall/schedule/time_range"
        return self.call(url=url, method=method, payload=args)


    def delete_schedule_time_range(
        self, **args: Dict[str, Any]
    ) -> requests.Response:
        """Delete a time range from an existing firewall schedule.
        https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-schedule-time-range"""
        method = "DELETE"
        url = "/api/v1/firewall/schedule/time_range"
        return self.call(url=url, method=method, payload=args)


    def get_firewall_states(
        self, **kwargs: Dict[str, Any]
    ) -> requests.Response:
        """Read the current firewall states.

        https://github.com/jaredhendrickson13/pfsense-api#1-read-firewall-states
        """
        url = "/api/v1/firewall/states"
        return self.call(url, payload=kwargs)


    def get_firewall_states_size(
        self, **kwargs: Dict[str, Any]
    ) -> requests.Response:
        """Read the maximum firewall state size, the current firewall state size, and the default firewall state size.

        https://github.com/jaredhendrickson13/pfsense-api#1-read-firewall-state-size
        """
        url = "/api/v1/firewall/states/size"
        return self.call(url, payload=kwargs)


    def update_firewall_state_size(
        self, **args: Dict[str, Any]
    ) -> requests.Response:
        """Modify the maximum number of firewall state table entries allowed by the system
        Note: use caution when making this call, setting the maximum state table size to a value lower than the current number of firewall state entries WILL choke the system
        https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-update-firewall-state-size"""

        # TODO: Add a check for current states > state size and require the user to pass force=True if they want to bypass the state check
        method = "PUT"
        url = "/api/v1/firewall/states/size"
        return self.call(url=url, method=method, payload=args)


    def create_traffic_shaper(
        self, **args: Dict[str, Any]
    ) -> requests.Response:
        """Add a traffic shaper policy to an interface.
        https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-traffic-shaper"""
        method = "POST"
        url = "/api/v1/firewall/traffic_shaper"
        return self.call(url=url, method=method, payload=args)


    def delete_traffic_shaper(
        self, **args: Dict[str, Any]
    ) -> requests.Response:
        """Delete a traffic shaper policy from an interface.
        https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-traffic-shaper"""
        method = "DELETE"
        url = "/api/v1/firewall/traffic_shaper"
        return self.call(url=url, method=method, payload=args)


    def get_traffic_shaper(
        self, **kwargs: Dict[str, Any]
    ) -> requests.Response:
        """Read all configured traffic shapers.

        https://github.com/jaredhendrickson13/pfsense-api#3-read-traffic-shapers
        """
        url = "/api/v1/firewall/traffic_shaper"
        return self.call(url, payload=kwargs)


    def update_traffic_shaper(
        self, **args: Dict[str, Any]
    ) -> requests.Response:
        """Update a traffic shaper policy for an interface.
        https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-update-traffic-shaper"""
        url = "/api/v1/firewall/traffic_shaper"
        method = "PUT"
        return self.call(url=url, method=method, payload=args)


    def create_traffic_shaper_limiter(
        self, **args: Dict[str, Any]
    ) -> requests.Response:
        """Add a traffic shaper limiter.
        https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-limiter"""
        url = "/api/v1/firewall/traffic_shaper/limiter"
        method = "POST"
        return self.call(url=url, method=method, payload=args)


    def delete_traffic_shaper_limiter(
        self, **args: Dict[str, Any]
    ) -> requests.Response:
        """Add a traffic shaper limiter.
        https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-limiter"""
        method = "POST"
        url = "/api/v1/firewall/traffic_shaper/limiter"
        return self.call(url=url, method=method, payload=args)


    def get_traffic_shaper_limiter(
        self, **kwargs: Dict[str, Any]
    ) -> requests.Response:
        """Get the traffic shaper limiters

        https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-read-limiters"""
        url = "/api/v1/firewall/traffic_shaper/limiter"
        return self.call(url, payload=kwargs)


    def create_limiter_bandwidth(
        self, **args: Dict[str, Any]
    ) -> requests.Response:
        """Create a limiter bandwidth setting.
        https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-limiter-bandwidth"""
        method = "POST"
        url = "/api/v1/firewall/traffic_shaper/limiter/bandwidth"
        return self.call(url=url, method=method, payload=args)


    def delete_limiter_bandwidth(
        self, **args: Dict[str, Any]
    ) -> requests.Response:
        """Delete a limiter bandwidth setting.
        https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-limiter-bandwidth"""
        method = "DELETE"
        url = "/api/v1/firewall/traffic_shaper/limiter/bandwidth"
        return self.call(url=url, method=method, payload=args)


    def create_limiter_queue(
        self, **args: Dict[str, Any]
    ) -> requests.Response:
        """Add a child queue to an existing traffic shaper limiter
        https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-limiter-queue"""
        method = "POST"
        url = "/api/v1/firewall/traffic_shaper/limiter/queue"
        return self.call(url=url, method=method, payload=args)


    def delete_limiter_queue(
        self, **args: Dict[str, Any]
    ) -> requests.Response:
        """Delete a child queue from an existing traffic shaper limiter
        https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-limiter-queue"""
        method = "DELETE"
        url = "/api/v1/firewall/traffic_shaper/limiter/queue"
        return self.call(url, method=method, payload=args)


    def create_firewall_rule(
        self, **args: Dict[str, Any]
    ) -> requests.Response:
        """Create firewall rules

        https://github.com/jaredhendrickson13/pfsense-api#3-read-firewall-rules"""
        url = "/api/v1/firewall/rule"
        method = "POST"
        return self.call(url=url, method=method, payload=args)


    @pydantic.validate_arguments
    def delete_firewall_rule(
        self, name: str, apply: Optional[bool]
    ) -> requests.Response:
        """Delete firewall rules

        https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-firewall-rules
        """
        url = "/api/v1/firewall/rule"
        method = "DELETE"

        payload: Dict[str, Union[str, bool]] = {"name": name}
        if apply:
            payload["apply"] = apply
        return self.call(url=url, method=method, payload=payload)


    def update_firewall_rule(
        self, **args: Dict[str, Any]
    ) -> requests.Response:
        """Update firewall rules

        https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-update-firewall-rules
        """
        url = "/api/v1/firewall/rule"
        method = "PUT"
        return self.call(url=url, method=method, payload=args)


    def get_firewall_rule(
        self, **kwargs: Optional[Any]
    ) -> requests.Response:
        """Read firewall rules

        https://github.com/jaredhendrickson13/pfsense-api#3-read-firewall-rules
        """
        url = "/api/v1/firewall/rule"
        return self.call(url=url, payload=kwargs)


    def create_traffic_shaper_queue(
        self, **args: Dict[str, Any]
    ) -> requests.Response:
        """Add a queue to an traffic shaper interface.
        https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-traffic-shaper-queue"""
        method = "POST"
        url = "https://{{$hostname}}/api/v1/firewall/traffic_shaper/queue"
        return self.call(url=url, method=method, payload=args)


    def delete_traffic_shaper_queue(
        self, **args: Dict[str, Any]
    ) -> requests.Response:
        """Delete a queue from an traffic shaper interface.
        https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-traffic-shaper-queue"""
        method = "DELETE"
        url = "https://{{$hostname}}/api/v1/firewall/traffic_shaper/queue"
        return self.call(url=url, method=method, payload=args)


    def create_virtual_ip(
        self, **args: Dict[str, Any]
    ) -> requests.Response:
        """Add a new virtual IP.
        https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-create-virtual-ips"""
        method = "POST"
        url = "https://{{$hostname}}/api/v1/firewall/virtual_ip"
        return self.call(url=url, method=method, payload=args)


    def delete_virtual_ip(
        self, **args: Dict[str, Any]
    ) -> requests.Response:
        """Delete a virtual IP.
        https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#2-delete-virtual-ips"""
        method = "DELETE"
        url = "https://{{$hostname}}/api/v1/firewall/virtual_ip"
        return self.call(url=url, method=method, payload=args)


    def get_virtual_ip(
        self, **kwargs: Dict[str, Any]
    ) -> requests.Response:
        """Read virtual IP assignments.

        https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#3-read-virtual-ips"""
        return self.call("/api/v1/firewall/virtual_ip", payload=kwargs)


    def update_virtual_ip(
        self, **args: Dict[str, Any]
    ) -> requests.Response:
        """Update a virtual IP.
        https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#4-update-virtual-ips"""
        method = "PUT"
        url = "https://{{$hostname}}/api/v1/firewall/virtual_ip"
        return self.call(url=url, method=method, payload=args)
