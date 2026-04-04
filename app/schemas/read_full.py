from typing import Optional

from app.schemas.pokemons import PokemonRead
from app.schemas.wild_encounters import WildEncountersRead


class WildEncountersReadFull(WildEncountersRead):
    pokemon: Optional[PokemonRead] = None

    model_config = {
        "from_attributes": True,
        "json_schema_extra": {
            "example": {
                "id": 1,
                "id_pokemon": 1,
                "code": "CheatCode123",
                "pokemon": {"id": 1, "name": "Bulbasaur"},
            }
        },
    }


class PokemonReadFull(PokemonRead):
    wild_encounters: list[WildEncountersRead] = []

    model_config = {
        "from_attributes": True,
        "json_schema_extra": {
            "example": {
                "id": 1,
                "name": "Bulbasaur",
                "wild_encounters": [
                    {"id": 1, "id_pokemon": 1, "code": "CheatCode123"}
                ],
            }
        },
    }
