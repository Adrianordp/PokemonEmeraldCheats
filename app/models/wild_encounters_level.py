from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class WildEncountersLevel(Base):
    __tablename__ = "wild_encounters_level"

    id: Mapped[int] = mapped_column(primary_key=True)
    level: Mapped[int] = mapped_column()
    code: Mapped[str] = mapped_column(String(17))
