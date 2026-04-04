from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from app.models.pokemons import Pokemons

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

    from app.schemas.pokemons import PokemonCreate, PokemonUpdate


class PokemonsRepository:
    @staticmethod
    def create(db: Session, pokemon: PokemonCreate) -> Pokemons:
        data = pokemon.model_dump(exclude_unset=True)
        db_pokemon = Pokemons(**data)
        db.add(db_pokemon)
        db.commit()
        db.refresh(db_pokemon)
        return db_pokemon

    @staticmethod
    def read_all(db: Session) -> list[Pokemons]:
        return db.query(Pokemons).all()

    @staticmethod
    def read_by_id(db: Session, pokemon_id: int) -> Optional[Pokemons]:
        return db.query(Pokemons).filter(Pokemons.id == pokemon_id).first()

    @staticmethod
    def read_by_name(db: Session, name: str) -> Optional[Pokemons]:
        return db.query(Pokemons).filter(Pokemons.name == name).first()

    @staticmethod
    def update(
        db: Session, pokemon_id: int, pokemon: PokemonUpdate
    ) -> Optional[Pokemons]:
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
        return db_pokemon

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
