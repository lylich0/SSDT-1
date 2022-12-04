from flask_smorest import Blueprint, abort
from flask.views import MethodView
from sqlalchemy.exc import IntegrityError
from database import db, UserModel
from schemas import UserSchema

users = []
blp = Blueprint("user", __name__, description="Operations on user")


@blp.route("/user")
class UserList(MethodView):
    @blp.response(200, UserSchema(many=True))
    def get(self):
        return UserModel.query.all()

    @blp.arguments(UserSchema)
    @blp.response(200, UserSchema)
    def post(self, user_data):
        user = UserModel(**user_data)
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            abort(404, message="User already exists")  # TODO test error message
        return user


@blp.route("/user/<string:uid>")
class User(MethodView):
    @blp.response(200, UserSchema)
    def get(self, uid: str):
        user = UserModel.query.get_or_404(uid)
        return user

    @blp.response(200, UserSchema)
    def delete(self, uid: str):
        user = UserModel.query.get_or_404(uid)
        db.session.delete(user)
        db.session.commit()
        return user