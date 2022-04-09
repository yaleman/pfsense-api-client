""" typing for the API """

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field, validator
from requests import Response, request
__all__ = [
    "APIResponse",
    "APIResponseDict",
    "APIResponseList",
]

class APIResponse(BaseModel):
    """ standard JSON API response from the pFsense API"""
    status: str
    code: int
    return_code: int = Field(..., title="return", alias="return", description="The return field from the API")
    message: str
    data: Any

    @validator("code")
    def validate_code(cls, value: int) -> int:
        """ validates it's an integer in the expected list """
        if value not in [200, 400, 401, 403, 404, 500]:
            raise ValueError(f"Got an invalid status code ({value}).")
        return value

class APIResponseDict(APIResponse):
    """ Dict-style JSON API response from the pFsense API"""
    data: Dict[str, Any]

class APIResponseList(APIResponse):
    """ List-style JSON API response from the pFsense API"""
    data: List[Any]

# pylint: disable=too-few-public-methods
class TypePFSenseAPIClient:
    """ This is entirely for mypy type inheritance and IDE-prettiness! """
    @classmethod
    def call(cls,
        url: str,
        method: str="GET",
        payload: Optional[Any] = None,
        params: Optional[Any] = None,
        **kwargs: Dict[str, Any],
        ) -> Response:
        """ mocking type for mypy inheritance """
        if payload is not None:
            kwargs["payload"] = payload
        if params is not None:
            kwargs["params"] = params
        return request(url=url, method=method, allow_redirects=True, **kwargs)
