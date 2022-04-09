""" typing for the API """

from typing import Any, List, Optional

from pydantic import BaseModel, Field, validator

__all__ = [
    "APIResponse"
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
