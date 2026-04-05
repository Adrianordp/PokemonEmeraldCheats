from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from sqlalchemy import select

from app.models.wild_encounters_level import WildEncountersLevel
from app.schemas.wild_encounters_level import WildEncountersLevelRead

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
    ) -> WildEncountersLevelRead:
        data = wild_encounters_level.model_dump(exclude_unset=True)
        db_wild_encounters_level = WildEncountersLevel(**data)
        db.add(db_wild_encounters_level)
        db.commit()
        db.refresh(db_wild_encounters_level)

        return WildEncountersLevelRead.model_validate(db_wild_encounters_level)

    @staticmethod
    def read_all(db: Session) -> list[WildEncountersLevelRead]:
        stmt = select(WildEncountersLevel)
        wild_encounters_levels = db.execute(stmt).scalars().all()

        return [
            WildEncountersLevelRead.model_validate(level)
            for level in wild_encounters_levels
        ]

    @staticmethod
    def read_by_id(
        db: Session, wild_encounters_level_id: int
    ) -> Optional[WildEncountersLevelRead]:
        stmt = select(WildEncountersLevel).filter(
            WildEncountersLevel.id == wild_encounters_level_id
        )
        wild_encounters_level = db.execute(stmt).scalars().first()

        if wild_encounters_level:
            return WildEncountersLevelRead.model_validate(wild_encounters_level)

        return None

    @staticmethod
    def read_by_level(
        db: Session, level: int
    ) -> Optional[WildEncountersLevelRead]:
        stmt = select(WildEncountersLevel).filter(
            WildEncountersLevel.level == level
        )
        wild_encounters_level = db.execute(stmt).scalars().first()

        if wild_encounters_level:
            return WildEncountersLevelRead.model_validate(wild_encounters_level)

        return None

    @staticmethod
    def update(
        db: Session,
        wild_encounters_level_id: int,
        wild_encounters_level: WildEncountersLevelUpdate,
    ) -> Optional[WildEncountersLevelRead]:
        stmt = select(WildEncountersLevel).filter(
            WildEncountersLevel.id == wild_encounters_level_id
        )
        db_wild_encounters_level = db.execute(stmt).scalars().first()

        if not db_wild_encounters_level:
            return None

        data = wild_encounters_level.model_dump(exclude_unset=True)

        for key, value in data.items():
            setattr(db_wild_encounters_level, key, value)

        db.commit()
        db.refresh(db_wild_encounters_level)

        return WildEncountersLevelRead.model_validate(db_wild_encounters_level)

    @staticmethod
    def delete(db: Session, wild_encounters_level_id: int) -> bool:
        stmt = select(WildEncountersLevel).filter(
            WildEncountersLevel.id == wild_encounters_level_id
        )
        db_wild_encounters_level = db.execute(stmt).scalars().first()

        if not db_wild_encounters_level:
            return False

        db.delete(db_wild_encounters_level)
        db.commit()

        return True
