""" testing firewall things """

import requests
import pytest

from pfsense_api_client import PFSenseAPIClient

@pytest.fixture(name="pfsense")
def pfsense_api_client():
    """ returns a configured API client """
    return PFSenseAPIClient(
        config_filename="~/.config/pfsense-api.json"
        )



def test_get_firewall_alias(pfsense: PFSenseAPIClient):
    """ pulls the full list of aliases """

    result = pfsense.get_firewall_alias()
    assert result
    print(result.json())

def test_get_firewall_alias_name(pfsense: PFSenseAPIClient):
    """ pulls a firewall alias called zzz_testing """

    result: requests.Response = pfsense.get_firewall_alias(name="zzz_testing")
    assert result.status_code == 200
    assert "zzz_testing" in result.text

    print(result.json())

def test_create_bogus_alias(pfsense: PFSenseAPIClient):
    """ creates an alias called zzz_bogus """

    try:
        result: requests.Response = pfsense.create_firewall_alias(
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

def test_delete_bogus_alias(pfsense: PFSenseAPIClient):
    """ delets an alias called zzzbogus """

    result: requests.Response = pfsense.delete_firewall_alias(
        name="zzzbogus",
        apply = False,
    )

    assert result.status_code == 200
