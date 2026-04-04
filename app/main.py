"""
This module contains the main function to read cheats for pokemons, wild
encounters, and wild encounter levels from database.

Usage:
    python -m app.main -p <pokemon_name>
    python -m app.main -w <pokemon_name>
    python -m app.main -l <wild_encounter_level>

p: Get all cheat codes related to a specific pokemon.
w: Get the cheat codes for a specific pokemon wild encounter.
l: Get the cheat code for a specific wild encounter level.
"""

import json
from argparse import ArgumentParser

from app.services.get_level_cheat import get_level_cheat
from app.services.get_pokemon_cheats import get_pokemon_cheats
from app.services.get_pokemon_encounter_cheat import get_pokemon_encounter_cheat

parser = ArgumentParser(
    description="Get cheat codes for pokemons and wild encounters."
)
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument(
    "-p",
    "--pokemon",
    type=str,
    help="Get all cheat codes for a specific pokemon.",
)
group.add_argument(
    "-w",
    "--wild-encounter",
    type=str,
    help="Get cheat codes for a specific pokemon wild encounter.",
)
group.add_argument(
    "-l",
    "--level",
    type=int,
    help="Get the cheat code for a specific wild encounter level.",
)


def main():
    """Main function to execute the parser process."""
    args = parser.parse_args()

    if args.pokemon:
        try:
            cheats = get_pokemon_cheats(args.pokemon)
            print(f"All cheat codes for pokemon '{args.pokemon}':")
            print(json.dumps(cheats, indent=2))
        except ValueError as e:
            print(e)

    elif args.wild_encounter:
        try:
            cheat_codes = get_pokemon_encounter_cheat(args.wild_encounter)
            print(f"Cheat codes to encounter pokemon '{args.wild_encounter}':")
            print(json.dumps(cheat_codes, indent=2))
        except ValueError as e:
            print(e)

    elif args.level is not None:
        try:
            cheat_code = get_level_cheat(args.level)
            print(f"Cheat code for wild encounter level {args.level}:")
            print(json.dumps(cheat_code, indent=2))
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()
