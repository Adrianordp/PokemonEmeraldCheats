from typing import Optional

from pydantic import BaseModel, Field


class WildEncountersBase(BaseModel):
    id_pokemon: int = Field(..., gt=0)
    code: str = Field(..., max_length=17)


class WildEncountersCreate(WildEncountersBase):
    model_config = {
        "json_schema_extra": {
            "example": {"id_pokemon": 1, "code": "CheatCode123"}
        },
    }


class WildEncountersRead(WildEncountersBase):
    id: int

    model_config = {
        "from_attributes": True,
        "json_schema_extra": {
            "example": {"id": 1, "id_pokemon": 1, "code": "CheatCode123"}
        },
    }


class WildEncountersUpdate(BaseModel):
    id_pokemon: Optional[int] = Field(None, gt=0)
    code: Optional[str] = Field(None, max_length=17)

    model_config = {
        "json_schema_extra": {
            "example": {"id_pokemon": 2, "code": "NewCheatCode456"}
        },
    }
