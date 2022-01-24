""" testing firewall things """

import pytest

from pfsense_api_client import PFSenseAPIClient

@pytest.fixture(name="pfsense")
def pfsense_api_client():
    """ returns a configured API client """
    return PFSenseAPIClient(
        config_filename="~/.config/pfsense-api.json"
        )

def test_firewall_get_rules(pfsense: PFSenseAPIClient):
    """ tests getting rules """
    response = pfsense.get_firewall_rule()
    assert len(response.json()) > 0

def test_firewall_get_rules_interface_filter(pfsense: PFSenseAPIClient):
    """ tests getting rules """
    wandata = pfsense.get_firewall_rule(interface="wan")
    assert len(wandata.json()) > 0
    landata = pfsense.get_firewall_rule(interface="lan")
    assert len(landata.json()) > 0
    assert landata != wandata
