from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, func

db = SQLAlchemy()


class UserModel(db.Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(
        String(64),
        unique=True,
        nullable=False
    )

    record = db.relationship(
        "RecordModel",
        back_populates="user",
        lazy="dynamic"
    )


class CategoryModel(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(
        String(64),
        unique=True,
        nullable=False
    )

    record = db.relationship(
        "RecordModel",
        back_populates="category",
        lazy="dynamic"
    )


class RecordModel(db.Model):
    __tablename__ = 'record'

    id = Column(Integer, primary_key=True)
    user_id = Column(
        Integer,
        ForeignKey("user.id"),
        unique=False,
        nullable=False
    )
    category_id = Column(
        Integer,
        ForeignKey("category.id"),
        unique=False,
        nullable=False
    )

    date = Column(TIMESTAMP, server_default=func.now())
    amount = Column(String, unique=False, nullable=False)

    user = db.relationship("UserModel", back_populates="record")
    category = db.relationship("CategoryModel", back_populates="record")


