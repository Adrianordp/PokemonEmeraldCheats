"""
Module for importing data from CSV files to database. This module provides
functions to read CSV files and insert the data into the database using the
repository pattern.
"""

import csv

from app.core.database import get_db
from app.repository.pokemons import PokemonsRepository
from app.repository.wild_encounters import WildEncountersRepository
from app.repository.wild_encounters_level import WildEncountersLevelRepository
from app.schemas.pokemons import PokemonCreate
from app.schemas.wild_encounters import WildEncountersCreate
from app.schemas.wild_encounters_level import WildEncountersLevelCreate


def import_pokemons_from_csv(file_path: str) -> None:
    """Import pokemons from a CSV file and insert them into the database."""

    name_set = set()
    new_pokemon_names = set()
    duplicate_pokemon_names = set()

    db = next(get_db())

    names_in_db = {pokemon.name for pokemon in PokemonsRepository.read_all(db)}
    name_set.update(names_in_db)

    with open(file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            name = row["name"]

            if not name:
                continue

            upper_name = name.upper()

            if upper_name in name_set:
                duplicate_pokemon_names.add(upper_name)

                continue

            try:
                PokemonsRepository.create(db, PokemonCreate(name=upper_name))
                name_set.add(upper_name)
                new_pokemon_names.add(upper_name)
            except Exception as e:
                print(f"Error inserting pokemon '{upper_name}': {e}")

    print(f"Finished importing pokemons from {file_path}")
    print(f"Newly inserted pokemons: {', '.join(new_pokemon_names)}")
    print(f"Duplicates skipped: {len(duplicate_pokemon_names)}")
    print(f"Duplicates: {', '.join(duplicate_pokemon_names)}")
    print(f"Total pokemons in database: {len(name_set)}")


def import_wild_encounters_from_csv(file_path: str) -> None:
    """
    Import wild encounters from a CSV file and insert them into the database.
    """
    codes_set = set()
    new_codes = set()
    duplicate_codes = set()

    db = next(get_db())

    codes_in_db = {
        wild_encounter.code
        for wild_encounter in WildEncountersRepository.read_all(db)
    }
    codes_set.update(codes_in_db)

    with open(file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            code = row["code"]

            if not code:
                continue

            if code in codes_set:
                duplicate_codes.add(code)
                continue

            pokemon = row["pokemon"]
            pokemon_upper = pokemon.upper()
            pokemon_in_db = PokemonsRepository.read_by_name(db, pokemon_upper)

            if not pokemon_in_db:
                print(
                    f"Warning: Pokemon '{pokemon_upper}' not found in database."
                )

            try:
                WildEncountersRepository.create(
                    db,
                    WildEncountersCreate(
                        id_pokemon=pokemon_in_db.id, code=row["code"]
                    ),
                )
                codes_set.add(code)
                new_codes.add(code)
            except Exception as e:
                print(f"Error inserting wild encounter: {e}")

    print(f"Finished importing wild encounters from {file_path}")
    print(f"Newly inserted wild encounters: {', '.join(new_codes)}")
    print(f"Duplicates skipped: {len(duplicate_codes)}")
    print(f"Duplicates: {', '.join(duplicate_codes)}")
    print(f"Total wild encounters in database: {len(codes_set)}")


def import_wild_encounters_level_from_csv(file_path: str) -> None:
    """
    Import wild encounters level modifiers from a CSV file and insert them into
    the database.
    """
    levels_set = set()
    new_levels = set()
    duplicate_levels = set()

    db = next(get_db())

    levels_in_db = {
        level_modifier.level
        for level_modifier in WildEncountersLevelRepository.read_all(db)
    }
    levels_set.update(levels_in_db)

    with open(file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            level = int(row["level"])

            if not level:
                continue

            if level in levels_set:
                duplicate_levels.add(level)
                continue

            try:
                WildEncountersLevelRepository.create(
                    db,
                    WildEncountersLevelCreate(
                        level=level,
                        code=row["code"],
                    ),
                )
                levels_set.add(level)
                new_levels.add(level)
            except Exception as e:
                print(f"Error inserting wild encounter level modifier: {e}")

    print(f"Finished importing wild encounter level modifiers from {file_path}")
    print(f"Newly inserted levels: {', '.join(map(str, new_levels))}")
    print(f"Duplicates skipped: {len(duplicate_levels)}")
    print(f"Duplicates: {', '.join(map(str, duplicate_levels))}")
    print(f"Total levels in database: {len(levels_set)}")


def main():
    """Main function to execute the import process."""
    import_pokemons_from_csv("res/pokemons.csv")
    import_wild_encounters_from_csv("res/wild_encounter_modifier_cheats.csv")
    import_wild_encounters_level_from_csv(
        "res/wild_encounter_level_modifier_cheats.csv"
    )


if __name__ == "__main__":
    main()
