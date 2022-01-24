""" testing firewall things """

import pytest

from pfsense_api_client import PFSenseAPIClient

@pytest.fixture(name="pfsense")
def pfsense_api_client():
    """ returns a configured API client """
    return PFSenseAPIClient(
        config_filename="~/.config/pfsense-api.json"
        )



def test_get_firewall_alias(pfsense: PFSenseAPIClient):
    """ creates an alias called zzz_bogus """

    result = pfsense.get_firewall_alias()
    assert result
    print(result.json())

def test_create_bogus_alias(pfsense: PFSenseAPIClient):
    """ creates an alias called zzz_bogus """

    result = pfsense.create_firewall_alias(
        name="zzzbogus",
        alias_type="host",
        descr = "Bogus description",
        address = "bogus.lol",
        detail = "bogus.lol is bogus",
        apply = False,
    )

    assert result.status_code == 200
