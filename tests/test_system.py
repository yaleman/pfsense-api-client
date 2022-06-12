""" tests that we can authenticate! """

import pytest

from pfsense_api_client import PFSenseAPIClient

@pytest.fixture()
def client() -> PFSenseAPIClient:
    """ returns a configured API client """
    return PFSenseAPIClient(
        config_filename="~/.config/pfsense-api.json"
        )

def test_system_status(client: PFSenseAPIClient) -> None:
    """ tests system_status """

    result = client.get_system_status()
    print(f"{result=}")
    assert result.status == "ok"
    assert result.code == 200
    assert result.data
