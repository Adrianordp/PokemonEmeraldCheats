"""
This module contains the main function to read cheats for pokemons, wild
encounters, and wild encounter levels from database.
"""

from app.core.database import get_db
from app.repository.pokemons import PokemonsRepository
from app.repository.wild_encounters import WildEncountersRepository
from app.repository.wild_encounters_level import WildEncountersLevelRepository


def get_pokemon_cheats(pokemon_name: str) -> list[str]:
    """Get all cheat codes related to a specific pokemon."""


def get_pokemon_encounter_cheat(pokemon_name: str) -> list[str]:
    """Get the cheat codes for a specific pokemon."""
    db = next(get_db())
    pokemon = PokemonsRepository.read_by_name(db, pokemon_name.upper())

    if not pokemon:
        raise ValueError(f"No pokemon found with name '{pokemon_name}'")

    wild_encounters = WildEncountersRepository.read_by_pokemon_id(
        db, pokemon.id
    )

    if not wild_encounters:
        raise ValueError(
            f"No wild encounters found for pokemon '{pokemon_name}'"
        )

    return [encounter.code for encounter in wild_encounters]


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
    pokemon_name = "pikachu"
    try:
        cheat_codes = get_pokemon_encounter_cheat(pokemon_name)
        print(
            f"Cheat codes for pokemon '{pokemon_name}': {', '.join(cheat_codes)}"
        )
    except ValueError as e:
        print(e)

    level = 55
    try:
        cheat_code = get_level_cheat(level)
        print(f"Cheat code for wild encounter level {level}: {cheat_code}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
