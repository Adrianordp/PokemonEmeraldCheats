from typing import Optional

from pydantic import BaseModel, Field


class WildEncountersLevelBase(BaseModel):
    level: int = Field(..., ge=1, le=100)
    code: str = Field(..., max_length=17)


class WildEncountersLevelCreate(WildEncountersLevelBase):
    model_config = {
        "json_schema_extra": {"example": {"level": 5, "code": "CheatCode123"}},
    }


class WildEncountersLevelRead(WildEncountersLevelBase):
    id: int

    model_config = {
        "from_attributes": True,
        "json_schema_extra": {
            "example": {"id": 1, "level": 5, "code": "CheatCode123"}
        },
    }


class WildEncountersLevelUpdate(BaseModel):
    level: Optional[int] = Field(None, ge=1, le=100)
    code: Optional[str] = Field(None, max_length=17)

    model_config = {
        "json_schema_extra": {
            "example": {"level": 10, "code": "NewCheatCode456"}
        },
    }
