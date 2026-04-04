from typing import Optional

from pydantic import BaseModel, Field


class PokemonBase(BaseModel):
    name: str = Field(..., max_length=255)


class PokemonCreate(PokemonBase):
    model_config = {
        "json_schema_extra": {"example": {"name": "Bulbasaur"}},
    }


class PokemonRead(PokemonBase):
    id: int

    model_config = {
        "from_attributes": True,
        "json_schema_extra": {"example": {"id": 1, "name": "Bulbasaur"}},
    }


class PokemonUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=255)

    model_config = {
        "json_schema_extra": {"example": {"name": "Ivysaur"}},
    }
