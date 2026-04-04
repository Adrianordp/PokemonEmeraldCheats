# Pokemon Emerald Cheats Repository

This repository contains a collection of cheat codes for the game Pokemon
Emerald. The cheat codes are organized in a structured format and can be easily
accessed and used by players to enhance their gaming experience.

## Cheat Code Categories
- **Wild Encounter Modifiers**: Codes to set specific Pokemon to appear in wild
encounters.
- **Level Modifiers**: Codes to set the levels of wild Pokemon encounters.

## Usage

### Importing Cheat Codes from CSV
To import cheat codes from CSV files, you can run the following command:
```bash
uv run python -m app.import_from_csv
```

### Help
To see the available options and usage instructions, you can run the following command:
```bash
uv run python -m app.main -h
# usage: main.py [-h] (-p POKEMON | -w WILD_ENCOUNTER | -l LEVEL)

# Get cheat codes for pokemons and wild encounters.

# options:
#   -h, --help            show this help message and exit
#   -p, --pokemon POKEMON
#                         Get all cheat codes for a specific pokemon.
#   -w, --wild-encounter WILD_ENCOUNTER
#                         Get cheat codes for a specific pokemon wild encounter.
#   -l, --level LEVEL     Get the cheat code for a specific wild encounter level.
```

### Getting All Cheat Codes for a Specific Pokemon
To get cheat codes for a specific Pokemon, you can run the following command:
```bash
uv run python -m app.main -p pikachu
```

### Getting Cheat Codes to Set Wild Encounter Of a Specific Pokemon
To get cheat codes to set wild encounters of a specific Pokemon, you can run the following command:
```bash
uv run python -m app.main -w pikachu
```

### Getting Cheat Codes to Set Wild Encounter Level
To get cheat codes to set wild encounter levels, you can run the following command:
```bash
uv run python -m app.main -l 55
```