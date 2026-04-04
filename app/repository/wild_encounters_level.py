from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from app.models.wild_encounters_level import WildEncountersLevel

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

    from app.schemas.wild_encounters_level import (
        WildEncountersLevelCreate,
        WildEncountersLevelUpdate,
    )


class WildEncountersLevelRepository:
    @staticmethod
    def create(
        db: Session, wild_encounters_level: WildEncountersLevelCreate
    ) -> WildEncountersLevel:
        data = wild_encounters_level.model_dump(exclude_unset=True)
        db_wild_encounters_level = WildEncountersLevel(**data)
        db.add(db_wild_encounters_level)
        db.commit()
        db.refresh(db_wild_encounters_level)
        return db_wild_encounters_level

    @staticmethod
    def read_all(db: Session) -> list[WildEncountersLevel]:
        return db.query(WildEncountersLevel).all()

    @staticmethod
    def read_by_id(
        db: Session, wild_encounters_level_id: int
    ) -> Optional[WildEncountersLevel]:
        return (
            db.query(WildEncountersLevel)
            .filter(WildEncountersLevel.id == wild_encounters_level_id)
            .first()
        )

    @staticmethod
    def read_by_level(db: Session, level: int) -> Optional[WildEncountersLevel]:
        return (
            db.query(WildEncountersLevel)
            .filter(WildEncountersLevel.level == level)
            .first()
        )

    @staticmethod
    def update(
        db: Session,
        wild_encounters_level_id: int,
        wild_encounters_level: WildEncountersLevelUpdate,
    ) -> Optional[WildEncountersLevel]:
        db_wild_encounters_level = (
            db.query(WildEncountersLevel)
            .filter(WildEncountersLevel.id == wild_encounters_level_id)
            .first()
        )
        if not db_wild_encounters_level:
            return None

        data = wild_encounters_level.model_dump(exclude_unset=True)

        for key, value in data.items():
            setattr(db_wild_encounters_level, key, value)

        db.commit()
        db.refresh(db_wild_encounters_level)
        return db_wild_encounters_level

    @staticmethod
    def delete(db: Session, wild_encounters_level_id: int) -> bool:
        db_wild_encounters_level = (
            db.query(WildEncountersLevel)
            .filter(WildEncountersLevel.id == wild_encounters_level_id)
            .first()
        )
        if not db_wild_encounters_level:
            return False
        db.delete(db_wild_encounters_level)
        db.commit()
        return True
