from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from app.models.wild_encounters import WildEncounters

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

    from app.schemas.wild_encounters import (
        WildEncountersCreate,
        WildEncountersUpdate,
    )


class WildEncountersRepository:
    @staticmethod
    def create(
        db: Session, wild_encounters: WildEncountersCreate
    ) -> WildEncounters:
        data = wild_encounters.model_dump(exclude_unset=True)
        db_wild_encounters = WildEncounters(**data)
        db.add(db_wild_encounters)
        db.commit()
        db.refresh(db_wild_encounters)
        return db_wild_encounters

    @staticmethod
    def read_all(db: Session) -> list[WildEncounters]:
        return db.query(WildEncounters).all()

    @staticmethod
    def read_by_id(
        db: Session, wild_encounters_id: int
    ) -> Optional[WildEncounters]:
        return (
            db.query(WildEncounters)
            .filter(WildEncounters.id == wild_encounters_id)
            .first()
        )

    @staticmethod
    def update(
        db: Session,
        wild_encounters_id: int,
        wild_encounters: WildEncountersUpdate,
    ) -> Optional[WildEncounters]:
        db_wild_encounters = (
            db.query(WildEncounters)
            .filter(WildEncounters.id == wild_encounters_id)
            .first()
        )
        if not db_wild_encounters:
            return None

        data = wild_encounters.model_dump(exclude_unset=True)

        for key, value in data.items():
            setattr(db_wild_encounters, key, value)

        db.commit()
        db.refresh(db_wild_encounters)
        return db_wild_encounters

    @staticmethod
    def delete(db: Session, wild_encounters_id: int) -> bool:
        db_wild_encounters = (
            db.query(WildEncounters)
            .filter(WildEncounters.id == wild_encounters_id)
            .first()
        )
        if not db_wild_encounters:
            return False
        db.delete(db_wild_encounters)
        db.commit()
        return True
