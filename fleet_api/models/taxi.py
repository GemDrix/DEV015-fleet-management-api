from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from ..database import db

class Taxi(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    plate: Mapped[str] = mapped_column(unique=True)
  