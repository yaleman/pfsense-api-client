""" testing firewall things """

import json
import pytest

from pfsense_api_client import PFSenseAPIClient

@pytest.fixture(name="pfsense")
def pfsense_api_client():
    """ returns a configured API client """
    return PFSenseAPIClient(
        config_filename="~/.config/pfsense-api.json"
        )


def test_get_system_api_version(pfsense: PFSenseAPIClient):
    """ tests getting the API version """
    response = pfsense.get_system_api_version()

    print(json.dumps(response.json()))
    assert response

def test_update_system_api_configuration(pfsense: PFSenseAPIClient):
    """ tests setting the API to not-read-only """
    response = pfsense.update_system_api_configuration(readonly=False)

    print(json.dumps(response.json()))
    assert response
