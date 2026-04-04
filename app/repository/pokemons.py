from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from app.models.pokemons import Pokemons
from app.schemas.pokemons import PokemonRead
from app.schemas.read_full import PokemonReadFull

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

    from app.schemas.pokemons import PokemonCreate, PokemonUpdate


class PokemonsRepository:
    @staticmethod
    def create(db: Session, pokemon: PokemonCreate) -> PokemonRead:
        data = pokemon.model_dump(exclude_unset=True)
        db_pokemon = Pokemons(**data)
        db.add(db_pokemon)
        db.commit()
        db.refresh(db_pokemon)
        return PokemonRead.model_validate(db_pokemon)

    @staticmethod
    def read_all(db: Session) -> list[PokemonRead]:
        pokemons = db.query(Pokemons).all()
        return [PokemonRead.model_validate(pokemon) for pokemon in pokemons]

    @staticmethod
    def read_by_id(db: Session, pokemon_id: int) -> Optional[PokemonReadFull]:
        pokemon = db.query(Pokemons).filter(Pokemons.id == pokemon_id).first()
        if pokemon:
            return PokemonReadFull.model_validate(pokemon)
        return None

    @staticmethod
    def read_by_name(db: Session, name: str) -> Optional[PokemonReadFull]:
        pokemon = db.query(Pokemons).filter(Pokemons.name == name).first()
        if pokemon:
            return PokemonReadFull.model_validate(pokemon)
        return None

    @staticmethod
    def update(
        db: Session, pokemon_id: int, pokemon: PokemonUpdate
    ) -> Optional[PokemonRead]:
        db_pokemon = (
            db.query(Pokemons).filter(Pokemons.id == pokemon_id).first()
        )
        if not db_pokemon:
            return None

        data = pokemon.model_dump(exclude_unset=True)

        for key, value in data.items():
            setattr(db_pokemon, key, value)

        db.commit()
        db.refresh(db_pokemon)
        return PokemonRead.model_validate(db_pokemon)

    @staticmethod
    def delete(db: Session, pokemon_id: int) -> bool:
        db_pokemon = (
            db.query(Pokemons).filter(Pokemons.id == pokemon_id).first()
        )
        if not db_pokemon:
            return False
        db.delete(db_pokemon)
        db.commit()
        return True
