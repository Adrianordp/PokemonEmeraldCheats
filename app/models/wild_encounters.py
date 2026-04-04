from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base
from app.models.pokemons import Pokemons


class WildEncounters(Base):
    __tablename__ = "wild_encounters"

    id: Mapped[int] = mapped_column(primary_key=True)
    id_pokemon: Mapped[int] = mapped_column(ForeignKey("pokemons.id"))

    code: Mapped[str] = mapped_column(String(17))

    pokemon: Mapped["Pokemons"] = relationship(
        "Pokemons", back_populates="wild_encounters"
    )
