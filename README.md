# pfsense-api-client

Provides python methods to call the pfsense API endpoint provided by the package at https://github.com/jaredhendrickson13/pfsense-api

# Authentication

Configure it one of two ways 

1. Pass the `config_filename` which is a JSON file with username/password/host (and optionally port).
2. Directly pass username/password/hostname (and optionally port).

At the moment it only supports the "Local Database" authentication method of username/password, but it should be relatively trivial to add JWT/API Token support at a later time.

(If you're going to do this, modify init to have a "mode" setting, which `call()` checks, then modifies things as needed.)