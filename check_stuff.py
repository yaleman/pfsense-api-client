#!/usr/bin/env python

""" pulls apart the module and checks it passes some checks """

import inspect

from loguru import logger

import pfsense_api_client.user
import pfsense_api_client.status
import pfsense_api_client.system
import pfsense_api_client.firewall
import pfsense_api_client.routing
import pfsense_api_client.service
import pfsense_api_client.service.dns

IGNORED_MEMBERS = [
    "requests",
    "dns",
]

TYPE_FOR_VERB = {
    "apply" : "POST",
    "create" : "POST",
    "delete" : "DELETE",
    "get" : "GET",
    "restart" : "POST",
    "start" : "POST",
    "stop" : "POST",
    "update" : "PUT",
}

for module in [
    pfsense_api_client.user,
    pfsense_api_client.status,
    pfsense_api_client.system,
    pfsense_api_client.firewall,
    pfsense_api_client.routing,
    pfsense_api_client.service,
    pfsense_api_client.service.dns,
]:

    for name, member in inspect.getmembers(module, ):
        if name in IGNORED_MEMBERS or name.startswith("__"):
            continue
        if inspect.ismodule(member):
            logger.debug("Skipping module: {}", name)
            continue
        if inspect.isfunction(member):
            logger.info("{} is a function!: {}", name, member)
            sig = inspect.signature(member)
            if sig.return_annotation == inspect.Signature.empty:
                logger.warning("Empty response signature")
            logger.debug("sig: {}", sig)
            namesplit = name.split("_")
            verb = namesplit[0]
            if verb not in TYPE_FOR_VERB:
                logger.error("Verb not found: {}", verb)
            # TODO: get the method from inside the function
        else:
            logger.warning("Not sure what {}.{} is: {}", module, name, type(member))
