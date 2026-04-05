"""
This module contains the main function to read cheats for pokemons, wild
encounters, and wild encounter levels from database.
"""

import json

from app.core.database import get_db
from app.repository.pokemons import PokemonsRepository


def get_pokemon_encounter_cheat(pokemon_name: str) -> dict[str, list[str]]:
    """Get the cheat codes for a specific pokemon."""
    db = next(get_db())
    pokemons = PokemonsRepository.read_by_name_fragment(
        db, pokemon_name.upper()
    )

    if not pokemons:
        raise ValueError(f"No pokemon found with name '{pokemon_name}'")

    codes: dict[str, list[str]] = {}

    for pokemon in pokemons:
        pokemon_name = pokemon.name

        if pokemon.wild_encounters:
            codes[pokemon_name] = []

            for encounter in pokemon.wild_encounters:
                if encounter.code:
                    codes[pokemon_name].append(encounter.code)

    return codes


def main():
    """Main function to execute the get_pokemon_encounter_cheat process."""
    name = "pikachu"
    try:
        cheat_codes = get_pokemon_encounter_cheat(name)
        print(f"Cheat codes to encounter pokemon '{name}':")
        print(json.dumps(cheat_codes, indent=2))

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
