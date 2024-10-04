import datetime as dt
from enum import Enum
from typing import Annotated, Any, Optional

from pydantic import AfterValidator, BaseModel, Field, HttpUrl, RootModel

INPUT_DATE_FORMAT = "%Y-%m-%dT%H:%M"


def check_date_format(value: str) -> dt.datetime:
    return dt.datetime.strptime(value, INPUT_DATE_FORMAT)


class Status(Enum):
    down = "down"
    resolved = "resolved"
    degraded = "degraded"
    at_risk = "at risk"


class Update(BaseModel):
    date: Annotated[str, AfterValidator(check_date_format)]
    details: str
    url: Optional[HttpUrl] = None


class Incident(BaseModel):
    status: Status
    affectedServices: str
    summary: str
    date: Annotated[str, AfterValidator(check_date_format)]
    updates: list[Update] = Field(min_length=1)


class StatusPage(RootModel[Any]):
    root: list[Incident]
