"""
This module contains the main function to read cheats for pokemons, wild
encounters, and wild encounter levels from database.
"""

import json

from app.core.database import get_db
from app.repository.pokemons import PokemonsRepository
from app.repository.wild_encounters import (
    WildEncountersRepository,  # noqa: F401
)
from app.repository.wild_encounters_level import WildEncountersLevelRepository


def get_pokemon_cheats(pokemon_name: str) -> dict[str, list[str]]:
    """Get all cheat codes related to a specific pokemon."""
    db = next(get_db())
    pokemon = PokemonsRepository.read_by_name(db, pokemon_name.upper())

    if not pokemon:
        raise ValueError(f"No pokemon found with name '{pokemon_name}'")

    pokemon_data = pokemon.model_dump()

    pokemon_data.pop("id", None)
    pokemon_data.pop("name", None)

    cheats = {}

    if pokemon_data.get("wild_encounters"):
        cheats["wild_encounters"] = []
        for encounter in pokemon_data["wild_encounters"]:
            if encounter.get("code"):
                cheats["wild_encounters"].append(encounter["code"])

    return cheats


def get_pokemon_encounter_cheat(pokemon_name: str) -> list[str]:
    """Get the cheat codes for a specific pokemon."""
    db = next(get_db())
    pokemon = PokemonsRepository.read_by_name(db, pokemon_name.upper())

    if not pokemon:
        raise ValueError(f"No pokemon found with name '{pokemon_name}'")

    if not pokemon.wild_encounters:
        raise ValueError(
            f"No wild encounters found for pokemon '{pokemon_name}'"
        )

    return [encounter.code for encounter in pokemon.wild_encounters]


def get_level_cheat(level: int) -> str:
    """Get the cheat code for a specific wild encounter level."""
    db = next(get_db())
    wild_encounters_level = WildEncountersLevelRepository.read_by_level(
        db, level=level
    )

    if not wild_encounters_level:
        raise ValueError(f"No cheat found for level {level}")

    return wild_encounters_level.code


def main():
    """Main function to execute the import process."""
    name = "pikachu"
    try:
        cheats = get_pokemon_cheats(name)
        print(f"All cheat codes for pokemon '{name}':")
        print(json.dumps(cheats, indent=2))
    except ValueError as e:
        print(e)

    name = "pikachu"
    try:
        cheat_codes = get_pokemon_encounter_cheat(name)
        print(f"Cheat codes to encounter pokemon '{name}':")
        print(json.dumps(cheat_codes, indent=2))

    except ValueError as e:
        print(e)

    level = 55
    try:
        cheat_code = get_level_cheat(level)
        print(f"Cheat code for wild encounter level {level}:")
        print(json.dumps(cheat_code, indent=2))
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
