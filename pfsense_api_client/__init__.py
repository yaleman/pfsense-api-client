""" pfSense API client """

import json

import os.path

from pathlib import Path
from typing import Optional

from pydantic import BaseModel, validate_arguments
import requests

__all__ = [
    "PFSenseAPIClient",
    ]


class Config(BaseModel):
    """ this sets up the right typing from the config file"""
    username: str
    password: str
    port: int
    hostname: str

class PFSenseAPIClient():
    """ pfSense API Client """
    # pylint: disable=too-many-arguments
    def __init__(
        self,
        username: Optional[str]=None,
        password: Optional[str]=None,
        hostname: Optional[str]=None,
        port: Optional[int]=None,
        config_filename: Optional[str]=None):
        if username:
            self.username = username
        if password:
            self.password = password
        if hostname:
            self.hostname = hostname
        if port:
            self.port = port
        if config_filename:
            self.config_filename = Path(os.path.expanduser(config_filename))
            if not self.config_filename.exists():
                error = f"Filename {self.config_filename.as_posix()} does not exist."
                raise FileNotFoundError(error)
            pydantic_config = Config(**json.load(self.config_filename.open(encoding="utf8")))
            self.hostname = pydantic_config.hostname
            self.username = pydantic_config.username
            self.password = pydantic_config.password
            self.port = pydantic_config.port

        self.baseurl = f"https://{self.hostname}"
        if hasattr(self, "port"):
            self.baseurl+=f":{self.port}"

    @validate_arguments
    def call(
        self,
        url: str,
        method: Optional[str]=None):
        """ makes an API call """
        call_url = f"{self.baseurl}{url}"
        payload = {
            "client-id": self.username,
            "client-token": self.password
        }

        if not method:
            method="GET"
        # print(f"calling {call_url} {method}")
        # print(f"payload: {payload}")
        if method =="GET":
            response = requests.get(url=call_url, params=payload)
        else:
            response = requests.request(method=method, url=call_url, json=payload)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as error:
            print(f"Failed to call {call_url}: {error}")
            return False
        return response

    def get_firewall_rules(self,
        interface: Optional[str]=None,
        ):
        """ gets the firewall rules """
        # docurl = https://github.com/jaredhendrickson13/pfsense-api#3-read-firewall-rules
        results = self.call("/api/v1/firewall/rule", method='GET')
        data = results.json()

        if "data" not in data:
            raise ValueError("no data")

        rules = data["data"]
        if not interface:
            return rules

        retval = []
        for rule in rules:
            interfaces = rule.get("interface", None)
            if not interfaces:
                continue
            interface_list = interfaces.split(",")
            if interface not in interface_list:
                continue

            retval.append(rule)
        data["data"] = retval
        return data
