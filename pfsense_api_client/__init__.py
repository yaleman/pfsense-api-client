""" pfSense API client """

import json

import os.path

from pathlib import Path
from typing import Any, Dict, Optional

from pydantic import BaseModel, validate_arguments
import requests

from .constants import RESPONSE_CODES
from . import firewall
from . import system

__all__ = [
    "PFSenseAPIClient",
]


class PFSenseConfig(BaseModel):
    """This sets up the right typing from the config file"""

    username: str
    password: str
    port: int
    hostname: str
    mode: Optional[str]


class PFSenseAPIClient:
    """pfSense API Client"""

    # pylint: disable=too-many-arguments
    def __init__(
        self,
        username: Optional[str] = None,
        password: Optional[str] = None,
        hostname: Optional[str] = None,
        port: Optional[int] = None,
        config_filename: Optional[str] = None,
        mode: Optional[str] = None,
    ):

        if username:
            self.username = username
        if password:
            self.password = password
        if hostname:
            self.hostname = hostname
        if port:
            self.port = port
        if mode:
            self.mode = mode
        else:
            self.mode = "local"

        if config_filename:
            self.config_filename = Path(os.path.expanduser(config_filename))
            if not self.config_filename.exists():
                error = f"Filename {self.config_filename.as_posix()} does not exist."
                raise FileNotFoundError(error)
            pydantic_config = PFSenseConfig(
                **json.load(self.config_filename.open(encoding="utf8"))
            )
            self.hostname = pydantic_config.hostname
            self.username = pydantic_config.username
            self.password = pydantic_config.password
            self.port = pydantic_config.port
            self.mode = pydantic_config.mode or "local"

        self.baseurl = f"https://{self.hostname}"
        if hasattr(self, "port"):
            self.baseurl += f":{self.port}"

    @validate_arguments
    def call(
        self,
        url: str,
        method: Optional[str] = None,
        payload: Dict[str, Any] = None,
    ) -> requests.Response:
        """makes an API call"""
        call_url = f"{self.baseurl}{url}"

        # print(f"mode: {self.mode}")
        if self.mode == "local":
            # this is the default
            if not payload:
                payload = {"client-id": self.username, "client-token": self.password}
            else:
                payload["client-id"] = self.username
                payload["client-token"] = self.password
        else:
            raise NotImplementedError("JWT and Access Token aren't implemented yet.")

        if method is None:
            method = "GET"
        # print(f"calling {call_url} {method}")
        # print(f"payload: {payload}")
        if method == "GET":
            response = requests.get(url=call_url, params=payload)
        elif method == "POST":
            response = requests.post(url=call_url, data=json.dumps(payload))
        else:
            response = requests.request(
                method=method, url=call_url, data=json.dumps(payload)
            )
        response.raise_for_status()
        return response

    def request_access_token(self):
        """gets a temporary access token
        https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-request-access-token
        """
        url = "/api/v1/access_token"
        return self.call(url=url, method="POST")

    get_firewall_rule = firewall.get_firewall_rule

    apply_firewall_changes = firewall.apply_firewall_changes
    delete_all_firewall_rules = firewall.delete_all_firewall_rules  # lol

    create_firewall_alias = firewall.create_firewall_alias
    delete_firewall_alias = firewall.delete_firewall_alias
    get_firewall_alias = firewall.get_firewall_alias
    update_firewall_alias = firewall.update_firewall_alias

    get_firewall_nat_one_to_one = firewall.get_firewall_nat_one_to_one

    get_nat_outbound_mapping = firewall.get_nat_outbound_mapping

    get_firewall_nat_port_forward = firewall.get_firewall_nat_port_forward

    get_firewall_schedule = firewall.get_firewall_schedule
    get_firewall_states = firewall.get_firewall_states
    get_firewall_states_size = firewall.get_firewall_states_size

    get_system_api_error = system.get_system_api_error
    get_system_api_version = system.get_system_api_version

    get_traffic_shaper_limiter = firewall.get_traffic_shaper_limiter

    get_virtual_ip = firewall.get_virtual_ip

    update_system_api_configuration = system.update_system_api_configuration

    def execute_shell_command(self, shell_cmd: str):
        """execute a shell command on the firewall
        https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-execute-shell-command
        """
        url = "/api/v1/diagnostics/command_prompt"
        method = "POST"

        return self.call(
            url=url,
            method=method,
            payload={"shell_cmd": shell_cmd},
        )
