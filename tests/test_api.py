""" testing firewall things """

import json

from pfsense_api_client import PFSenseAPIClient

from .utils import client

def test_get_system_api_version(client: PFSenseAPIClient) -> None:
    """ tests getting the API version """
    response = client.get_system_api_version()

    print(json.dumps(response.dict()))
    assert response.status

def test_update_system_api_configuration(client: PFSenseAPIClient) -> None:
    """ tests setting the API to not-read-only """
    response = client.update_system_api_configuration(readonly=False)

    print(json.dumps(response.json()))
    assert response
