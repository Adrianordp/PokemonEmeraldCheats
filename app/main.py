"""
This module contains the main function to read cheats for pokemons, wild
encounters, and wild encounter levels from database.
"""

import json

from app.services.get_level_cheat import get_level_cheat
from app.services.get_pokemon_cheats import get_pokemon_cheats
from app.services.get_pokemon_encounter_cheat import get_pokemon_encounter_cheat


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
