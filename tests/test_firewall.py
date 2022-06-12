""" testing firewall things """

import pytest

from pfsense_api_client import PFSenseAPIClient

@pytest.fixture()
def client() -> PFSenseAPIClient:
    """ returns a configured API client """
    return PFSenseAPIClient(
        config_filename="~/.config/pfsense-api.json"
        )

def test_firewall_get_rules(client: PFSenseAPIClient) -> None:
    """ tests getting rules """
    response = client.get_firewall_rule()
    assert len(response.json()) > 0

def test_firewall_get_rules_interface_filter(client: PFSenseAPIClient) -> None:
    """ tests getting rules """
    wandata = client.get_firewall_rule(interface="wan")
    assert len(wandata.json()) > 0
    landata = client.get_firewall_rule(interface="lan")
    assert len(landata.json()) > 0
    assert landata != wandata
