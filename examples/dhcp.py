#!/usr/bin/env python
""" interacting with dhcp things """

import sys
from typing import Dict, List, Optional

import questionary
from pfsense_api_client import PFSenseAPIClient

import click
from loguru import logger

LOGGER_FORMAT = '<level>{message}</level>'


def get_client() -> PFSenseAPIClient:
    """ client factory """
    logger.remove()
    logger.add(format=LOGGER_FORMAT, sink=sys.stdout)
    client = PFSenseAPIClient(
        config_filename="~/.config/pfsense-api.json"
        )
    return client

@click.group()
def cli():
    """ DHCP CLI for pFsense """

@cli.command()
@click.option("--mac", "-m", help="Delete by MAC address")
@click.option("--hostname", "-h", help="Delete by hostname")
@click.option("--ip", "-i", help="Delete by IP Address")
@click.option("--debug", "-d", is_flag=True, default=False, help="Debug mode, dump more data.")
def delete_lease(
    mac: Optional[str] = None,
    hostname: Optional[str] = None,
    ip: Optional[str] = None,
    debug: bool = False,
) -> None:
    """ Delete a DHCP lease, not actually supported by the pFsense API yet... https://github.com/jaredhendrickson13/pfsense-api/issues/212 """
    client = get_client()
    lease_info = client.get_dhcpd_leases()
    lease_data:  List[Dict[str, str]] = lease_info.data

    if mac and debug:
        logger.debug("Searching for MAC: {}", mac.lower())
    if hostname and debug:
        logger.debug("Searching for hostname: {}", hostname.lower())
    if ip and debug:
        logger.debug("Searching for IP: {}", ip.lower())

    if not (mac or hostname or ip):
        logger.error("Please specify one of MAC/hostname/IP address")
        sys.exit(1)

    for lease in lease_data:
        if mac and "mac" in lease:
            if mac.lower() != lease["mac"].lower():
                if debug:
                    logger.debug("Skipping this because MAC doesn't match: {}", lease)
                continue
        if hostname and "hostname" in lease:
            if hostname.lower() != lease["hostname"].lower():
                if debug:
                    logger.debug("Skipping this because hostname doesn't match: {}", lease)
                continue
        if ip and "ip" in lease:
            if ip.lower() != lease["ip"].lower():
                if debug:
                    logger.debug("Skipping this because IP Address doesn't match: {}", lease)
                continue
        logger.warning("Target:")
        for key, item in lease.items():
            if key != "staticmap_array_index" and str(item).strip() != "":
                logger.info("{:10} {}", key, item)
        if questionary.confirm("Please confirm deletion: ").ask():
            logger.error("Sorry, this isn't supported by the pFsense API yet!")




@cli.command()
@click.option("--find", "-f", help="Does a wildcard match based on this")
@click.option("--expired", "-e", is_flag=True, default=False, help="Includes expired leases, off by default.")
@click.option("--debug", "-d", is_flag=True, default=False, help="Debug mode, dump more data.")
def list_leases(
    find: Optional[str]=None,
    expired: bool=False,
    debug: bool=False,
    ) -> None:
    """ lists DHCP leases """
    client = get_client()
    lease_info = client.get_dhcpd_leases()

    lease_data:  List[Dict[str, str]] = lease_info.data

    for lease in lease_data:
        if find is not None:
            if find not in str(lease.values()):
                continue
        if not expired and lease['state'] == "expired":
            continue
        lease_message = f"{lease['type']}\t{lease['mac']}\t{lease['ip']}\t{lease.get('hostname', '')}"
        if "descr" in lease and lease["descr"]:
            lease_message += f" ({lease['descr']})"
        if not lease["online"]:
            logger.debug(lease_message)
        else:
            logger.info(lease_message)
        if debug:
            logger.debug(lease)

if __name__ == '__main__':
    cli()
