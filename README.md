# pfsense-api-client

Provides python methods to call the pfsense API endpoint provided by the package at https://github.com/jaredhendrickson13/pfsense-api

# ⚠️ WARNING ⚠️
# This is very early in development.

### Configuring authentication

Configure it one of two ways 

1. Pass the `config_filename` which is a JSON file with username/password/host (and optionally port).
2. Directly pass username/password/hostname (and optionally port).

At the moment it only supports the "Local Database" authentication method of username/password, but it should be relatively trivial to add JWT/API Token support at a later time.

(If you're going to do this, modify init to have a "mode" setting, which `call()` checks, then modifies things as needed.)

### Example JSON file

```json
{
        "username" : "me",
        "password" : "mysupersecretpassword",
        "hostname" : "example.com",
        "port" : 8443
}
```

## Ignoring Certificate validation

You can specify a `requests_session` option on construction, which one could configure to ignore verification.

```python
import requests

from pfsense_api_client import PFSenseAPIClient

session = requests.Session()
session.verify = False
api = PFSenseAPIClient(
        config_filename="~/.config/pfsense.json",
        requests_session=session,
        )
```