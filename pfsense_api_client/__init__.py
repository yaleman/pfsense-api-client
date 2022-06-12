""" pfSense API client """

import json

import os.path

from pathlib import Path
from typing import Any, Dict, Optional

from pydantic import BaseModel
import requests


from .api_types import APIResponse, BasePFSenseAPIClient
from .constants import RESPONSE_CODES
from .firewall import FirewallMixin
from .service  import ServiceMixin
from .status import StatusMixin
from .system import SystemMixin

__all__ = [
    "PFSenseAPIClient",
]



class PFSenseAPIClient(
    FirewallMixin,
    ServiceMixin,
    StatusMixin,
    SystemMixin,
    BasePFSenseAPIClient,
    ):
    """pfSense API Client"""

    def request_access_token(self) -> requests.Response:
        """gets a temporary access token
        https://github.com/jaredhendrickson13/pfsense-api/blob/master/README.md#1-request-access-token
        """
        url = "/api/v1/access_token"
        return self.call(url=url, method="POST")

    def execute_shell_command(self, shell_cmd: str) -> requests.Response:
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
