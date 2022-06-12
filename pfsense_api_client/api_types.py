""" typing for the API """

import json
import os
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Field, validator
from requests import Response, Session
__all__ = [
    "APIResponse",
    "APIResponseDict",
    "APIResponseList",
]


class PFSenseConfig(BaseModel):
    """This defines the expected config file

        Example config file:
    ```json
    {
            "username" : "me",
            "password" : "mysupersecretpassword",
            "hostname" : "example.com",
            "port" : 8443,
    }
    ```
    """

    username: Optional[str]
    password: Optional[str]
    port: int = 443
    hostname: str
    mode: str = "local"
    jwt: Optional[str]
    client_id: Optional[str]
    client_token: Optional[str]



class APIResponse(BaseModel):
    """standard JSON API response from the pFsense API"""

    status: str
    code: int
    return_code: int = Field(
        ..., title="return", alias="return", description="The return field from the API"
    )
    message: str
    data: Any

    @validator("code")
    def validate_code(cls, value: int) -> int:
        """validates it's an integer in the expected list"""
        if value not in [200, 400, 401, 403, 404, 500]:
            raise ValueError(f"Got an invalid status code ({value}).")
        return value


class APIResponseDict(APIResponse):
    """Dict-style JSON API response from the pFsense API"""

    data: Dict[str, Any]


class APIResponseList(APIResponse):
    """List-style JSON API response from the pFsense API"""

    data: List[Any]


# pylint: disable=too-few-public-methods
class BasePFSenseAPIClient:
    """ Base """
   # pylint: disable=too-many-arguments,too-many-instance-attributes
    def __init__(
        self,
        username: Optional[str] = None,
        password: Optional[str] = None,
        hostname: Optional[str] = None,
        port: Optional[int] = None,
        config_filename: Optional[str] = None,
        mode: Optional[str] = None,
        requests_session: Session = Session(),
    ):

        self.session = requests_session

        if config_filename:
            self.config = self.load_config(config_filename)
        else:
            config_data: Dict[str, Union[str,int]] = {}
            if username:
                config_data["username"] = username
            if password:
                config_data["password"] = password
            if hostname:
                config_data["hostname"] = hostname
            if port:
                config_data["port"] = port
            if mode:
                config_data["mode"] = mode
            self.config = PFSenseConfig.parse_obj(config_data)

        if self.config.mode == "local" and \
            (self.config.username is not None and self.config.password is not None):
            self.session.auth = (self.config.username, self.config.password)
        elif self.config.mode == "local":
            raise ValueError("Authentication Mode is set to local and username or password are not set!")

    @property
    def baseurl(self) -> str:
        """ returns the base URL of the host """
        retval = f"https://{self.config.hostname}"
        if self.config.port:
            retval += f":{self.config.port}"
        return retval

    def load_config(self, filename: str) -> PFSenseConfig:
        """Loads the config from the specified JSON file (see the `PFSenseConfig` class for what fields are required)"""
        self.config_filename = Path(os.path.expanduser(filename))
        if not self.config_filename.exists():
            error = f"Filename {self.config_filename.as_posix()} does not exist."
            raise FileNotFoundError(error)
        pydantic_config = PFSenseConfig(
            **json.load(self.config_filename.open(encoding="utf8"))
        )
        self.config = pydantic_config
        # self.hostname = pydantic_config.hostname
        # self.port = pydantic_config.port
        # self.mode = pydantic_config.mode or "local"

        return pydantic_config

    def call(
        self,
        url: str,
        method: str = "GET",
        payload: Optional[Any] = None,
        params: Optional[Any] = None,
        **kwargs: Dict[str, Any],
    ) -> Response:
        """mocking type for mypy inheritance"""
        if url.startswith("/"):
            url = f"{self.baseurl}{url}"

        if payload is not None and method == "GET":
            kwargs["params"] = payload
        elif payload is not None:
            kwargs["json"] = payload

        if params is not None:
            kwargs["params"] = params

        if "headers" not in kwargs:
            kwargs["headers"] = {}

        if self.config.mode == "jwt":
            kwargs["headers"]["Authorization"] = f"Bearer {self.config.jwt}"
        elif self.config.mode == "api_token":
            kwargs["headers"]["Authorization"] = f"{self.config.client_id} {self.config.client_token}"

        return self.session.request(
            url=url,
            method=method,
            allow_redirects=True,
            **kwargs,  # type: ignore
            )

    def call_api(
        self,
        url: str,
        method: str = "GET",
        payload: Optional[Dict[str, Any]] = None,
    ) -> APIResponse:
        """makes a call, returns the JSON blob as a dict"""
        response = self.call(url, method, payload)
        return APIResponse.parse_obj(response.json())

    def call_api_dict(
        self,
        url: str,
        method: str = "GET",
        payload: Optional[Dict[str, Any]] = None,
    ) -> APIResponse:
        """makes a call, returns the JSON blob as a dict"""
        response = self.call(url, method, payload)
        print(response.json())
        return APIResponse.parse_obj(response.json())

    def call_json(
        self,
        url: str,
        method: str = "GET",
        payload: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """makes a call, returns the JSON blob as a dict"""
        response = self.call(url, method, payload)
        result: Dict[str, Any] = response.json()
        return result
