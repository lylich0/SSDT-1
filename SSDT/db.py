from sqlalchemy import Column, Integer, String
from SSDT.views import db


class UserModel(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class CategoryModel(db.Model):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class RecordModel(db.Model):
    __tablename__ = 'records'
    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    category_id = Column(String)
    date = Column(String)
    amount = Column(String)

