""" typing for the API """

from typing import Any, Dict, List

from pydantic import BaseModel, Field, validator

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
    data: List[Any]

    @validator("code")
    def validate_code(cls, value: int) -> int:
        if value not in [200, 400, 401, 403, 404, 500]:
            raise ValueError(f"Got an invalid status code ({value}).")
        return value

class APIResponseDict(APIResponse):
    """ Dict-style JSON API response from the pFsense API"""
    data: Dict[str, Any]

class APIResponseList(APIResponse):
    """ List-style JSON API response from the pFsense API"""
    data: List[Any]
