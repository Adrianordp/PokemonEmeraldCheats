"""
This module contains the main function to read cheats for pokemons, wild
encounters, and wild encounter levels from database.
"""

import json

from app.core.database import get_db
from app.repository.pokemons import PokemonsRepository


def get_pokemon_cheats(pokemon_name: str) -> dict[str, list[str]]:
    """Get all cheat codes related to a specific pokemon."""
    db = next(get_db())
    pokemons = PokemonsRepository.read_by_name_fragment(
        db, pokemon_name.upper()
    )

    if not pokemons:
        raise ValueError(f"No pokemon found with name '{pokemon_name}'")

    cheats: dict[str, list[str]] = {}

    for pokemon in pokemons:
        pokemon_name = pokemon.name

        if pokemon.wild_encounters:
            cheats[pokemon_name] = []

            for encounter in pokemon.wild_encounters:
                if encounter.code:
                    cheats[pokemon_name].append(encounter.code)

    return cheats


def main():
    """Main function to execute the get_pokemon_cheats process."""
    name = "pikachu"
    try:
        cheats = get_pokemon_cheats(name)
        print(f"All cheat codes for pokemon '{name}':")
        print(json.dumps(cheats, indent=2))
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
