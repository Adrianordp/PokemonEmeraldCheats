from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base

if TYPE_CHECKING:
    from app.models.wild_encounters import WildEncounters


class Pokemons(Base):
    __tablename__ = "pokemons"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String(255), unique=True)

    wild_encounters: Mapped[list[WildEncounters]] = relationship(
        "WildEncounters", back_populates="pokemon"
    )
