""" utility functions for the tests """

import pytest

from pfsense_api_client import PFSenseAPIClient

@pytest.fixture()
def client() -> PFSenseAPIClient:
    """ returns a configured API client """
    return PFSenseAPIClient(
        config_filename="~/.config/pfsense-api.json"
        )
