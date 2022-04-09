""" testing DHCP things """

import json

from pfsense_api_client import PFSenseAPIClient

from .utils import client

def test_get_dhcp_status_log(client: PFSenseAPIClient) -> None:
    """ tests get_dhcp_status_log """

    response = client.get_dhcp_status_log()
    response_dict = response.dict()
    print("replacing data ")
    datalen = len(response_dict["data"])
    response_dict["data"] = [response_dict["data"][0]]
    response_dict["data"].append(f"Original response length: {datalen}")
    print(json.dumps(
        response_dict,
        indent=4,
        default=str,
        ))

    assert response.status == "ok"
    assert response.code == 200
    assert response.return_code == 0

def test_get_dhcpd_leases(client: PFSenseAPIClient) -> None:
    """ tests get_dhcpd_leases """

    response = client.get_dhcpd_leases()
    response_dict = response.dict()
    # print("replacing data ")
    # datalen = len(response_dict["data"])
    # response_dict["data"] = [response_dict["data"][0]]
    # response_dict["data"].append(f"Original response length: {datalen}")
    print(json.dumps(
        response_dict,
        indent=4,
        default=str,
        ))

    assert response.status == "ok"
    assert response.code == 200
    assert response.return_code == 0

def test_get_dhcpd_service_configuration(client: PFSenseAPIClient) -> None:
    """ tests get_dhcpd_service_configuration """

    response = client.get_dhcpd_service_configuration()
    response_dict = response.dict()
    print(json.dumps(
        response_dict,
        indent=4,
        default=str,
        ))

    assert response.status == "ok"
    assert response.code == 200
    assert response.return_code == 0
