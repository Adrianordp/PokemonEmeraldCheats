"""
This module contains the main function to read cheats for pokemons, wild
encounters, and wild encounter levels from database.
"""

import json

from app.core.database import get_db
from app.repository.wild_encounters_level import WildEncountersLevelRepository


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
    """Main function to execute the get_level_cheat process."""
    level = 55
    try:
        cheat_code = get_level_cheat(level)
        print(f"Cheat code for wild encounter level {level}:")
        print(json.dumps(cheat_code, indent=2))
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
