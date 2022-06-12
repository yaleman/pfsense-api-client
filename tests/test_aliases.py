""" testing firewall things """

import requests
import pytest

from pfsense_api_client import PFSenseAPIClient

from .utils import client

def test_get_firewall_alias(client: PFSenseAPIClient) -> None:
    """ pulls the full list of aliases """
    result = client.get_firewall_alias()
    assert result
    print(result.json())

def test_get_firewall_alias_name(client: PFSenseAPIClient) -> None:
    """ pulls a firewall alias called zzz_testing """
    result: requests.Response = client.get_firewall_alias(name="zzz_testing")
    assert result.status_code == 200
    assert "zzz_testing" in result.text

    print(result.json())

def test_create_bogus_alias(client: PFSenseAPIClient) -> None:
    """ creates an alias called zzz_bogus """
    try:
        result: requests.Response = client.create_firewall_alias(
            name="zzzbogus",
            alias_type="host",
            descr = "Bogus description",
            address = "bogus.lol",
            detail = "bogus.lol is bogus",
            apply = False,
        )
    except requests.exceptions.HTTPError as httperror:
        if httperror.response.status_code == 400:
            pytest.skip("Skipping because the alias 'zzzbogus' already exists")
        else:
            raise requests.exceptions.HTTPError from httperror

    assert result.status_code == 200

def test_delete_bogus_alias(client: PFSenseAPIClient) -> None:
    """ delets an alias called zzzbogus """

    result: requests.Response = client.delete_firewall_alias(
        name="zzzbogus",
        apply = False,
    )
    print(f"{result.content=}")

    assert result.status_code == 200
