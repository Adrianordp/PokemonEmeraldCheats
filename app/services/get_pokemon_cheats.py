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
